## 上周工作

### patch方法1

在切patch时，以标记中的MA点为中心切割

* 测试结果（threshold=0.5）
ROC

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/ROC-0423.png)

RP曲线

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/Precision_recall-0423.png)

```
Area under the ROC curve: 0.6770082133707085
Area under Precision-Recall curve: 0.0022216137670928978
Jaccard similarity score: 0.9479866912668149
F1 score (F-measure): 0.005257828662770824

Confusion matrix:
[[47674731  2557487]
 [   58668     6914]]
ACCURACY: 0.947986691267
SENSITIVITY: 0.105425269129
SPECIFICITY: 0.949086719603
PRECISION: 0.00269614619554
```

### patch方法2

以（0，0）为起始中心点，step步长滑窗切割，保留中心点是MA的patch

* 训练结果

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/train_acc_loss-0423.png)

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/validation_acc_loss-0423.png)

* 测试结果（threshold=0.5）

ROC

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/ROC-0423byStep.png)

RP曲线

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/Precision_recall-0423byStep.png)

```
Area under the ROC curve: 0.6652803430223589
Area under Precision-Recall curve: 0.050938328770136064
Jaccard similarity score: 0.9506529311421176
F1 score (F-measure): 0.0051529016134882885

Confusion matrix:
[[47809323  2422895]
 [   59154     6428]]
ACCURACY: 0.950652931142
SENSITIVITY: 0.0980146991553
SPECIFICITY: 0.951766115524
PRECISION: 0.00264600466879
```

## 问题

虽然改变了训练patch，使得正负像素样本比例相对协调，但测试结果还是很糟糕（测试图像正负样本像素比例严重不均衡）

## 下周计划

1. dilate object mask (高斯模糊扩大MA标签区域大小)
2. change UNet (pooling，convolution，dropout等参数调整，gabor filter to initilize kernels等)