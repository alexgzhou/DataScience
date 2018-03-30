# 颈动脉分叉周报-20180329

## 数据扩充

* x,y,z方向以图像中心为轴顺时针或逆时针旋转小幅度
* x,y,z方向正方向或负方向平移小幅度
因此，数据扩充倍数为64倍（2的6次方）

## 标注中正负样本数量
 * 以右侧数据为例，ROI正样本占整体的1%到2%之间，如果是pv正样本，这个比例估计会更小

## validation loss（第一个UNET，左侧数据，validation_split =0.2，loss=dice_coef， early_stopping[patience =10]）
* 尝试跑k折交叉验证，但是对于深度学习，需要建立k个MODEL, memory不支持，已放弃
* 上图是没加dropout，下图是两个卷积层之间加上了dropout（0.2），蓝色为validation loss，黄色为training loss
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/1st_L_withoutDropOut.png)
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/val_loss_bn_1st_l.png)


## 问题

* validation loss无法下降
* 正负样本不均衡

## 下周计划

* registration：把图像配准到一个空间
* data augmentaion：主要采用intensity transformation，少用spatial transformation
* loss function: 可试用weighted-crossentropy提高正样本的权重

## 不成熟的个人小想法

* 解决数据不足的问题：采用半监督学习的方法，用标记数据先训练，然后把无标记数据扔进网络预测拿到标记，再把（无标记数据，预测标记）扔进之前网络从之前的权重开始训练

	- 采用无标记的test数据
	- 把左右颈动脉大致切成两大块，采用无标记的那一侧数据