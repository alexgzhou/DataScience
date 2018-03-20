# 颈动脉分叉周报-20180314
## 前言（预处理流程）
### 对于原始图像
	原始图像的size和spacing不相同
1、 归一化 normalization<br>
	原来处理是减去0除以4095，但考虑到不同设备的区别（最大值有些是4000，有些是4095），因此改成了 (x - min)/(max - min)<br>
2、 降采样 resample<br>
    spacings 为 1.6，这样最后尺寸为（128,128,128）时比较充分涵盖ROI，采用线性插值，像素类型为Float32<br>
3、 padding or cropping<br>
	基于中心做补零或者裁减操作，使图像输出尺寸为（128,128,128），该尺寸能跑三层或四层UNET的较大尺寸<br>
4、 生成零均值的numpy数据集<br>
	数据集的dimension需为5，[None,dims1,dims2,dims3,channels]（tensorflow的数据格式为channel_last)<br>

### 对于标注图像
	标准图像的坐标系和原始图像一致，只不过只取了部分区域
1、 padding<br>
    标注图像只涵盖ROI，补零使其尺寸和对应的原始图像一致，同时返回ROI mask<br>
2、 降采样 resample<br>
	spacings 为1.6，采用邻近插值，像素类型为Uint8<br>
3、 padding or cropping<br>
	基于中心做补零或者裁减操作，使图像输出尺寸为（128,128,128）<br>


## 本周工作
### resample造成的误差

* 目的：好奇采样造成的误差，于是把标注图像做了一次resample，然后再resample回去原来的spacings，利用dice_coef计算误差
* 实验数据：右侧5个样本，第一次的spacings为[0.2,1.6]，步长0.1
* 实验结果: 下图y轴为5个样本的平均dice_coef，说明即使深度学习的准确率为100%，最后准确率也只有0.91左右？
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/resample_errors.png)

### 提取ROI
#### 网络结构
1、原始结构加上（128,128,128）的输入尺寸会出现内存不足的问题，考虑到提取ROI的准确率不用太高，于是简化了经典的Unet结构，如下图：<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/simpleUNET.JPG)
图中Unet深度只有3层，但其实深度为4层的时候内存也可以支持（最开始接一层16 filters），但是学习曲线非常差，如下图：<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/bad_curve.png)<br>
猜测是网络结构太深，传播不了？<br>

2、训练数据y_train(epochs=800, batch_size=2, optimizer:Adam(lr=0.00001),loss=dice_coef_loss)<br>
1）roi，相当于一个立方体mask(上图是右侧数据,最佳是0.95左右；下图是左侧数据，最佳是0.98左右)<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/simple_right_loss.png)<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/simple_Left_loss.png)<br>

2）pv，颈动脉血管的轮廓<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/simple_right_loss(pv2roi).png)<br>
原因分析：正负样本不均衡？那在high resolution时会不会也出现这种情况？<br>
3）pv_filled，第二步的填充，把轮廓补成立体（待做）<br>

3、处理ROI预测数据<br>
ROI预测数据是概率，可以画heatmap（待做）<br>
计算boundingbox，在未处理过的原始图像上进行合适的resample，生成下一个神经网络的训练数据<br>
boundingbox:index->physicalPoint->index

## 问题

* 怎么把轮廓填成立体？
* 深度增加时如何解决学习曲线很差的问题？

## 下一步要做的事情

* 跑下一个网络结构
* 数据扩充（对原始和标注做同样的操作？flip?translate?rotate?直方图均衡化）
* 跑左侧数据
* maybe 把图像中左右颈动脉分成两张图像，做半监督学习（不了解，不知道可行性，想得太遥远了）

