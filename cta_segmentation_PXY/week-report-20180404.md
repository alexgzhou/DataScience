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

## intensity data augmentaion

* 放弃了median filter 和椒盐噪声，总共8 filters

## 第一个UNET结果

* loss:dice_coef_loss, batch_size:2,dropout:0.2
* loss:binary_cross_entropy, batch_size:2,dropout:0.2
* loss:weighted_corss_binary_crossentropy（pos_rate:0.9）, batch_size,droput:0.2，效果非常不好



## 梳理整个流程