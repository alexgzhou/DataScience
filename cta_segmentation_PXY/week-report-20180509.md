# 颈动脉二分叉周报-20180509
## 目前计划
- 实验一：flip后配准，取存在overlap的patches作为UNET训练数据（15个样本）
- 实验二：flip后配准，取uneven spacing的patches作为UNET训练数据
- 实验三：数据扩增以及第二个挑战者的测试数据作为UNET训练数据

## 进度
实验一和实验二同时进行，实验三已经拿到挑战者的测试数据
- 实验一和实验二的patches大小为（48,96,112）
- 实验二中核心patches大小为（36,84,88），x\y方向距离(2, 2, 3, 3, 4, 5)，z方向距离(2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8)取点，切割部分已经写好，从patches到image的部分还待调试

## 难点
- 无论是实验一还是实验二，validation取的是challenge202和challenge201，但是训练不下去，基本不超过10个epoch，val_dice_coef就停滞在某个数值（0.1134或0.3345），但是训练集上loss仍在继续下降，学习曲线比如下图
![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/imagesInTime/5.09/prelu.png)

## 计划
1. training_set和validation_set取一样的数据集，排除代码有误的情况
2. patches中以label的正样本数（pixel_wise）——原话是pathces的dice排序，只训练正样本数较多的patches。
3. context information vs sample numbers, 进一步提高patches的大小