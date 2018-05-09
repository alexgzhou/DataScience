# DM周报
## 本周问题
- 在用DDSM病灶数据库训练过程中，遇到如下图ValueError，不知道这个shape哪里出现的，看看源代码努力解决中
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180509/error.PNG?raw=true)
- 发现之前转换DDSM数据图像的时候，因为直接跳过了“灰度值映射到光密度”进行归一化的操作，然后不同图像之间有灰度差异，有的很暗？
- 良性图像
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180509/1.PNG?raw=true)
- 癌症图像
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180509/2.PNG?raw=true)
- DDSM网站示例图像
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180509/3.PNG?raw=true)

## 下一步计划
- 还是打算先用现在处理的图像训练起来，如果结果不好，再看看要不要做“灰度值映射光密度”的操作或者什么别的
- 打算用DDSM的数据验证一下我之前训练出来的网络效果如何
- 46服务器出了点问题，打算找个师兄帮我修一下QAQ
