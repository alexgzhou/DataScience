library(utiml)
library(utiml,prudent)

library(mldr)

setwd("C://Users/King/Desktop/datasets")

algorithms = list('scene', 'yeast')

for (algorithm in algorithms) {
  
  mymld <- mldr(algorithm)
  folds <- create_kfold_partition(mymld, 
                                  k = 10, 
                                  method = "random")
  
  for (i in 1:10) {
    
    dataset <- partition_fold(folds,i)
    
    train <- dataset$train
    test <- dataset$test
    
    label <- train$labels
    indexes <- label$index[label$count == 0]
    
    train <- remove_labels(train, indexes)
    test <- remove_labels(test, indexes)
    
    model <- dbr(train)
    pred <- as.bipartition(predict(model,test))
    
    test_n <- test$measures$num.instances
    zero_n <- length(indexes)
    
    pred <- cbind(pred, array(0,dim=c(test_n,zero_n)))
    std <- cbind(test$dataset[test$labels$index], array(0,dim=c(test_n,zero_n)))
    
    filename <- paste("./DBR/",paste(algorithm,i,"pred", sep="-"),".csv",sep = "")
    write.csv(pred,filename)
    
    filename <- paste("./DBR/",paste(algorithm,i,"std", sep="-"),".csv",sep = "")
    write.csv(std,filename)
  }
}



