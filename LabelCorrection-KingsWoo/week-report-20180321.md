﻿# 周报20180321

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
  - 现在MATLAB中跑出第一阶段结果，之后使用appendix算法，需要再写一个接口
* 20180319 至ZY沟通应用场景
* 20180319 对算法进行了优化
  - 增加了通过validation确定cutoff moment的过程(vc)