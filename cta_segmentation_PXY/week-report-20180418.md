# 颈动脉二分叉周报-20180418
## done
### 直接以spacing不一致的图像作为训练数据（右侧数据）
- 对于partial volume，经过二值化（binaryThreshold：0.5)得到的label后，取label为1的bounding，这个区域在x,y轴上几乎是相应样本给定的roi范围的一半，在z轴上倒是基本一致

sample name |roi-size|bounding-start|bounding-end
---|---|---|---
challenge001 | 210, 273, 96 | 66, 72, 0 | 143, 191, 95 
challenge005 | 191, 205, 97 | 66, 66, 0 | 124, 138, 96 
challenge010 | 103, 133, 121 | 32, 38, 0 | 73, 97, 120  
challenge102 | 144, 126, 121 | 35, 34, 0 | 102, 81, 120 
challenge202 | 83, 100, 134 | 33, 33, 0 | 49, 50, 103  

- 预处理只是一些切割补零操作以及归一化
- unet网络深度为三层，loss为dice_coef_loss，初始输入层filter个数为16，batch_size为4，epochs为150，earlystopping的patience为10，validation_split为0.2

1. 取较大范围(280,280,140)——覆盖了所有样本 roi 范围
- block_size(120,120,60)  overlap(40,40,26)
- 图像前后对比

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_x.JPG)

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_y.JPG)

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_z.JPG)
- 学习曲线

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/big_noresample_r.png)

- 预测结果（以前后图像对比中slice示例）

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/x_predict_3pool_big.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/y_predict_3pool_bigl.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/z_predict_3pool_big.png)



2. 取较小范围（140,140,140）——堪堪覆盖label bounding 范围
- block_size(120,120,60)  overlap(40,40,26)
- 图像前后对比

 ![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_x.JPG)

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_y.JPG)

 ![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_z.JPG)
 - 学习曲线

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/samll_noresample_r.png)

- 预测结果（以前后图像对比中slice示例）

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/x_predict_3pool_small.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/y_predict_3pool_small.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/z_predict_3pool_small.png)

3. 训练数据与2中一致，但是网络结构深度为4，即做了4次max pooling，并且第一层conv为32 filters
- 学习曲线

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/dice_big_nodrop_4pool_r.png)

- 预测结果（2中以前后图像对比中slice示例）

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/x_predict.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/y_predict.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/z_predict.png)

4. dice

sample name | 3pool_big_roi |3pool_small_roi |4pool_small_roi
---|---|---|---
challenge001 | 0.15273945181 | 0.590382651397 | 0.888845588569
challenge005 | 0.18025824305 | 0.65840281197 | 0.896515224681
challenge010 | 5.54839764192e-05 | 0.629559906692 | 0.855514293209
challenge102 | 6.73308339838e-05 | 0.629573394201 | 0.830611707726
challenge202 | 8.74420919515e-05 | 0.690274683303 | 0.285117964435
mean per image | 0.0666415903524 | 0.639638689513 | 0.751320955724
mean per block | 0.1407074010354368 | 0.6442137106714935 |0.859461308391731
3. 问题
- 初步可排除配准误差对学习曲线的影响
- 预测时图像边缘的预测值都会稍高一点，切块和不切块都一致，为什么？