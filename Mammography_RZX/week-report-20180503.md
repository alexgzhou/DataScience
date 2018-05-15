# DM周报
## 本周工作
- 实现ddsm-ljpeg图像转换到png，并且利用overlay文件切割出了224x224的病灶png图像
- 值得提到的一点是，用了作者所说的github上的一个ljpeg转jpg的项目，但是部分图像转换的时候会有报错
“ Command './jpegdir/jpeg -d -s /data/DDSM/cases/benigns/benign_01/case3093/B_3093_1.LEFT_MLO.LJPEG' returned non-zero exit status 6”
在找解决方法，不好解决的话，打算直接放弃这些不能转换的
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180503/C_0002_1.LEFT_CC.png?raw=true)
![image](https://github.com/zhuoxin10/DataScience/blob/master/Mammography_RZX/source/images/20180503/C_0002_1.LEFT_CC.patch.png?raw=true)

## 下一步计划
- 复现ddsm以及病灶数据库的训练，看看效果
