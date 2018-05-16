# BabyFace_FYL_周报
## 调试程序，使程序能正常运行
* 为加快调试速度，每一类放10张图片
* 解决predict_generator报错，keras版本更新，函数输入参数改变，val_samples更改为step，现在程序可以运行，但是参数具体含义还要再研究
* 解决lunix系统下图像问题，在文件开头加上import matplotlib  和matplotlib.use('Agg')
## 代码解读
* 配置后端
 image_dim_ordering tf为tensorflow       image_data_format
* 设置参数
* 设置模型model
# 图片生成器 ImageDataGenerator.flow_from_directory
train_datagen = ImageDataGenerator(			#图片生成器，无限生成数据，直到达到规定epoch数
	rescale=1. / 255,				#缩放因子
	shear_range=0.2,				#剪切强度
	zoom_range=0.2,					#随机缩放幅度
	horizontal_flip=True,				#随机水平翻转
	vertical_flip=False,				#随机竖直翻转
	width_shift_range=0.3,				#图片宽度比例，数据提升时水平偏移幅度
	height_shift_range=0.3,				#图片高度比例，数据提升时垂直偏移幅度
	rotation_range=0.2,				#数据提升时，随机转动的角度
	fill_mode='nearest')				#图形变换时，超出边界点的处理方式
train_generator = train_datagen.flow_from_directory(#以文件夹问路径，生成经过数据提升/归一化后的数据，在一个无限循环中无限产生batch数据
	train_data_dir,					#目标文件夹
	target_size=(img_height, img_width),		#图形尺寸
	batch_size=batch_size,				#batch数据的大小
	class_mode='categorical',			#返回的标签数据的形式
	shuffle=True)					#是否打乱数据
# 模型评估
model.evaluate_generator
# 模型预测
odel.predict_generator

