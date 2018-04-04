# 颈动脉分叉周报-20180404

## registration

* 确定reference image
	- 取所有图像中的最大physical size
	- 根据x方向的wanted size(168)计算各向同性的spacing(1.6~)
	- 起点为（0,0,0），size可根据physical size和spacing计算得出

* 生成roi mask，把原始图像和roi mask配准到reference image的空间
	- 原始图像在采样之前经过了sigma为0.4的高斯模糊
	- transform保持了中心不变

* cropping
	- 中心切割（80，80，160）

* 图片示例 challenge001

1)高斯模糊后原图和补零后的partial volume，slice=270<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/smooth%2Bpad_pv%5B001_270%5D.png)<br>

1)高斯模糊后原图和补零后的roi mask，slice=270<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/smooth%2Bpad_roi%5B001_270%5D.png)<br>

2)registration后原图和partial volume，slice =100<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/registration%2Bresample_pv%5B001_100%5D.png)<br>

2)registration后原图和roi mask，slice =100<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/registration%2Bresample%5B001_100%5D.png)<br>

3)切割后原图和partial volume，slice=70<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/crop_pv(80%2C80%2C160)%5B001_70%5D.png)<br>

3)切割后原图和roi mask，slice=70<br>
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/crop(80%2C80%2C160)%5B001_70%5D.png)<br>


## intensity data augmentaion

* 放弃了median filter 和椒盐噪声，总共8 filters
* 下图challenge001，slice=100
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/intensity_aug_001.png)

## 第一个UNET结果（validation_split=0.2，右侧数据45samples，batch_size:2，dropout:0.2）

* loss:dice_coef_loss(-dice_coef)

```python
SMOOTH = 1.0
def dice_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection + SMOOTH) / (K.sum(y_true_f) + K.sum(y_pred_f) + SMOOTH)
```
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/val_loss_1st_r.png)

* loss:binary_cross_entropy, batch_size:2,dropout:0.2
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/binary_cross_1st_r.png)

* loss:weighted_corss_binary_crossentropy（pos_rate:0.9），效果非常不好，没放图

* loss:custom_dice_coef_loss(-custom_dice_coef)（图在跑，待补）

```python
SMOOTH = 1.0
def custom_dice_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    penalty = K.sum((y_true_f - 1) * y_pred_f)
    return (2. * intersection + +penalty +SMOOTH) / (K.sum(y_true_f) + K.sum(y_pred_f) + SMOOTH)
```

## 梳理整个流程
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/first_unet.JPG)
![](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/second_unet.JPG)



## 问题

* 虽然第一个UNET的dice_coef还行，但是预测的bounding非常不准确，基本没有起到缩小范围的作用
* 预测时网络输入需要进行零均值化吗？
* 第二个UNET的训练输入的bounding是以第一个UNET的预测结果还是以给定的roi范围？
