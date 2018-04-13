# 周报20180411

## 论文结构 (LabCor)
---
1. introduction
2. Relative Work
	1. multi-label learning
	2. Binary Relevance with Stacking Structure
	3. Dependent Binary Relevance
	4. Pruned stacking approaches	
3. The proposed approach
	1. improve function
	2. two level classifiers
	3. Label Correction
	4. Iterated Label Correction	
4. experiments 
	1. data sets <sub>**只有图**</sub>
	2. Evaluation criteria
	3. Comparison algorithms
5. results <sub>**只有图**</sub>
	1. Comparison with 2BR series methods
	2. Apply label correction to more multi-label algorithms
	3. Label strength
	4. visualization of label correction
6. Conclusion <sub>**暂缺**</sub>

## 结果展示
---
1. **Datasets**

![数据集](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/dataset%20characteristic.png)

2. **Evaluation Sheets**

	在表格中，各项符号的意义是：
	* **加粗字体** 表示该算法该项在全部算法中**最优**
	* &uarr; 单上箭头表示该算法该项表现显著**优**于*LabCor*且 *0.05>P>0.005*
	* &uArr; 双上箭头表示该算法该项表现显著**优**于*LabCor*且 *P<0.005*
	* &darr; 单下箭头表示该算法该项表现显著**劣**于*LabCor*且 *0.05>P>0.005*
	* &dArr; 双下箭头表示该算法该项表现显著**劣**于*LabCor*且 *P<0.005*

![评估结果1](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/Evaluation%20sheet1.png)

![评估结果2](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/Evaluation%20sheet2.png)

## 工作内容
---
* 通过采用 svm.linearSVC 代替 svm.SVC 的方案避免了 SVC 在部分训练集下全部分类为0的问题（原因未知）
* 修复了 linearSVC 分类时训练集必须有2或2类以上标签，当标签全为0的时候会报错的问题（与之前的方案相同）
* 修复了评估指标中当预测值和金标准完全吻合时 macroF1 != 1 的问题
* 完成了基于 python 的 *DBR, 2BR, RDBR* 的算法实现，并获取了不同算法的预测结果
* 对不同算法的算法表现进行了记录和对比
* 基本完成论文1\~4节的文字工作，1\~6节的公式、数据、图表工作
* 尝试用 R 完成 *PruDent* 算法，但是 *utiml* 包中该算法的实现似乎对正类数据量有要求，较少的数据量会导致内部的某一部<sub>（剪枝选择？）</sub>出现问题，因此最后没有用该程序。但该程序同时解决了针对SVM的单类标签报错问题，具有一定的参考价值，因此在repo内部继续保留。
* 用 R 语言下 *utiml* 包内的 *BR* 和 python 下 *skmultilearn* 内的 *BR* 实现进行对比，两者结果相差较大，可能R中存在内部优化。
* 用 R 语言可以直接读写 *.arff* 文件，以后可以加以利用（*.arff* 基于稀疏存储，所需空间比 *.csv* 小很多）

## 下周计划
---
* 完成论文初稿