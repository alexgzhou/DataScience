# 本周内容

## 眼底血管微动脉瘤分割

### 数据及结果
* 数据集包括：original，RGB，jpg格式，250张，1944*2592；MA-Mask，单通道，png格式，500张（expert1和expert2各250张）
* 参数：采用patch-extract方法（64*64），共提取20000patches，batch-size（32），训练用了20张原图（一直提醒run out of memory...）
* 训练结果（橙色为acc，蓝色为loss）
![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/train_acc_loss-0329.png)

* 问题：样本每张图中的微动脉瘤数目少，且形状微小，导致负样本像素数目远大于正样本像素数目，以致于训练结果中准确率一直较高（0.974）且几乎不变

* 改进思路：扩充正样本像素数（1.扩大微动脉瘤区域，blur；2.人工添加微动脉瘤个数）

### 下一步计划

* 查阅文献看看针对这种正负样本极不均衡的数据集有什么好的解决方案
* 准备好方案收集菌落生长的数据集

