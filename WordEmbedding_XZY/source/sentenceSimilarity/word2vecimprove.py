# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:58:37 2018

@author: thinkPad
"""

from sentence_preprocess import sentence_preprocess
import numpy as np
import operator
from gensim import models
from fileObject import FileObj


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    if v1 is not None and v2 is not None:
        v1_u = unit_vector(v1)
        v2_u = unit_vector(v2)
        return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
        #return np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)


def average_vectors(vectors):
    return sum(vectors) / len(vectors)


def average_sentence_vector(sentence, model):
    words = []
    for word in sentence:
        try:
                c = model[word]
        except KeyError:
                c = 0
        words.append(c)    
    return average_vectors(words)
'''def average_sentence_vector(sentence, model):
    return average_vectors([model[word] for word in sentence])'''




if __name__ == '__main__':
    

    model = models.Word2Vec.load('fenci3min_count1')
    


    train_file = open('6resulthouban.txt', encoding='utf-8',errors='ignore')
    train_text=train_file.readlines()
    test_file = open('zhenduanxxhouban.txt', encoding='utf-8',errors='ignore')
    file = open("zhenduanxxresult.txt", "a",encoding='utf-8')
    similarities = {}
    a = 1
    b = 7
    for line1 in test_file:
        line1 = line1.replace("\n", "")
        line1 = line1.replace("\t", "")
        query = sentence_preprocess(line1)
        mem = (0,0)
        train_file.readline()
        for line in train_text[a:b]:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            sentence_vec1 = average_sentence_vector(sentence_preprocess(line), model)
            sentence_vec2 = average_sentence_vector(query, model)
            similarities[line] = angle_between(sentence_vec1, sentence_vec2)
            if mem[0] <= similarities[line]:
                mem = (similarities[line],line)
        file.write(str(line1)+"\n")
        file.write(str(mem[1]) + "\n")
        a = a + 7
        b = b + 7
    file.flush()
    file.close()
'''    def sentence2vec(self,sentence):
        sentence = Sentence(sentence,self.seg)
        vec_bow = self.dictionary.doc2bow(sentence.get_cuted_sentence())#把描述转为词包
        return self.model[vec_bow]

    # 求最相似的句子
    def similarity(self,sentence,j):
        sentence_vec = self.sentence2vec(sentence)#直接使用上面得出的tf-idf 模型即可得出描述的tf-idf 值

        sims = self.index[sentence_vec]#利用索引计算每一条评论和描述之间的相似度
        simlist = sorted(enumerate(sims), key=lambda item: item[1],reverse=True)
        file = open("wujianyiresult.txt", "a")
        file.write(str(j)+"\n")
        for x in range(6):
            index = simlist[x][0]
            score = simlist[x][1]
            sentence = self.sentences[index]
            sentence.set_score(score)
            file.write(str(sentence.origin_sentence)+str(sentence.score)+"\n") 
        file.flush()
        file.close()'''