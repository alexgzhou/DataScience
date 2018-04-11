#encoding=utf-8

from zhcnSegment import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence

if __name__ == '__main__':
    # 读入训练集
    file_obj = FileObj(r"testSet/num-tjms.txt")
    train_sentences = file_obj.read_lines()

    test1_sentences=input("请输入关键词：")
    #test1_sentences = "T波 异常"

    # 分词工具，基于jieba分词，我自己加了一次封装，主要是去除停用词
    seg = Seg()

    # 训练模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    ss.TfidfModel()         # tfidf模型
    # ss.LsiModel()         # lsi模型
    # ss.LdaModel()         # lda模型

    # 测试集1
    right_count = 0
    sentence = ss.similarity(test1_sentences)
    print (sentence.origin_sentence)
    
