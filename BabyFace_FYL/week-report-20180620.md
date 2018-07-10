# BabyFace_FYL_周报
### IPPG - （pre）processing steps
## ROI selection/tracking
* SURE（Automatic detection based upon speed-up robust features）  forehead/cheeks
* skin/noskin classification  速度更快，可以适应侧面
## color channel selection
* Green: pulse signal
* Red: Oxygen saturation
* RGB: (ICA,PCA)  BSS
## signal denoising
* 带通，自适应带通，移动平均，小波去噪
## physiological signal extraction 生理信号提取
* 启发式： 时频分析
* 基于学习的方法： 多特征融合支持向量回归 （更优）
* 心率 呼吸 血氧饱和度 等
## 下周计划
* 查具体实现的论文
* 在github上 看一些面部识别的代码