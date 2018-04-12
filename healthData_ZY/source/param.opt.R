## xgb parameter optimization

# nrounds <- 50
nrounds <- 200
params.xgb <- list(
  booster = "gbtree",
  gamma = 0, 
  max_depth = 6, 
  min_child_weight = 1, 
  max_delta_step = 0, 
  subsample = 0.7, 
  colsample_bytree = 1, 
  # booster = "gblinear", 
  # objective = "binary:logistic"
  objective = "reg:logistic"
)
# params.xgb$eta <- 0.1

params.xgb.grid <- list()


watchlist <- list(eval = model.Dtest, train = model.Ddata)
model.xgb <- xgb.train(params.xgb, model.Ddata, nrounds = nrounds, 
                       verbose = 1, save_period = NULL, 
                       eval_metric = "auc", watchlist = watchlist, 
                       callbacks = list(cb.evaluation.log()))
curve(model.xgb$evaluation_log$train_auc[x], 1, nrounds)
curve(model.xgb$evaluation_log$eval_auc[x], 1, nrounds, add = TRUE)


## max_depth, min_weight
mydepth <- c(3, 4, 5, 6, 7, 8, 9)
mycweight <- c(1, 2, 3, 4, 5, 6)
param.test1 <- matrix(NA, length(mydepth), length(mycweight))
colnames(param.test1) <- mycweight
rownames(param.test1) <- mydepth
for (i in 1:length(mydepth)){
  for (j in 1:length(mycweight)){
    params.xgb$max_depth <- mydepth[i]
    params.xgb$min_child_weight <- mycweight[j]
    
    model.xgb <- xgb.train(params.xgb, model.Ddata, nrounds = nrounds, 
                           verbose = 1, save_period = NULL, 
                           eval_metric = "auc", watchlist = watchlist, 
                           callbacks = list(cb.evaluation.log()))
    param.test1[i, j] <- max(model.xgb$evaluation_log$eval_auc)
    # curve(model.xgb$evaluation_log$train_auc[x], 1, nrounds)
    # curve(model.xgb$evaluation_log$eval_auc[x], 1, nrounds, add = TRUE)
  }
}

opt.res <- which(param.test1 == max(param.test1), arr.ind = TRUE)
max_depth <- mydepth[opt.res[1]]
min_child_weight <- mycweight[opt.res[2]]


## gamma 
# params.xgb <- list(
#   booster = "gbtree",
#   gamma = 0, 
#   max_depth = max_depth, 
#   min_child_weight = min_child_weight, 
#   max_delta_step = 0, 
#   subsample = 0.7, 
#   colsample_bytree = 1, 
#   # booster = "gblinear", 
#   # objective = "binary:logistic"
#   objective = "reg:logistic"
# )
params.xgb$max_depth <- max_depth
params.xgb$min_child_weight <- min_child_weight
param.test2 <- rep(0, 10)
for (i in 0:10) {
  params.xgb$gamma <- i/10
  model.xgb <- xgb.train(params.xgb, model.Ddata, nrounds = nrounds, 
                         verbose = 1, save_period = NULL, 
                         eval_metric = "auc", watchlist = watchlist, 
                         callbacks = list(cb.evaluation.log()))
  param.test2[i] <- max(model.xgb$evaluation_log$eval_auc)
}

opt.res <- which(param.test2 == max(param.test2), arr.ind = TRUE)
gamma <- (opt.res-1) / 10


## subsample, colsample_bytree
params.xgb <- list(
  booster = "gbtree",
  gamma = gamma, 
  max_depth = max_depth, 
  min_child_weight = min_child_weight, 
  max_delta_step = 0, 
  subsample = 0.7, 
  colsample_bytree = 1, 
  # booster = "gblinear", 
  # objective = "binary:logistic"
  objective = "reg:logistic"
)
mysubsample <- 5:10/10
mycolsbytree <- 5:10/10
param.test3 <- matrix(NA, length(mysubsample), length(mycolsbytree))
colnames(param.test3) <- mysubsample
rownames(param.test3) <- mycolsbytree
for (i in 1:length(mysubsample)){
  for (j in 1:length(mycolsbytree)){
    params.xgb$subsample <- mysubsample[i]
    params.xgb$colsample_bytree <- mycolsbytree[j]
    
    model.xgb <- xgb.train(params.xgb, model.Ddata, nrounds = nrounds, 
                           verbose = 1, save_period = NULL, 
                           eval_metric = "auc", watchlist = watchlist, 
                           callbacks = list(cb.evaluation.log()))
    param.test3[i, j] <- max(model.xgb$evaluation_log$eval_auc)
    # curve(model.xgb$evaluation_log$train_auc[x], 1, nrounds)
    # curve(model.xgb$evaluation_log$eval_auc[x], 1, nrounds, add = TRUE)
  }
}

opt.res <- which(param.test3 == max(param.test3), arr.ind = TRUE)
subsample <- mysubsample[opt.res[1]]
colsample_bytree <- mycolsbytree[opt.res[2]]


## max_delta_step 
params.xgb <- list(
  booster = "gbtree",
  gamma = gamma, 
  max_depth = max_depth, 
  min_child_weight = min_child_weight, 
  max_delta_step = 0, 
  subsample = subsample, 
  colsample_bytree = colsample_bytree, 
  # booster = "gblinear", 
  # objective = "binary:logistic"
  objective = "reg:logistic"
)
mymaxdstep <- 0:10
param.test4 <- rep(0, length(mymaxdstep))
for (i in 0:(length(mymaxdstep)-1)) {
  params.xgb$gamma <- mymaxdstep[i+1]
  model.xgb <- xgb.train(params.xgb, model.Ddata, nrounds = nrounds, 
                         verbose = 1, save_period = NULL, 
                         eval_metric = "auc", watchlist = watchlist, 
                         callbacks = list(cb.evaluation.log()))
  param.test4[i+1] <- max(model.xgb$evaluation_log$eval_auc)
}

opt.res <- which(param.test4 == max(param.test4), arr.ind = TRUE)
max_delta_step <- mymaxdstep[opt.res]

param.xgb.gbtree.opted <- list(
  booster = "gbtree", 
  gamma = gamma, 
  max_depth = max_depth, 
  min_child_weight = min_child_weight, 
  max_delta_step = max_delta_step, 
  subsample = subsample, 
  colsample_bytree = colsample_bytree, 
  objective = "reg:logistic"
)
# > param.xgb.gbtree.opted
# $booster
# [1] "gbtree"
# 
# $gamma
# [1] 0.4
# 
# $max_depth
# [1] 4
# 
# $min_child_weight
# [1] 3
# 
# $max_delta_step
# [1] 7
# 
# $subsample
# [1] 0.9
# 
# $colsample_bytree
# [1] 1
# 
# $objective
# [1] "reg:logistic"

# > param.xgb.gbtree.opted
# $booster
# [1] "gbtree"
# 
# $gamma
# [1] 0.1
# 
# $max_depth
# [1] 3
# 
# $min_child_weight
# [1] 6
# 
# $max_delta_step
# [1] 8
# 
# $subsample
# [1] 0.9
# 
# $colsample_bytree
# [1] 0.9
# 
# $objective
# [1] "reg:logistic"
