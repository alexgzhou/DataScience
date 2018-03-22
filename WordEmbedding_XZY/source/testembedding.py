# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
# 如果已经保存过模型，则直接加载即可
# 前面训练并保存的代码都可以省略
model = Word2Vec.load("word_embedding")
# 使用模型
# 返回和一个词语最相关的多个词语以及对应的相关度
items = model.wv.most_similar(u'甲状腺')
for item in items:
    # 词的内容，词的相关度
    print (item[0], item[1])
# 返回两个词语之间的相关度
#model.similarity(u'甲状腺',  u'结节')