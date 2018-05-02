# 体检结论生成-20180418

## 本周工作：尝试训练

### 1. 尝试scikit-multilearn

* scikit-multilearn是多标签学习的包，内含基本的多标签学习算法
* 问题：无法预设模型的参数，即可以取出训练好的参数，但无法传递。

### 2. 用tensorflow构建基于线性回归的br分类

* 线性回归，W = [5, 3, 2] ; b = 8

	初始化 W[0] = 4, b = 7: 

	![](https://github.com/WindsOfWinter/picture/blob/master/p1.png)

	初始化 W = [5.1, 2, 1.5], b = 6:

	![](https://github.com/WindsOfWinter/picture/blob/master/p2.png)

	随机初始化（-1到1）：

	![](https://github.com/WindsOfWinter/picture/blob/master/p3.png)

* 只初始化一部分参数，可能结果还没有随机初始化好？

### 3. 训练

* 正在跑，跑得很慢