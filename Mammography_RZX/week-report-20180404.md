# DM周报
## 测试
比赛要求的测试输出如下图：
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180404/out.jpg?raw=true)
第一列包含受试者的ID，第二列包含乳房的偏侧（左侧或右侧）。第三列包含预测乳房在12个月内发生癌症的置信水平。置信水平必须取[0,1]中的值，其中0表示乳房不会发展癌症，1意味着乳房肯定会发展成癌症。

---

子挑战SC1要求只考虑钼钯检查图像信息，SC2则还可以考虑之前的临床信息（也就是只有SC2允许使用exams_metadata数据）
###### SC1部分结果
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180404/sc_1.JPG?raw=true)
###### SC2部分结果
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180404/sc_2.JPG?raw=true)
## 存在问题&下一步计划
1. 复现训练部分
2. 跑训练的代码时，还有报错，需要研究一下代码，进行修改。
