# 颈动脉二分叉周报-20180411

## done
### 图像配准
1. 原始图像做了高斯滤波，partial volumen做了二值化（0.5-1为1，其余为0）
2. 配准到同一个物理空间（reference_image），spacing保持isotropic，大约在0.5左右（resample操作，原始图像线性插值，pv邻近插值）
3. 选取一个样本作为fixed image，其他作为moving image，利用meansquare进行配准,保存每个样本对应的transform（resample操作）

### roi选择
1. 针对每个样本，对于给定的roi index，比如's': (11, 74, 194), 'f': (220, 346, 289)，先在原图像坐标上转为物理坐标
2. 再把物理坐标做对应图像经过的配准变换
3. 在配准图像坐标上转为index
4. 遍历所有样本，起点取最小值，终点取最大值，作为参考的roi范围
5. 起点终点可稍作浮动 low =(148,216,286)， up=(292,360,430)，使得Size为144

### 图像切割
1. 在配准图像（image & label）上把参考的roi范围内的切割下来
2. block cut：进一步切小，block_size：40，overlap：27，满足block_size+(block_size-overlap)*(N-1)=Size，转成numpy格式
### UNET训练
- 参数：深度三层，第一层conv大小为16，没有dropout， batch_size=4， epochs=100，optimizer=Adam(lr=initial_learning_rate)， loss=dice_coef_loss
- 结果：不好
- ![image](https://github.com/cirweecle/DataScience/blob/master/cta_segmentation_PXY/terriableImages/0410dice_simple_r.png)

## problems
- 配准方式多种多样，结果大不相同，有些配准后使得roi区域比在同一物理空间取时还要大，配准效果难以衡量
- 学习曲线非常差

## to do
- 对原图像不做任何处理，截取标注给定的roi范围，切成统一大小的block训练。
- 图像扩增后再跑一次UNET？只扩增那些正样本比较多的block？
- resnet？