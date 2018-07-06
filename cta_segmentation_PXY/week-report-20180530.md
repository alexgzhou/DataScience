# 颈动脉二分叉周报-20180530

## 1.training set = validation set
- 目的：为了排除代码错误
- 网络结构：UNET，max pooling layers =4, first conv filters = 32, use bias = True, optimizer = Adam(lr = 0.00001), metrics = [dice_coef]
- 数据：(48,96,112) patches with overlap (17, 12, 48) cut from image region with size (110,180,240) after registration
- loss = -dice_coef<br>
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/5.15/overlap_lr0.0001_all_dice.png)

- loss = binary_crossentropy<br>
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/5.15/overlap_lr0.0001_entropy.png)<br>
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/5.15/bn_32filters_dice.jpg)

## 2.even spacing VS uneven spacing
- 前言：even spacing采用的数据格式和实验1中一样，所以操作比较简单也方便比较训练结果，但是采用同样网络结构，loss取binary_crossentropy的条件下，只改变了validation set 和 training set，结果并不好如下图<br>
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/5.15/bn_32filters_diff_val.jpg)

- whether augmentation helps?

## 3.larger patches to contain more context information


## 4.skip empty patches (those without positive label)
假如用-dice_coef作为loss function时必须跳过无正标签的patch，因为dice_coef在y_true, y_pred均为空时的值最大，和有正标签时完全正确预测的值一致，而数据集中empty patches的数量超过2/3


## 5.basics about Tang's test data

sample|x_start|x_end|y_start|y_end|z_start|z_end|origin_size_y
---|---|---|---|---|---|---|---|
challeng009|256|512|51|450|160|382|481
challeng100|256|512|51|450|228|445|561
challenge011|0|255|51|450|237|470|576
challenge012|256|512|51|450|243|442|546
challenge013|0|255|51|450|131|279|395
challenge014|0|255|51|450|193|387|491
challenge015|0|255|51|450|201|393|501
challenge016|0|255|51|450|164|335|419
challenge017|0|255|51|450|195|397|501
challenge018|0|255|51|450|133|339|457
challenge019|0|255|51|450|221|377|480
challenge020|240|512|51|450|228|401|508
challenge021|0|255|51|450|201|439|533
challenge022|0|255|51|450|195|398|536
challenge023|256|512|51|450|207|429|501
challenge024|256|512|51|450|166|420|533
challenge025|256|512|51|450|202|397|493
challenge026|0|255|51|450|185|410|532
challenge027|256|512|51|450|206|409|501
challenge028|256|512|51|450|179|388|514
challenge029|256|512|51|450|174|397|504
challenge030|256|512|51|450|183|415|497
challenge031|256|512|51|450|251|473|579
challenge032|0|255|51|450|160|383|475
challenge033|0|255|51|450|241|460|571
challenge034|0|255|51|450|209|421|530
challenge035|0|255|51|450|180|408|526
challenge103|255|512|51|450|220|450|744
challenge104|0|256|51|450|307|504|772
challenge105|255|512|51|450|181|430|718
challenge106|0|255|51|450|228|390|634
challenge107|256|512|51|450|194|396|637
challenge108|0|255|51|450|284|489|751
challenge109|200|400|51|450|193|458|710
challenge203|256|512|51|450|200|481|684
challenge204|0|256|51|450|410|568|658
challenge205|256|512|51|450|218|528|662
challenge206|256|512|51|450|252|448|789
challenge207|256|512|51|450|186|443|757
challenge208|0|255|51|450|264|554|827
challenge209|256|512|51|450|250|525|636

## problem：will metal artifacts reduction helps?
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/5.15/tipical_example_metal_artifacts.png)

## Tan's normalization
itk、cmake生成成功后，执行时遇到了内存不足的问题，现在在把c++程序转为python

## use Tang's results
由于数据集太大，无法一次性载入内存，目前已写好data generator等待执行