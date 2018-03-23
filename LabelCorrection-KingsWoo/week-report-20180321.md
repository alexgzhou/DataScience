# 周报20180321

* 20180315 完成上周周报
* 20180315 对文件读取进行了优化
* 20180315 开始跑数据，MLKNN速度明显快于ECC
* 20180315 建立论文word文档，开始借鉴写作套路
---
* 20180316 实现BR在predictor中的集成
  - 单标签分类器使用sklearn.svm.SVC
  - 多标签实现使用skmultilearn.problem_transform.BinaryRelevance()
  - 通过predictor('br',...)调用
---
* 20180317 对顶层run.py进行修改，加入了时间戳和log记录过程
* 20180317 对原有改进函数（improve function）进行矫正，加入负分损失系数k且设定为10
---
* 20180319 联系Jun Huang, 尝试拿到LLSF和LPLC的原码
  - 已拿到，使用MATLAB编写
  - 先在MATLAB中跑出第一阶段结果，之后使用appendix算法，需要再写一个接口
* 20180319 已成功跑起LPLC，根据文献确定每个数据集的最优参数

    数据集名称|alpha|k
	:-----|:--|:--
	CAL500|0.7|13
	corel5k|0.7|5
	corel16k|0.7|5
	emotions|0.7|19
	rcv1...|1.0|9
	enron|0.7|21
	genbase|0.7|15
	medical|0.7|15	
	scene|0.7|11
	yeast|0.7|5
  - 使用数据时注意，原函数的x和y规模分别为n_x*d_x和d_y*n_y,与函数说明不一致
  - 还未进行数据接口的设定
  - 实验室电脑连导入数据至MATLAB的内存都没有...之后空闲要去向大佬请教服务器的使用方法
* 20180319 至ZY沟通应用场景
* 20180319 对算法进行了优化
  - 增加了通过validation确定cutoff moment的过程(vc)
---  
* 20180320 对算法进行优化
  - 调整了improve function，增加了显著性项
* 20180320 用MATLAB进行LPLC算法的学习（由于python3.5不支持mlab）：
  1. 使用.csv导入数据至MATLAB
  2. MATLAB格式化输出10折交叉验证结果
  3. python格式化读取.mat文件
  - 因为LPLC代码直接来自Jun Huang，同时有很多手动操作，因此没有上传至github
  - 完成了上述数据集基于LPLC的学习，下一步对每个数据集的结果进行改进，观察效果
* 20180320 细化了log所记录的时间节点，并实现实时存储
* 20180320 似乎之前增加的显著性项对算法效果产生了影响，准备之后再确认要不要拿掉
