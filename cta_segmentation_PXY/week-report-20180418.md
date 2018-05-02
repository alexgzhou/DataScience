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

sample name | 3pool_big_roi | 3pool_small_roi | 4pool_small_roi
---|---|---|---
challenge001 | 0.15273945181 | 0.590382651397 | 0.888845588569
challenge005 | 0.18025824305 | 0.65840281197 | 0.896515224681
challenge010 | 5.54839764192e-05 | 0.629559906692 | 0.855514293209
challenge102 | 6.73308339838e-05 | 0.629573394201 | 0.830611707726
challenge202 | 8.74420919515e-05 | 0.690274683303 | 0.285117964435
mean per image | 0.0666415903524 | 0.639638689513 | 0.751320955724
mean per block | 0.1407074010354368 | 0.6442137106714935 |0.859461308391731

### 半监督训练

1. 数据预处理：
- 概要：另一侧的标注数据flip，配准到物理空间，然后进一步做基于互信息的配准，然后把参考roi范围提取出来再切block
- 细节：参考roi范围由标注数据的bounding box经过预处理过程相应的transformation得到，重采样时原始图像做平滑后且归一化后再插值，label图像做线性插值后再二值化
- 最后数据格式： spacing=0.5~， roi参考大小为（140,140,220），block_size为（96,96,128）， overlap为（26,26,34），每个样本被切成27个block，训练样本有15个，测试样本有41个

2. 零均值化：
- 测试数据（无对应label）也同样及鞥过上述预处理流程，最后和训练数据合并求均值和方差，分别对测试、训练数据做 减去均值、除以方差的操作

3. 半监督学习：
- 概要：1）训练数据和标注数据作为预训练模型的输入；2)根据上一个训练模型预测测试集，取平均概率最大和最小的N个（训练集个数*percentage）测试样本和预测结果加入训练集，并在测试集中删除相应的样本；3）训练数据打乱随机分出验证集进行下一个训练模型，初始化并非之前训练好的权重；4）循环结束条件为测试样本不足或者超出循环轮数
- 细节：模型UNET，4次maxpooling，dropout_rate为0.2，初始层conv的filter个数为16，损失函数dice，batch_size为4,epochs为250
- 疑问：1）每次从测试集中选取样本的函数；2）循环中模型的初始化
- 改进方向：1）第一次预训练可以比其他次久一点；2）原始训练数据的扩增

