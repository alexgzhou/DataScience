require(xgboost)
require(ROCR)
require(DMwR)

set.seed(1212)

df7 <- read.csv(file.choose(), stringsAsFactors = F)

## increase the number of positive samples, direct sampling
# table(df7$y2)
# df7.p <- df7[which(df7$y2 == 1),]
# df7.p <- df7.p[(1:3000),]
# df7 <- rbind(df7,df7.p)

# class(df7$XINGBIE)
# df7$XINGBIE <- factor(df7$XINGBIE)
# df7$birthyear <- as.numeric(substr(df7$CHUSHENGRQ,1,4))
df7$tjyear <- as.numeric(substr(df7$TIJIANRQ,1,4))
df7$age <- df7$tjyear-df7$birthyear
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
df7 <- df7[which(!is.na(df7$DBP) & !is.na(df7$SBP) & !is.na(df7$DBP2) & !is.na(df7$SBP2)), ]
# df7 <- df7[which(!is.na(df7$DBP) & !is.na(df7$SBP)), ]
df7$XINGBIEs <- ifelse(df7$XINGBIE == 2, 0, 1)
df7$ages <- df7$age/100
df7$BMIs <- (df7$BMI - mean(df7$BMI))/sd(df7$BMI)
df7$DBPs <- (df7$DBP - mean(df7$DBP))/sd(df7$DBP)
df7$SBPs <- (df7$SBP - mean(df7$SBP))/sd(df7$SBP)
df7$FBGs <- (df7$FBG - mean(df7$FBG))/sd(df7$FBG)
df7$TGs <- (df7$TG - mean(df7$TG))/sd(df7$TG)
df7$HDLs <- (df7$HDL - mean(df7$HDL))/sd(df7$HDL)
df7$BMI2s <- (df7$BMI2 - mean(df7$BMI2))/sd(df7$BMI2)
df7$DBP2s <- (df7$DBP2 - mean(df7$DBP2))/sd(df7$DBP2)
df7$SBP2s <- (df7$SBP2 - mean(df7$SBP2))/sd(df7$SBP2)

## now using SMOTE to create a more "balanced problem"
## perc.over = xx 表示少样本变成原来的（1+xx/100）倍;perc.under=yy 表示多样本变成少样本的 yy/100 *(xx/100)倍
# df7.imp <- df7[,c("XINGBIEs","ages","DBPs", "SBPs", "FBGs", "TGs", "HDLs", "BMIs","BMI2s","y2")]  # All data has Na's
# df7.imp <- df7[,c("XINGBIE","age","DBP", "SBP", "FBG", "TG", "HDL", "BMI","y","BMI2","y2")]
df7.imp$Species <- factor(ifelse(df7.imp$y2 == "1","rare","common"))
table(df7.imp$Species)
prop.table(table(df7.imp$Species))
df7.imp.new <- SMOTE(Species ~ ., df7.imp, perc.over = 100, perc.under = 390) # perc.over是100整数倍，多则取整百有效
table(df7.imp.new$y2)
table(df7.imp.new$y2)
prop.table(table(df7.imp.new$y2))
df7 <- df7.imp.new
# df7 <- df7.imp.new[,c(2,1,9,(3:8),10)]

df7$rowname <- seq(1:nrow(df7))
rownames(df7) <- df7$rowname

# rownames(df7) <- df7$TIJIANBM
## 用作df4的feature importance，后面y2转为y
# df7 <- df7[,c("XINGBIEs","ages","DBPs", "SBPs", "FBGs", "TGs", "HDLs", "BMIs","y")]
# features <- c("XINGBIEs","ages","DBPs", "SBPs", "FBGs", "TGs", "HDLs", "BMIs")

features <- c("XINGBIEs","ages","DBPs", "SBPs", "FBGs", "TGs", "HDLs", "BMIs","BMI2s")
# features <- c("XINGBIE","age","DBP", "SBP", "FBG", "TG", "HDL", "BMI","BMI2")
# features <- colnames(df7) %in% c("XINGBIE","age","DBP", "SBP", "FBG", "TG", "HDL", "TLDL", "BMI")
model.data <- df7[, colnames(df7) %in% features]
model.label <- data.frame(label = df7$y2)
rownames(model.label) <- rownames(model.data)

# model.label.a <- df7[, c("y2", "TG")]
# model.label.b <- df7$y2

## training set and test set
tr.size <- 2/3

size <- round(summary(factor(df7$y2)) * tr.size)
tmp.id <- lapply(1:length(size), function(j){
  sample(rownames(df7[which(df7$y2 == (j - 1)), ]), size[j])
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
  eta = 0.3,
  # max_depth = 3,
  # subsample = 0.7,
  # objective = "binary:logistic"
  objective = "reg:logistic"
)
# nrounds <- 20
# model.xgb <- xgboost(data = model.data.train, label = model.label.train, 
#                      nrounds = nrounds, params = params, 
#                      verbose = 1, save_period = NULL, eval_metric = "error")
# plot(model.xgb$evaluation_log)

## modeling xgb.train
## find best nrounds
# nrounds <- 400
nrounds <- 400
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
xgb.plot.importance(model.imp[1:9,])

