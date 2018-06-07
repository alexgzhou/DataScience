## 无菌检测
- 这周就测试了一下模拟侧面贴二维码后对拍得的图像的影响，特定角度下完全没有影响的最大宽度是29mm
- 数据待预处理

- 下一步工作计划
    - 检测目标：	1，浊度识别：自动识别微生物生长的浊度变化，并进行结果判定；2，可见异物识别：自动识别1mm或更小的徐庄、颗粒状、丝状等可见异物（菌落），并进行结果判定
    - 文献调研可行性，再制定具体计划

## chestCamera

1. freeze the weight

之前用的方法：
```
for layer in model.layers[:100]:
    layer.trainable = False
```
没有错，但是训练效果会变差；后面发现是因为在执行过程中，如依次设置1-500、1-400、1-300、1-200等，前面的设置会覆盖后面的设置，也就是说每次变更权重的可训练性时，其实都没有变。
后面再每次变更前都设置了一遍所有的权重都是trainable=true，再固定前数层的权重不训练，重新run了之后发现结果（auc=0.6）并没有比全参数训练时的效果（auc≈0.7）好，重新查看每次循环中的模型参数统计，发现了新的问题：

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/params.png)

图中1是basemodel的参数统计，2是更改basemodel最后两层后的模型参数统计，3~6是每次变更参数可训练性后的参数统计，然后就发现trainable params数一直没有变，total 和non-trainable数一直在变化没有规律。。。


换一个设置思路：先全部设置trainable=false，然后每次变更时设置true的数据（待测试）

2. cross validation

- 先用了一个简单的模型测试通了图像数据的交叉验证方法

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/cv5-model.png)

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/cv5-output.png)

- 初步结果不是很理想，后面还要继续调整