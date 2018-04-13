## 笔记

### [7 Techniques to Handle Imbalanced Data](https://www.kdnuggets.com/2017/06/7-techniques-handle-imbalanced-data.html)

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/imbalanced-data-1.png)

1. 使用正确的评价指标

> Precision/Specificity:
> Recall/Sensitivity
> F1 score:precision和recall的调和平均数
> MCC：correlation coefficient between the observed and predicted binary classifications
> AUC

2. 对训练集重采样

> Under-sampling 
> Over-sampling： repetition, bootstrapping or SMOTE (Synthetic Minority Over-Sampling Technique)

3. 正确使用K折交叉验证

> 应在over-sampling之前使用交叉验证，以防止过拟合

4. 搭配不同的重新取样数据集

5. 用不用比率重新取样

6. Cluster the abundant class

7. Design your own models

## 下一步计划

* 对训练数据进行处理：切割patches时以每个MA像素点为中心分别在原图和手动分割图上相同位置切割（可能会有的问题是很多patch可能只是平移一个像素点的差别）