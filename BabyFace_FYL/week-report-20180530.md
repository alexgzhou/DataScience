# BabyFace_FYL_周报
## abnormal_normal_densenetDataSet2.py运行结果
* 参数设置 num_epochs = 20  epoch_perrun = 5 batch_size = 10
### 混淆矩阵
![image](https://github.com/fyl0109/DataScience/blob/master/BabyFace_FYL/source/data2confusionmwithoutnormalization0.png)
### 归一化混淆矩阵
![image](https://github.com/fyl0109/DataScience/blob/master/BabyFace_FYL/source/data2confusionmwithnormalization0.png)
### ROC曲线
![image](https://github.com/fyl0109/DataScience/blob/master/BabyFace_FYL/source/roccurveselection0.png)
* 准确率0.7-0.8 原代码能到0.9
## 下周计划
* 将batch_size改回8，并增加训练次数，再训练一次模型
* tensorflow-gpu版本安装