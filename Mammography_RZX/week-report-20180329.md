# DM周报
## 解决的问题
（记录一下对源代码的更改）
1. 由于tensorflow版本不同（服务器上是1.11，DM用的是0.12.1）报错。尝试python虚拟环境，错误仍存在，直接把代码中tensorflow的api按照对应版本改了。
2. metadata映射到dicom文件时，filename没有成功映射。还不知道为什么，暂时把test.py代码中if，else都改成了if里面的映射语句。
## 存在问题&下一步计划
1. CUDA_ERROR_OUT_OF_MEMORY：和别的同学协商一下gpu的使用
2. 解决运行环境、兼容性问题
3. 尝试少部分数据，跑跑看

