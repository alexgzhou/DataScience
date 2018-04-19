
## 训练时，Patch切割方法改进

* 在切patch时，以标记中的MA点为中心切割
```
大小：64*64
共20000张
epochs：100
```

> epochs=100时，loss: 0.0044 - acc: 0.9983 - val_loss: 1.1921e-07 - val_acc: 1.0000

* 切割patch样本

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/patch-sample.png)

> 输入原图为什么是红色？

## 训练结果：

* Train ACC和LOSS

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/train_acc_loss-0418.png)

* Validation ACC和LOSS

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/validation_acc_loss-0418.png)

* Test

模型参数因报错中断未能保存，后面会再次训练和测试


## 问题
1. 输入样本可视化之后不知道为什么是红色的，打算用其它可视化方法确认一下输入样本
2. 改变切割patch方法之后，虽然训练Acc和Loss曲线有所改善（从不变到逐渐上升至收敛），但是收敛epoch数很小（10左右），且验证集Acc一直为1，还是存在比较大的问题。可能的原因大概有：①这种切割方法切出来的相邻patch间可能只是平移一个或几个像素的差别，相对差别很小；②groundtruth中用的都是相同大小的方块标记MA，跟实际MA大小的差别应该较大，导致训练图像单一。

## 下周
1. 调整patch切割方法
2. 更换数据集（e_ophtha_MA.zip）？