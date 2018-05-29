# DM周报
## 本周工作
### patch训练
0,1,2 label一类，3,4 label一类，据此画出ROC图，AUC最高约0.859  ![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/patch-auc.PNG?raw=true)  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/ROC-3000.png?raw=true)  

train loss  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/otal-loss.PNG?raw=true)  

train accuracy  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/train-acc.PNG?raw=true)  

validation loss这个很奇怪，在上升？？  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/valid-loss.PNG?raw=true)  

validation accuracy，最高约0.6756  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/acc.PNG?raw=true)  

### DDSM训练
针对DDSM的训练还是有点问题，结果不太好。  
AUC最好约0.68  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/ROC-2000.png?raw=true)  

validation accuracy  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/3-acc.PNG?raw=true)

validation loss  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/3-valid-loss.PNG?raw=true)

train loss  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/3-train-loss.PNG?raw=true)

train accuracy  
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180523/3-train-acc.PNG?raw=true)


## 下一步计划
1. 感觉问题还是针对DDSM数据预处理的不够理想
2. 作者有提过把patch网络插入到final model时可以“make the detector net overfit on patches“,拿overfit的patch网络作为训练起点试试看？？
