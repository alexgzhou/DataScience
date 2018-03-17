# 周报20180314

* 20180315 完成上周周报
* 20180315 对文件读取进行了优化
* 20180315 开始跑数据，MLKNN速度明显快于ECC
* 20180315 建立论文word文档，开始借鉴写作套路

* 20180316 实现BR在predictor中的集成
  - 单标签分类器使用sklearn.svm.SVC
  - 多标签实现使用skmultilearn.problem_transform.BinaryRelevance()
  - 通过predictor('br',...)调用
* 20180316 实现RAkEL在predictor中的集成
  - 代码来源 https://github.com/NLeSC/embodied-emotions-scripts
  - 在源代码基础上进行了一定修改及参数矫正

* 20180317 对顶层run.py进行修改，加入了时间戳和log记录过程
* 20180317 对原有改进函数（improve function）进行矫正，加入负分损失系数k且设定为10
