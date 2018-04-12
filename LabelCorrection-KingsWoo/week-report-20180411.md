# 周报20180408

## 论文结构
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
1. datasets

![数据集](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/dataset%20characteristic.png)

2. evaluation sheets

![评估结果1](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/Evaluation%20sheet1.png)

![评估结果2](https://github.com/KingsWoo/DataScience/blob/master/LabelCorrection-KingsWoo/source/pic/Evaluation%20sheet2.png)

## 工作内容
---
* 完成了基于python的DBR,2BR,RDBR的算法实现，并获取了不同算法的预测结果
* 对不同算法进行了对比和记录
* 修复了单标签SVM分类训练集必须有2或2类以上标签，当标签全为0的时候会报错的问题
* 修复了评估指标中当预测值和金标准完全吻合时macroF1不为1的问题
* 基本完成论文1~4节的文字工作，1~6节的公式、数据、图表工作

## 下周计划
---
* 完成论文初稿