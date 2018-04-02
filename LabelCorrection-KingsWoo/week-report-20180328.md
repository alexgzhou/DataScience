# 周报20180328

* 20180326 修复由于scikit.svm.SVC函数在分类数为1（即全为0）会报错的bug
* 20180326 修复values文件所记录结果与应当记录结果差1列的bug
* 20180326 对log的记录方式进行了一点优化，更清晰了
---
* 20180327 增加selector规范代码
* 20180327 introduction瞎扯了两段
---
* 20180328 从一篇文章找到了一系列文章 
  - BR2算法：
    即最初的stacking BR算法。可追溯至 *D.H. Wolpert, Stacked generalization, Neural Networks 5 (1992) 214–259.*
  - DBR算法：Dependent binary relevance models for multi-label classification 2014
	* 给出了Pipeline
	* 使用的第二层BR输入参数为(x,y_estimate), 感觉和STA没有明显的区别
  - 获取Rule：Learning rules for multi-label classification: a stacking and a separate-and-conquer approach 2016
  - 通过剪枝挑选强相关的label
	* PruDent: A Pruned and Confident Stacking Approach for Multi-Label Classification 2015
	* Correlation-Based Pruning of Stacked Binary Relevance Models for Multi-Label Learning 2009

===
4.8 前论文中文初稿