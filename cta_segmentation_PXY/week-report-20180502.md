# 颈动脉二分叉周报-20180502

## 任务
- [x] - 衡量配准的效果 
- [ ] - 采取【-1,1】的初始化而非【0,1】，用challenge202作为验证集，加上翻转后的图像训练UNET，尝试调参
- [ ] - 利用GAN搭建半监督网络利用其余41个测试样本，并询问其他挑战者的分割结果
- [ ] - patch切割时采用uneven spacing

## 配准的效果
- 利用分割结果来衡量配准效果，比较配准前后分割结果的dice, jaccard, hausdorff_distance, mean_surface_distance,median_surface_distance, std_surface_distance, min_surface_distance 等参数
- 比较好的配准方法是采用互信息,参数：learningRate=1.0,numberOfIterations=100,convergenceMinimumValue=1e-6,convergenceWindowSize=10，numsofbin=50
- 结果如下：<br>
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/4.27/beforeRegister_table.png)<br>
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/4.27/afterRegister_table.png)
