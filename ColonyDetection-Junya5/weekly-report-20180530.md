## 无菌检测

### 图像采集
- 前两周进行了六种菌液的采集（生孢梭菌、铜绿假单胞菌、金黄色葡萄球菌、黑曲菌、枯草杆菌、白色念珠菌）。
- 每种菌采集周期约2-3天（菌液约1-2天长出菌落，之后形态变化不大），每种菌都有10瓶菌液样本。
- 采集流程：菌液制成后约20小时（未见菌落）、44小时（有可见菌落）拍摄0°、90°、180°、270°四个角度各10张图像，并以其中一瓶样本连续采集图像。
- 图像大小：1916*1370
- 各种菌液前后变化图：

1. 生孢梭菌
    - 菌液颜色较明亮，顶部有氧化层，氧化层的减小说明菌落在生长
    - 菌落形状有大有小，较明显的颗粒状，大部分呈悬浮状，底部会有部分沉积
    
![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/生孢梭菌.png)

2. 铜绿假单胞菌
    - 菌液颜色较明亮，顶部有氧化层
    - 菌落生长在顶部，棉花状，增加液体浑浊度

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/铜绿假单胞菌.png)

3. 金黄色葡萄球菌
	- 菌液颜色较明亮，顶部有氧化层
	- 菌落大部分呈密集颗粒状，小部分聚集较大，悬浮，液体表面聚集明显
	
![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/金黄色葡萄球菌.png)

4. 黑曲菌
	- 菌液颜色较深，无氧化分层
	- 菌落大部分沉积在底部，棉花状

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/黑曲菌.png)

5. 枯草杆菌
	- 菌液颜色较深，无氧化分层
	- 菌落无明显形状，会增加菌液浊度，部分样本中悬浮少数黑点

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/枯草杆菌.png)

6. 白色念珠菌
	- 菌液颜色较深，无氧化分层
	- 菌落生长不明显，菌液浊度也无明显变化，部分样本可见底部形态略微有变化

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/白色念珠菌.png)

- 图像数量：6（菌液种类）x4（四个角度）x10（单次拍摄数量，图像几乎完全一样）x10（菌液样本数）x2（次）（=4800张）+6xSequential（间隔相同时间连续拍摄，持续约2天）

###计划进行

- 检测目标
	- 分类：六种菌分类
	- 浊度识别：自动识别微生物生长的浊度变化，并进行结果判定
	- 可见异物识别：自动识别1mm或更小的徐庄、颗粒状、丝状等可见异物（菌落），并进行结果判定
	- 生长前期预测：结合浊度识别和可见异物识别

- 图像预处理：
	- 对图像进行固定尺寸固定位置裁剪，裁剪出包含菌液瓶的主体部分
	- 部分菌液菌落生长会沉积在底部的图像或者亮度较暗的图像，预处理调整图像点高度或者部分区域的亮度
	- 对可见菌落进行分割标注


- 出现的问题：
	- 菌落生长变化时间较短，长到肉眼可见之后生长变化不明显
	- 有几种菌的生长会布满整个样本（如金黄色葡萄球菌），远近深浅叠加，有些菌落生长在底部且无明显变化（如白色念珠菌），做分割的标注会比较困难
	- 菌落深浅不一，有些会跟液体浊度混淆




## chestCamera

###  freeze the weight

- 方法
```
for layer in model.layers[:100]:
    layer.trainable = False
```
- 结果会比不加这一项的差，查阅的很多资料里这种用法并没有问题，也看到有人说ImageNet的模型不太适用于医学图像数据集，所以可能固定参数不变会比微调参数的性能差。

### ground truth vs. pretiction

- 训练中有把预测结果与标注结果不一致的图像保存下来，查看之前某一次不采用固定参数训练的错分结果：
	- 实际为0，预测为1的，共15张

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/0vs1.png)

	- 实际为1，预测为0的，共23张

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/1vs0.png)

	- 感觉这些错分的图像肉眼可以看辨别正确
	- confusion matrix with normalization

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/data2confusionmwithnormalization2.png)


### cross validation

- 正在修改调试图像分类任务的k折交叉验证模型
- 使用keras模型和sklearn库
```
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import StratifiedKFold
```

