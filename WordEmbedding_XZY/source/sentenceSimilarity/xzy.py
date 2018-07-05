#encoding=utf-8

from zhcnSegment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence

if __name__ == '__main__':
    # 读入训练集
    file_obj = FileObj(r"testSet/tjmsnew.txt")
    train_sentences = file_obj.read_lines()

    file_obj = FileObj(r"testSet/zhenduanxx-utf.txt")
    test1_sentences = file_obj.read_lines()
    #test1_sentences = "子宫 肌瘤"

    # 分词工具，基于jieba分词，主要是去除停用词
    seg = Seg()

    # 训练模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    #ss.TfidfModel()         # tfidf模型
    #ss.LsiModel()         # lsi模型
    ss.LdaModel()         # lda模型
    #ss.W2Vmodel()

    for j in range(0,len(test1_sentences)):
        sentence = ss.similarity(test1_sentences[j],j)
'''    # 测试集1
    right_count = 0
    file = open("result6.txt", "a")
    for j in range(0,len(test1_sentences)):
        sentence = ss.similarity(test1_sentences[j])
        file.write(str(sentence.origin_sentence)+str(sentence.score)+"\n")
    file.flush()
    file.close()'''
'''            if i != sentence.id:
                print (str(i) + " wrong! score: " + str(sentence.score))
            else:
                right_count += 1
                print (str(i) + " right! score: " + str(sentence.score))'''    
    
