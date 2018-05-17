# 词嵌入周报20180516


## 计划：

解决上周word xx not in vocabulary的报错，对代码进行整合。
开始论文撰写

## 本周工作：

### 1.尝试修改分词方案以解决报错

用全模式分词，保证多样的分词结果

cutall = True

开启HMM新词发现模式，对于未登录词(词库中没有的词)，采用有汉字成词能力的 HMM 模型进行切分

HMM = True

代码修改如下：


 `   seg_list = jieba.cut(sentence, cut_all = True, HMM = True) `


运行结果：

有所改进，但在稍后仍出现了同样的error:(

### 2.尝试修改词嵌入过程以解决报错

在词嵌入过程中发现，默认模式下word2vec只处理出现次数超过5次的词，于是将min_count参数改为1.

运行结果：

仍出现了同样的error，
此处开始怀疑代码编写有错。

### 3.找到error原因

通过仔细查找，发现在分词的时候
`seg_list = [x for x in jieba.cut(sentence)]if len(x)>=2`

使得只有分词后不保留单字，造成了not in vocabulary的关键错误，

重新分词之后 发现原来的test_file不够准确（部分数据格式不准确），

于是重新做了一个test_file，

但中间出现了很多空行 是因为他们在csv中占同一格 ，

重新处理了一下数据，

程序正常运行结束。



## 下周工作

投入论文撰写工作