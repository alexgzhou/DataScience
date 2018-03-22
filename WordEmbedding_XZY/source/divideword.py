# -*- coding: utf-8 -*-
'''import jieba

medical_text = open('./tjms.txt').read()
medical_words = [x for x in jieba.cut(medical_text) if len(x) >= 2]
print (medical_words)
'''
import jieba
import codecs
with open('./tjms.txt', 'r') as f:
    for line in f:
        seg = [x for x in jieba.cut(medical_text) if len(x) >= 2]
        s= ' '.join(seg)
        m=list(s)
        with open('fc2.txt','wb+')as f:
            for word in m:
                f.write(word.encode('utf-8'))
                #print word