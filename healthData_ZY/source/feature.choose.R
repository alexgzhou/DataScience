require(xgboost)
require(ROCR)
require(DMwR)
require("corrplot")
set.seed(1212)

# 用全部数据计算feature importance
df5all <- read.csv(file.choose(), stringsAsFactors = F)
df5all <- df5all[which(!is.na(df5all$DBP) & !is.na(df5all$SBP) & !is.na(df5all$SBP2) & !is.na(df5all$DBP2)), ]
df5allt <- df5all[,c(26,44,31,4:8,32,26,44,37:42,36)]
df5c1 <- as.data.frame(df5allt[,c(1:9)],stringsAsFactors = FALSE)
df5c2 <- as.data.frame(df5allt[,c(10:18)],stringsAsFactors = FALSE)
colnames(df5c2) <- c("XINGBIE", "age","BMI","DBP","SBP","FBG","TG","HDL","y")
df5c <- rbind(df5c1,df5c2)
# df5c.cor <- cor(df5c)
# corrplot(df5c.cor,method="color",addCoef.col="grey")
# df7 <-df5c

df7 <- read.csv(file.choose(), stringsAsFactors = F)
df7l <- df7
df7 <- df7l[which(df7l$y == 0), ]
## increase the number of positive samples, direct sampling
# table(df7$y2)
# df7.p <- df7[which(df7$y2 == 1),]
# df7.p <- df7.p[(1:3000),]
# df7 <- rbind(df7,df7.p)

# class(df7$XINGBIE)
# df7$XINGBIE <- factor(df7$XINGBIE)
# df7$birthyear <- as.numeric(substr(df7$CHUSHENGRQ,1,4))
df7$tjyear <- as.numeric(substr(df7$TIJIANRQ,1,4))
df7$age <- df7$tjyear-as.numeric(df7$birthyear)+1
# hist(df7$age)
# df7$ageGroup <- ifelse(
#   df7$age<=30, "(0,30]",  
#    ifelse(  
#      df7$age<=35, "(30,35]",
#      ifelse(  
#        df7$age<=40, "(35,40]",
#        ifelse(  
#          df7$age<=45, "(40,45]",
#          ifelse(  
#            df7$age<=50, "(45,50]", 
#            ifelse(
#              df7$age<=55,"(50,55]",
#              ifelse(
#                df7$age<=65,"(55,65]","(65,+)" 
#              )
#            )
#          )  
#        )  
#      )  
#    )  
#  )

# df7$ageGroup <- ifelse(
#   df7$age<=30, 1,
#   ifelse(
#     df7$age<=35, 2,
#     ifelse(
#       df7$age<=40, 3,
#       ifelse(
#         df7$age<=45, 4,
#         ifelse(
#           df7$age<=50, 5,
#           ifelse(
#             df7$age<=55,6,
#             ifelse(
#               df7$age<=65,7,8
#             )
#           )
#         )
#       )
#     )
#   )
# )
# class(df7$ageGroup)
# df7$ageGroup <- factor(df7$ageGroup)

## standardization
# summary(df7)
df7 <- df7[which(!is.na(df7$DBP) & !is.na(df7$SBP) ), ]
# df7 <- df7[which(!is.na(df7$DBP) & !is.na(df7$SBP)), ]
# df7$XINGBIEs <- df7$XINGBIE
df7$XINGBIEs <- ifelse(df7$XINGBIE == 2, 0, 1)
# df7$ages <- df7$age/100
df7$ages <- (df7$age - mean(df7$age))/sd(df7$age)
df7$BMIs <- (df7$BMI - mean(df7$BMI))/sd(df7$BMI)
df7$DBPs <- (df7$DBP - mean(df7$DBP))/sd(df7$DBP)
df7$SBPs <- (df7$SBP - mean(df7$SBP))/sd(df7$SBP)
df7$FBGs <- (df7$FBG - mean(df7$FBG))/sd(df7$FBG)
df7$TGs <- (df7$TG - mean(df7$TG))/sd(df7$TG)
df7$HDLs <- (df7$HDL - mean(df7$HDL))/sd(df7$HDL)
df7$BMI2s <- (df7$BMI2 - mean(df7$BMI2))/sd(df7$BMI2)
# df7$DBP2s <- (df7$DBP2 - mean(df7$DBP2))/sd(df7$DBP2)
# df7$SBP2s <- (df7$SBP2 - mean(df7$SBP2))/sd(df7$SBP2)

