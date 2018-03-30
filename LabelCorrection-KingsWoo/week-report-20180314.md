# 周报20180314

## 数据集获取与预处理
### 所使用数据集包括：
* CAL500 
* corel5k 
* corel16k001 
* corel16k002 
* corel16k003 
* emotions 
* enron
* genbase 
* medical 
* rcv1subset1 
* rcv1subset5 
* scene 
* yeast
### 完成了将.arff文件转换为.csv格式的过程（FYL）
* .arff文件可以通过weka软件打开，从而在.arff和.csv之间相互转换
* .arff文件可以支持数据的**矩阵表达**和**稀疏表达**，在使用**稀疏表达**时其大小会远小于.csv文件
### 完成了对数据集x,y矩阵的切割
* 基于数据集提供的y标签列表，通过readfile.divide_csv实现 (in source)
* 所使用的库是python原生csv库中csv.reader，返回一个迭代器，直接使用以下代码获取
> data = [row for row in reader] 
### 完成.csv数据读取模块readfile.read_csv
* csv默认带标签,将会把文件内的第一行分离

## 算法实现
* 实现了appendix标签矫正算法，方法名为appendix.regression_method
* 移植了MLkNN算法，封装在predictor.mlknn内
  - 基于scikit-multilearn
* 移植了ECC算法，封装在predictor.ecc内 
  - 基于scikit-learn以及https://github.com/hussainzaidi/cce
  - 可以尝试使用skml库，但是python3.5里没有
* 使用predictor.predictor作为调度算法
* 完成了自动算法验证与结果存储的过程
  - main.single_training_process(...)能够实现特定算法、数据集和折数的验证
  - 通过调整run.py内的参数即可实现自动算法验证

## 结果输出
* 每次验证会输出五个文件，分别是：

文件名 | 说明
:-----|:---------
...impro.csv|对标签分别进行矫正时的提升效果
...values.csv|标签矫正过程的参数曲线
...y_std.csv|所选择训练集所对应的金标准
...y_ori.csv|矫正前算法得到的预测结果
...y_adv.csv|矫正后算法得到的预测结果
* 典型的参数曲线（对应values）如图所示

![参数曲线](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/values.PNG)
* 典型的单标签矫正效果（对应impro）如图所示

![矫正效果](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/impro.PNG)
