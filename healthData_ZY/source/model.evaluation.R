# model evaluation
# resume model.xgb is the model object and the parameters have been optimized
score <- predict(model.xgb, newdata = model.data.test)

## 密度曲线
require(ggplot2)
model.score.label <- data.frame(score = score, y2 = model.label.test)
model.score.label$y2 = factor(model.score.label$y2)
# 基函数：x设置目标变量，fill设置填充色
ggplot(model.score.label, aes(x = score, fill = y2)) +
  geom_density(alpha = 0.3) # 密度曲线函数：alpha设置填充色透明度

# summary(score)
label.pred <- ifelse(score >= 0.425, 1, 0)

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
# 0.425
fn <- 897
fp <- 576
tn <- 17503
tp <- 8375

# delete 0.425
fn <- 865
fp <- 563
tn <- 17469
tp <- 8383


eva.TPR <- tp/(tp+fn)
eva.TNR <- tn/(tn+fp)
eva.PPV <- tp/(tp+fp)
eva.npv <- tn/(tn+fn)
eva.ACC <- (tp+tn)/(tp+tn+fp+fn)
eva.F1 <- 2*tp/(2*tp+fp+fn)


# table(df7$y2)

# ranking evaluation
require(ROCR)
# pred <- prediction(model.test, model.label)
# help("performance")
pred <- prediction(score, model.label.test)
perf.roc <- performance(pred, "tpr", "fpr")
perf.PR <- performance(pred, "prec", "rec")   # PR曲线，得到Error rate
perf.SeSp <- performance(pred, "sens", "spec")
perf.lift <- performance(pred, "lift", "rpp")
perf.gains <- performance(pred, "prec", "rpp")
perf.lorenz <- performance(pred, "rec", "rpp")

# perf.pre <- performance(pred, "prec", "rec")
perf.auc <- performance(pred, "auc")
par(cex.axis=1.5,cex.lab=1.5)
plot(perf.roc,lwd=2,colorize=TRUE, family="A")
plot(perf.PR,lwd=2,colorize=TRUE,xlab="Recall",ylab="Precision", family="A")
plot(perf.SeSp,lwd=2,colorize=TRUE,xlab="Specificity",ylab="Sensitivity", family="A")
plot(perf.lift,lwd=2,colorize=TRUE,xlab="Rate of positive predictions",ylab="Lift", family="A")
plot(perf.gains,lwd=2,colorize=TRUE,xlab="rpp",ylab="Precision", family="A")
plot(perf.lorenz,lwd=2,colorize=TRUE,xlab="rpp",ylab="Recall", family="A")
# plot(perf.pre)
auc <- perf.auc@y.values[[1]]
