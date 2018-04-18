# FYL-mimiciii-周报
## mimiciii数据申请
* HIPAA学习隐私保护课程
* 同意数据使用协议，申请至少一星期回复
* CSV文件，PostreSQL,MySQL，MonetDB
## 阅读MIMIC-III, a freely accessible critical care database
### 数据内容
* 生命体征
* 药物治疗
* 实验室测量结果
* 由护理人员绘制的观察和记录
* 体液平衡
* 程序代码
* 诊断代码
* 影像报告
* 住院时间
* 生存数据
### ICU数据集
![image](https://github.com/fyl0109/DataScience/blob/master/mimiciii_FYL/source/%E6%95%B0%E6%8D%AE%E8%BF%90%E4%BD%9C.jpg)
### 数据的细节信息
![image](https://github.com/fyl0109/DataScience/blob/master/mimiciii_FYL/source/%E7%97%85%E4%BA%BA%E5%88%86%E7%B1%BB.jpg)
### 疾病的分类，根据ICD-9
![image](https://github.com/fyl0109/DataScience/blob/master/mimiciii_FYL/source/%E7%96%BE%E7%97%85%E5%88%86%E7%B1%BB.jpg)
### 数据
* 存在26个table中
* 作为未加工的医院数据
* 特定的ID 特定的病人、入院、入ICU
* 数据来自两个不同的系统 CareVue和MetaVision，未能merge的有标识
### 应用方向
* 患者结局预测
* 血压监测技术的临床意义研究
* 非结构化病人笔记的语义分析

## 下周计划
* 查找对数据的处理方法