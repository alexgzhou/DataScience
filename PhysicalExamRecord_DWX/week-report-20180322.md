## 体检结论生成-3DUnetCNN-20180314

### 1.导出数据

* 由于各个软件版本不一致，连接数据库花了很久时间。要注意python，instantclient，plsql的版本要保持一致。

### 2.稀疏性分析

* 选取100条患者数据，计算其检查项目（x）有异常的个数，和体检结论（y）有对应问题的个数，观察x/y的结果。
* x/y 小于1的情况占16%，大于1的情况占65%，可知检查结论不是简单的一对一。
* 最终有无意义还是要看训练出模型的参数。

### 3.数据分析

* 有近300条特征没有使用过，可以直接舍去。x和y的数量不一致，将来做的时候要筛掉有x但没有y的患者。存在一个检查项目同时属于多个项目组的情况，所以不能用项目组来直接分类。
* 从每个特征的出现次数看，数据是可以大致按体检套餐分类的。

### 4.进一步工作

* 将检查数据根据体检套餐的不同进行分类
* 进行分批次学习

