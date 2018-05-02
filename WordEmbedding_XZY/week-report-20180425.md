# 词嵌入周报20180425


## 计划：

尝试Lsi、Lda以及word2vec方法并比较结果

## 本周工作：

输入疾病为：子宫 肌瘤

tf-idf方法：

![此处输入图片的描述][1]

Lsi方法：

![此处输入图片的描述][2]

Lda方法：

![此处输入图片的描述][3]

word2vec方法：

![此处输入图片的描述][4]

可以看出word2vec方法相似匹配度较差

在使用word2vec方法时，发现经常出现如下报错：

![此处输入图片的描述][5]

怀疑是因为word2vec在转换词向量时的参数设置：


    model = Word2Vec(sentences, size=128, window=5, min_count=5, workers=4)

即只取最小出现过五次以上的词进行词向量转换

故将词向量模型改为min_count=1，出来的结果：

![此处输入图片的描述][6]

仍无区别

则可能是word2vec方法自身的缺陷。

在网上找到了相应的解释：

用word2vec将句子中的词向量进行简单相加作为句向量，这个方法确实有效，但只对15个字以内的短句子有效，这种方案常在搜索时做query比对。如果简单向量相加，丢掉了很多词与词相关意思，句子与句子的模式、结构等造成负面影响，无法更精细的表达句子与句子之间的关系。


## 下阶段目标：

找新的语料数据，进行扫描测试。

  
[1]: https://s14.postimg.cc/w3bkgjf81/20180425160912.png
  
[2]: https://s14.postimg.cc/6kj83kle9/20180425161021.png
  
[3]: https://s14.postimg.cc/ubillp10x/20180425161121.png
  
[4]: https://s14.postimg.cc/oncauvwpd/20180425161401.png
  
[5]: https://s14.postimg.cc/691rqzkfl/20180425162656.png
  
[6]: https://s14.postimg.cc/vqtd27ee9/20180425193152.png