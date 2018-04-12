# model evaluation

# resume model.xgb is the model object and the parameters have been optimized
score <- predict(model.xgb, newdata = model.data.test)
# summary(score)
label.pred <- ifelse(score >= 0.5, 1, 0)

label.eva <- data.frame(true = model.label.test, pred = label.pred, res = NA)


# classification evaluation
label.eva$res <- as.factor(unlist(lapply(1:nrow(label.eva), function(i){
  if(label.eva$true[i] == 1 && label.eva$pred[i] == 1){
    "tp"
  } else if(label.eva$true[i] == 0 && label.eva$pred[i] == 1){
    "fp"
  } else if(label.eva$true[i] == 1 && label.eva$pred[i] == 0){
    "fn"
  } else if(label.eva$true[i] == 0 && label.eva$pred[i] == 0){
    "tn"
  }
})))
summary(label.eva$res)
table(df6N$y2)

# ranking evaluation
require(ROCR)
# pred <- prediction(model.test, model.label)
pred <- prediction(score, model.label.test)
perf.roc <- performance(pred, "tpr", "fpr")
# perf.pre <- performance(pred, "prec", "rec")
perf.auc <- performance(pred, "auc")
plot(perf.roc)
# plot(perf.pre)
auc <- perf.auc@y.values[[1]]