# 针对y=1的组别实施label 01调换
# df7$y2 <- ifelse(df7$y2 == 1, 0, 1)

df7$rowname <- seq(1:nrow(df7))
rownames(df7) <- df7$rowname

# rownames(df7) <- df7$TIJIANBM
## 用作df4的feature importance，后面y2转为y
# df7 <- df7[,c("XINGBIEs","ages","DBPs", "SBPs", "FBGs", "TGs", "HDLs", "BMIs","y")]
# features <- c("XINGBIEs","ages","DBPs", "SBPs", "FBGs", "TGs", "HDLs", "BMIs")

# features <- c("XINGBIE", "age","BMIs","DBPs","SBPs","FBGs","TGs","HDLs")
features <- c("BMIs","DBPs","SBPs","FBGs","TGs","HDLs")
# features <- c("XINGBIEs","ages","BMIs","DBPs", "SBPs", "FBGs", "TGs", "HDLs")
# features <- colnames(df7) %in% c("XINGBIE","age","DBP", "SBP", "FBG", "TG", "HDL", "TLDL", "BMI")
model.data <- df7[, colnames(df7) %in% features]
model.label <- data.frame(label = df7$y)
rownames(model.label) <- rownames(model.data)

# model.label.a <- df7[, c("y2", "TG")]
# model.label.b <- df7$y2

## training set and test set
tr.size <- 1/4

size <- round(summary(factor(df7$y)) * tr.size)
tmp.id <- lapply(1:length(size), function(j){
  sample(rownames(df7[which(df7$y == (j - 1)), ]), size[j])
})
id.train <- unlist(tmp.id)
# id.test <- as.character(setdiff(df7$TIJIANBM, id.train))
id.test <- as.character(setdiff(df7$rowname, id.train))

model.data.train <- as.matrix(model.data[id.train, ])
model.label.train <- as.matrix(model.label[id.train, ])
model.data.test <- as.matrix(model.data[id.test, ])
model.label.test <- as.matrix(model.label[id.test, ])

## modeling xgboost
params.xgb <- list(
  booster = "gbtree",
  # booster = "gblinear",
  eta = 0.2,
  # max_depth = 3,
  # subsample = 0.7,
  # objective = "binary:logistic"
  objective = "reg:logistic"
)
# model.xgb <- xgboost(data = model.data.train, label = model.label.train, 
#                      nrounds = nrounds, params = params, 
#                      verbose = 1, save_period = NULL, eval_metric = "error")
# plot(model.xgb$evaluation_log)

## modeling xgb.train
## find best nrounds
nrounds <- 150
# nrounds <- 100
model.Ddata <- xgb.DMatrix(model.data.train, label = model.label.train)
model.Dtest <- xgb.DMatrix(model.data.test, label = model.label.test)
watchlist <- list(eval = model.Dtest, train = model.Ddata)
model.xgb <- xgb.train(params.xgb, model.Ddata, nrounds = nrounds, 
                       verbose = 1, save_period = NULL, 
                       eval_metric = "auc", watchlist = watchlist, 
                       callbacks = list(cb.evaluation.log()))
curve(model.xgb$evaluation_log$train_auc[x], 1, nrounds)
curve(model.xgb$evaluation_log$eval_auc[x], 1, nrounds, add = TRUE)
nrounds.best <- model.xgb$evaluation_log$iter[which.max(model.xgb$evaluation_log$eval_auc)]

## # analyze features importance
model.imp <- xgb.importance(features, model.xgb)
# plot
xgb.plot.importance(model.imp[1:9,],cex.axis=1.5,cex.lab=1.5, family="A")
legend(x = "bottomright", legend = c("a","b"), title = "legend", col = c("blue", "red"), lty = c(1, 1))
