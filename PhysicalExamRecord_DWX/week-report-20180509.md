# 体检结论生成-20180509

## 本周工作：合并分类器

### 1. 用一批新的测试样本测试，发现基本上所有排在后面（差不多100以后）的标签，没有分类器可以预测出positive的值。因为这些标签所拥有的正样本过少。

* 对每个标签，挑选出预测效果最好的分类器（下面是每行一个标签，它的最高F值和训练它精度最高的分类器号）：

![](https://github.com/WindsOfWinter/picture/blob/master/0509%206.png)

### 2. 动态阈值法，找到使F值最大的linear regression的阈值。
* 对每个标签，挑选出预测效果最好的分类器（下面是每行一个标签，它的最高F值和训练它精度最高的分类器号）：

![](https://github.com/WindsOfWinter/picture/blob/master/0509%207.png)

### 3. 用加权投票的方法得出每个标签的最终分类结果。

![](https://github.com/WindsOfWinter/picture/blob/master/0509%205.png)

### 4. 下周计划

* 检查代码问题
* 重采样（加大正样本比例）训练，以提高不太长出现标签的训练效果。使用另外的loss function