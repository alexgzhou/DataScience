# week-report-0329

标签（空格分隔）： 未分类

---

## 本周工作 ##
---
计划复现

> Li, Xiang, et al. "Emotion recognition from multi-channel EEG data through Convolutional Recurrent Neural Network." IEEE International Conference on Bioinformatics and Biomedicine IEEE, 2017:352-359.


---
1. Anaconda与TensorFlow安装
（在安装Anaconda的时候要注意在环境变量那里把两个路径都勾选上，不然就会出现spyder等在其他环境下安装不上等错误T_T）

2. 找可参考的源码
https://github.com/Niter/EmotionRecognitionDNN
github上少有直接使用DEAP数据集对EEG信号进行深度学习的，相似度比较低。

3. 数据预处理

> Each participant file(s0x.dat) contains two arrays:
data: 40 x 40 x 8064	video/trial x channel x data
labels: 40 x 4 video/trial x label (valence, arousal, dominance, liking) 

- 用Matlab进行小波变换db=4，‘WholeCWT.m’
- 用Python计算功率密度谱，归一化和切分，得到‘SplittedFlattenedPSD.dat’
- 跑了一个LSTM-RNN的例程
- 学习如何使用Python3读取和处理数据
- 代码复写

## 问题和下周计划 ##
由于找到的代码多是用python2.7写的，但是windows系统下TensorFlow只能在python3以上环境中运行，所以很多代码都不能直接使用。numpy中的很多常用函数在数据类型上发生了很大的变化，所以为解决科学计算相关的问题浪费了很多时间。
1. 继续复写or  **接入实验室服务器（xshell）跑通程序**
2. 找面部表情视频预处理软件等，完成对面部特征的提取
3. 找代码继续学习其他深度学习算法的可复现流程，尝试套用以复现其他文献or模型。（optional）




