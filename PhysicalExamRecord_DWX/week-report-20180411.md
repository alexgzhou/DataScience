# 体检结论生成-20180411

## 本周工作：构建训练顺序

### 1.调整特征排列顺序

* 调整前（按完成次数排序）：
* 调整后（按相似度排序）：
* ![](https://github.com/WindsOfWinter/picture/blob/master/compare.png)

### 2.寻找合适的分组数目
* k=20：共270个特征可被利用，分为63组
* k=30：共280个特征可被利用，分为77组
* k=50：共380个特征可被利用，分为90组
* 即k越大，能利用到的特征越多，同时训练步骤越复杂

### 3.构建训练的树
* k=50，共90组特征。示意图如下：
* ![](https://github.com/WindsOfWinter/picture/blob/master/tree.png)

### 4.下周计划
* 训练模型，计算评价指标

