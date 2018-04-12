# DM周报
## 本周工作
- 以在DDSM训练好的网络DDSM_net作为起点，不使用metadata，对500张dream challenge的图像进行训练，结果如下（对应SC_1）：
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180411/WechatIMG122.png?raw=true)

---
- 对应SC_2的话一开始以为应该用DDSM_net作起点，也使用metadata，但会报错，如下，问题无法解决：
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180411/WechatIMG120.jpeg?raw=true)
- 然后试了不指定起点，结果不出所料的不好。
- 再看了一遍作者的方法，发现作者在针对SC_2的训练时起点选取了SC_1的最佳结果并进行了decapitate it (cut out 3 last layers) and continue training to recover the last layers，但是还是...
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180411/WechatIMG123.jpeg?raw=true)

## 下一步计划
1. 没有复现得到DDSM_net的过程？
2. batch_size默认是10，但是OOM了，跑的时候取得是2，有影响吗？
3. 在过程中发现很多理论知识、概念的缺失，后面会继续学习
