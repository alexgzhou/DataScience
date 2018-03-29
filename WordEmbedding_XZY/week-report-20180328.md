# 词嵌入周报20180328


## 计划
复现RoboTrumpDNN代码

## 本周工作



### 1. TensorFlow安装与环境配置

参考教程https://blog.csdn.net/u010858605/article/details/64128466

另外由于部分代码需要用到keras库，因此还要安装一下theano，过程较简单，不予赘述。


### 2. RoboTrumpDNN

神经网络较复杂，大致结构为：
Trump:input-timedistributeddense-BN-LSTM左-BN左-LSTM左（-LSTM右-BN右-LSTM右）LSTM-LSTM-BN-dropout-dense-ELU-dropout-dense-activation（softmax）-output

使用词嵌入向量
在运行代码的时候出现问题
原因：代码使用语句为keras0.x的版本，而安装版本为keras2.1.5
两个版本的区别：keras0.x和keras2.x相差太多（keras0.x和keras1.x就相差很多了），函数用法基本不同，且有部分layers如RoboTrumpDNN里使用的timedistributeddense层已被删除。

找到一个网页详细描述了2与1的差别https://blog.csdn.net/ch1209498273/article/details/78287145
如要修改代码时可以参考（不过还需要找到keras0版本与keras1的区别，他们实在差太多了）

解决方法:改写代码或找新的代码



因为希望借鉴学习文本生成的过程，找了一些其他的文本生成代码，并尝试运行：

### 3. RNN_Text_Generation_Tensorflow

https://github.com/spiglerg/RNN_Text_Generation_Tensorflow

特点：英文文本处理 两层lstm 输入为one-hot向量 基于TensorFlow

耗费时间过长，未能运行完成

### 4.lstm_text_generation_chinese

https://github.com/crownpku/lstm_text_generation_chinese

特点：中文文本处理 两层lstm 输入为one-hot向量 基于旧版keras

需要修改代码才可运行

### 5.Text_Generation
https://github.com/alex-mau/Text_Generation

特点：英文文本处理 两层lstm（与4结构相似） 输入词嵌入向量 基于新版keras

尝试用体检报告数据训练该神经网络模型，出来的结果并不好：

![此处输入图片的描述][1]

可能是代码对英文文本和中文文本的处理并不一样，还需要深入理解代码进行修正

对神经网络模型的训练过程有了大致的了解，可以尝试将结合各程序进行代码的修改实现中文文本生成


##存在问题

1.对神经网络的训练过程不够熟练，对代码理解不够深入，在进行调试与代码修改上存在困难，应多看多学多问。

2.找到的一些代码keras版本不适用，程序跑不出

3.cpu跑代码还是太慢了，想改用gpu跑

##下周目标 

继续探索，找到一个最合适的方案，并对代码进行改进。

转换方向：通过体检结果的异常值关键词对其进行扩写，看看有什么方法或是源码-文献及github
  


  
[1]: https://s17.postimg.org/ws7zqqvvj/image.png