﻿# 词嵌入周报20180411


## 计划

按上周的思路进行代码的编写，尝试实现一个文本生成雏形。

## 本周工作

上周有了思路，同义词改写，模板改写，深度学习方法，其中，第一种方法可以预知效果不理想，因此想先尝试第二种模板法，主要思路为：将关键词与语料库中的模板进行关键词相似度比较，即将词向量与相应的句向量进行距离比较，并将相似度最高的句向量对应的原文本输出。


初步实验，结果尚可，但发现分句问题，且疾病并非完全符合：

![此处输入图片的描述][1]

![此处输入图片的描述][2]

这是因为在读取数据时用的是readline方法，即按文本一行一行读取，因此需要重新处理数据，将完整的模板写入一行。这种操作使得一行的文本变长，因此在程序运行时明显感到变慢，但输出效果提升。

![此处输入图片的描述][3]

![此处输入图片的描述][4]

## 存在问题：

需要将患者情况表达清楚详细，否则会出现如下情况：

![此处输入图片的描述][5]

## 下周目标：

考虑用深度学习的方法，尝试无模板生成，但效果有待考虑。

  
[1]: https://s9.postimg.org/ymq8kfqdb/20180411145045.png
  
[2]: https://s9.postimg.org/6zdj6eprz/20180411145414.png
  
[3]: https://s9.postimg.org/cc2dk3y4f/20180411145734.png
  
[4]: https://s9.postimg.org/cq3pjyakv/20180411150938.png
  
[5]: https://s9.postimg.org/s03kr90z3/20180411151747.png