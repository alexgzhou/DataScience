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
  
  if ((algorithm == "scene") | (algorithm == "medical")) {
    phi = 0.02
  }else{
    phi = 0.1
  }
  
  for (i in 1:10) {
    
    dataset <- partition_fold(folds,i)
    
    train <- dataset$train
    test <- dataset$test
    
    label <- train$labels
    indexes <- label$index[label$count == 0]

    
    train <- remove_labels(train, indexes)
    test <- remove_labels(test, indexes)
    
    test_x <- test$dataset[test$attributesIndexes]
    train_x <- train$dataset[train$attributesIndexes]
    test_y <- test$dataset[test$labels$index]
    train_y <- train$dataset[train$labels$index]
    
    test_n <- test$measures$num.instances
    
    xs <- rbind(test_x,train_x)
      
    model <- prudent(train,phi=phi)
    pred <- as.bipartition(predict(model,xs)[0:test_n,])
    
    zero_n <- length(indexes)
      
    pred <- cbind(pred, array(0,dim=c(test_n,zero_n)))
    std <- cbind(test_y, array(0,dim=c(test_n,zero_n)))
    
    filename <- paste("./PruDent/",paste(algorithm,i,"pred", sep="-"),".csv",sep = "")
    write.csv(pred,filename)
    
    filename <- paste("./PruDent/",paste(algorithm,i,"std", sep="-"),".csv",sep = "")
    write.csv(std,filename)
  }
}



