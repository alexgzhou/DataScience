
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
