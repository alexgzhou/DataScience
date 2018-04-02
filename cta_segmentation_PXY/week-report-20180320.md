# 颈动脉分叉周报-20180320

## 前言

### resample造成的误差(修正)

* 目的：好奇采样造成的误差，于是把标注图像做了一次resample，然后再resample回去原来的spacings，利用dice_coef计算误差
* 实验数据：右侧5个样本，第一次的spacings为[0.2,1.6]，步长0.1，**resample之前cast到uint上去**
* 实验结果: 下图y轴为5个样本的平均dice_coef
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/resample_errors(cast_first).png)

### partial segmentation 到底是什么？
并非是之前以为的只有轮廓（VTK三维展示投影算法造成的误解），用sitk切片来看：pv是填充好的体积；直接看数组值，接近血管的地方是类似[0,0.125,0.925,1,1,1,1,1,1,1]这样的值。<br>
所以，之前利用pv作为label数据来跑提取ROI的UNET的学习曲线不佳的问题原因不明。

## 本周工作

### 提取ROI
* 1.第一个UNET网络的预测结果是每个像素值为1的概率，因此以0.5为阈值做threshold得到mask，然后计算这张mask的boundingbox，就可以得到roi区域的最小索引和最大索引(physical point)
* 2.在对应原始图像坐标中把physical point转化为index，考虑到误差原因，把4作为容忍误差加进去，然后做裁减，保存为roi.mhd
* 3.重复之前预处理过程：roi.mhd：intensity-normalization->resample(0.23,0.23,0.23)->padding or cropping(300,300,300)->block cutting(size=(24,24,24),overlap=(1,1,1)) ->零均值;<br>
    pv.mhd:cast(uint8)->padding or cropping (into size of roi)->resample(0.23,0.23,0.23)->padding or cropping(300,300,300)->block cutting(size=(24,24,24),overlap=(1,1,1))
* 4.Size、block_size和overlap的关系必须满足  block_size+(block_size-overlap)\*(N-1)=Size

### 第二个UNET训练结果
* 1.采取原来的UNET网络结构（batch-size=10, epochs=50)
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/simple_right_loss_2nd.png)
* 2.初始层filter为16的三层UNET，加了batch_normalization和dropout(0.2)(batch-size=16,epochs=200)
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/simple_right_loss_2nd_dropout.png)

                      
### 预测值拼回去
* 1、取拼成图像的block数目（N\*N\*N）
* 2、把column全部拼好
* 3、把wall全部拼好
* 4、把整张图拼好（overlap部分均取平均值）

## 下周计划
* 1、block size可取大一点，囊括多一点context information
* 2、overlap可以取大一点，允许的话进行data augmentation
* 3、跑validation loss
* 4、（以后再说）对于pv中过度值的特殊处理（视为概率）