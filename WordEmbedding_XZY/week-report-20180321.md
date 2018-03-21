# 词嵌入周报20180321





## 本周工作-数据处理



本周的主要工作是进行数据的预处理，将体检数据（tjms）提取出来转成txt格式，并做词嵌入处理。



### 1. 连接数据库



用python方法连接，需要进行cx_Oracle的安装以及相应环境配置，具体方法参考http://blog.csdn.net/u013012406/article/details/59057416

由于版本问题走了很多弯路，一定要记住操作系统版本、python、instantclient、cx_oracle这4部分的位数（32或64位）必须一致！！！

数据库连接代码见visitdatabase.py



### 2. 导出数据



将数据导出为txt格式，方便进行词嵌入处理，需先将数据导出成csv，再另存为txt格式

找到了pandas库可以方便的将数据进行导出成csv格式

pandas库使用手册http://blog.csdn.net/u014281392/article/details/75331570

在访问数据库代码后加入下面两行即可，十分方便。

```python

df = pd.DataFrame(result)

df.to_csv("result1.csv")

```

中途出现编码报错：



    UnicodeEncodeError: 'gbk' codec can't encode character u'\xa0' in position

在前面加入一段

```python

import os  

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  

```

得以解决

数据导出代码见converttocsv.py



### 3. 分词


采用jieba库进行分词（关于结巴分词的使用方法：http://blog.csdn.net/wangpei1949/article/details/57413419）：

遇到报错：



    TypeError: write() argument must be str, not bytes+

网上搜索才发现原来是文件打开方式有问题，把之前的打开语句修改为用二进制方式打开就没有问题

把



    open('fc2.txt','w+')

改成


    open('fc2.txt','wb+')

即成功运行
分词结果：

![此处输入图片的描述][1]

分词代码见divideword.py

### 4. 词嵌入

用gensim库里的word2vec工具实现词向量空间的生成

生成与测试代码见wordembedding.py和testembedding.py



##下周目标
 
按之前的几个思路：Trump、问答系统、cmu等进行探索，深入阅读文献与代码，尝试复现部分代码。




  [1]: https://s17.postimg.org/8o1k4do7j/image.png
