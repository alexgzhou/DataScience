library(utiml)
library(utiml,prudent)

library(mldr)

setwd("C://Users/King/Desktop/datasets")

algorithms = list('CAL500','corel5k', 'emotions', 'enron', 'genbase', 'medical', 'scene', 'yeast',
                  'rcv1subset1', 'rcv1subset5')

for (algorithm in algorithms) {
  
  mymld <- mldr(algorithm)
  folds <- create_kfold_partition(mymld, 
                                  k = 10, 
                                  method = "random")
  for (i in 1:10) {
    
    dataset <- partition_fold(folds,i)
    
    model <- prudent(dataset$train,phi=0.1)
    proba <- predict(model,dataset$test)
    pred <- fixed_threshold(proba)
    
    filename <- paste("./PruDent/",paste(algorithm,i,"pred", sep="-"),".csv",sep = "")
    write.csv(pred,filename)
    
    filename <- paste("./PruDent/",paste(algorithm,i,"std", sep="-"),".csv",sep = "")
    write.csv(mldr_to_labels(dataset$test),filename)
  }
}



