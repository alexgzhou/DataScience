# 颈动脉分叉周报-20180314
## 预处理流程
### 对于原始图像
	原始图像的size和spacing不相同
1、 归一化 normalization<br>
	原来处理是减去0除以4095，但考虑到不同设备的区别（最大值有些是4000，有些是4095），因此改成了 (x - min)/(max - min)<br>
2、 降采样 resample<br>
    spacings 为 1.6，这样最后尺寸为（128,128,128）时比较充分涵盖ROI，采用线性插值，像素类型为Float32<br>
3、 padding or cropping<br>
	基于中心做补零或者裁减操作，使图像输出尺寸为（128,128,128），该尺寸为能跑三层或四层UNET的较大尺寸<br>
4、 生成零均值的numpy数据集<br>
	数据集的dimension需为5，[None,dims1,dims2,dims3,channels]（tensorflow的数据格式为channel_last<br>

### 对于标注图像
	标准图像的坐标系和原始图像一致，只不过只取了部分区域<br>
1、 padding<br>
    标注图像只涵盖ROI，补零使其尺寸和对应的原始图像一致，同时返回ROI mask<br>
2、 降采样 resample<br>
	spacings 为1.6，采用邻近插值，像素类型为Uint8<br>
3、 padding or cropping<br>
	基于中心做补零或者裁减操作，使图像输出尺寸为（128,128,128）<br>
4、 生成零均值的numpy数据集<br>
	数据集的dimension需为5，[None,dims1,dims2,dims3,channels]（tensorflow的数据格式为channel_last）<br>

## resample造成的误差
	好奇采样造成的误差，于是把标注图像做了一次resample，然后再resample回去原来的spacings，利用dice_coef计算误差<br>
	实验数据：右侧5个样本，中间的spacings为[0.2,1.6]，步长0.1<br>
	实验结果:<br>
	