# 颈动脉二分叉周报-20180418
## done
### 直接以spacing不一致的图像作为训练数据（右侧数据）
- 对于partial volume，经过二值化（binaryThreshold：0.5)得到的label后，取label为1的bounding，这个区域在x,y轴上几乎是相应样本给定的roi范围的一半，在z轴上倒是基本一致

sample name |roi-size|bounding-start|bounding-end
:-:|:-:|:-:|:-:|:-:
challenge001 | 210, 273, 96 | 66, 72, 0 | 143, 191, 95 |
challenge005 | 191, 205, 97 | 66, 66, 0 | 124, 138, 96 |
challenge010 | 103, 133, 121 | 32, 38, 0 | 73, 97, 120  |
challenge102 | 144, 126, 121 | 35, 34, 0 | 102, 81, 120 |
challenge202 | 83, 100, 134 | 33, 33, 0 | 49, 50, 103  |

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
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/big_predict_x.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/big_predict_y.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/big_predict_z.png)
2. 取较小范围（140,140,140）——堪堪覆盖label bounding 范围
- block_size(120,120,60)  overlap(40,40,26)
- 图像前后对比

 ![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_x.JPG)

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_y.JPG)

 ![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/images/big_001_z.JPG)
 - 学习曲线

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/samll_noresample_r.png)

- 预测结果（以前后图像对比中slice示例）

![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/small_predict_x.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/small_predict_y.png)
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/small_predict_z.png)

3. 问题
- 初步可排除配准误差对学习曲线的影响
- 预测时图像边缘的预测值都会稍高一点，切块和不切块都一致，为什么？