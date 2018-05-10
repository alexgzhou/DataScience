# week-report-20180509

标签（空格分隔）： 未分类

---

#本周工作:特征提取&多模态深度学习算法
面部特征:
60s-->1500帧
*68点的坐标 * 40 trails * 32 participates

> End-to-End Multimodal Emotion Recognition Using Deep Neural Networks

dataset：RECOLA
视频部分：用裁切不正的被试者面部视频的像素强度（pixel intensities）取代传统的尺度不变特征转换(SIFT) 和方向梯度直方图 (HOG)
**ResNet-50模型**
https://github.com/LindsayXX/pics/blob/master/050901.jpg
7×7 convolutional layer with 64 feature maps → max pooling layer of size 3×3 → 4 Bottleneck Architectures → shortcut connection/ an average pooling layer

语音网络提取1280维特征，视觉网络提取2048维特征，连接形成3328维特征向量，馈送到每层256个单元的2层LSTM。在基于Glorot的初始化之后初始化LSTM层的权重，并利用单峰模型的权重初始化视觉和语音网络。最后，整个网络进行端对端训练。

> Emotion Recognition Using Multimodal Deep Learning

dataset：SEED&DEAP
**Bimodal Deep AutoEncoder (BDAE) 模型**
（Restricted Boltzmann Machine -- has a visible layer and a hidden layer)
https://github.com/LindsayXX/pics/blob/master/050902.jpg
Encoding & Decoding
hEEG,hEye: hidden layers  & W: weight matrices
finally use unsupervised back-propagation algorithm to fine-tune the weights and bias

DEAP：将同一时间段（一秒）的不同频道数据组合以形成BDAE网络的输入信号

> 迁移学习？

用额外数据集（FER dataset，TFD等）训练神经网络





