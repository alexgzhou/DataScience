# 文献情况

1. [A Deep Learning Method for Microaneurysm Detection in Fundus Images](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/Paper/ADeepLearningMethodforMicroaneurysmDetection.pdf)
> Shan J, Li L. A Deep Learning Method for Microaneurysm Detection in Fundus Images[C]// IEEE First International Conference on Connected Health: Applications, Systems and Engineering Technologies. IEEE, 2016:357-358.

* 目标：MA检测
* 方法：Green channel image，25*25 image patch，Stacked Sparse Autoencoder（SSAE）+ Softmax Classifier + Finetuning + 10-fold cross-validation，
* 数据：DIARETED
* 结果：F-measure 91.3%，AUC 96.2% 
* 结构图

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/1-architecture.png)


2. [Improved Microaneurysm Detection using Deep Neural Networks](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/Paper/ImprovedMicroaneurysmDetectionUsingDeepNeural.pdf)
> Haloi M. Improved Microaneurysm Detection using Deep Neural Networks[J]. Computer Science, 2015.

* 目标：MA检测
* 方法：RGBchannels，129*129 image patch，CNN（+dropout+**maxout**）
* 数据：DIARETED
* 网络结构

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/2-method-overview.png)

* 部分评价指标

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/2-comparison.png)


## 小结

* 从文献看，血管微动脉瘤作为糖尿病视网膜病变的前兆，一般做检测（有或无）的比较多，且文中未提及公知数据库是否有正负样本像素数及不均衡问题，但从文献2的网络输出结果看（输出每一个像素点是否为MA的概率），可以转化为分割任务。
* 针对现有数据集存在的难点还需要调研更多的文献方法

---

# 图像标注工具

* 考虑到后期需要制作菌落图像数据集，就先查了几种图像数据标注工具，常用的工具有：

1. [Labelme](https://github.com/wkentaro/labelme)适用于图像分割任务数据集制作
* 功能：多边形填充标注
![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/labelme-1.png)
* 保存为.json格式文件


> labelme_json_to_dataset <文件名>.json

* 即可得到一个文件夹，有四个文件，*.png, info.yaml , label.png, label_viz.png

2. [LabelImg](https://github.com/tzutalin/labelImg)适用于图像检测任务的数据集制作
* 功能：bondingbox标注
![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/labelImg-1.png)
