## chestCamera

### 复现结果(50epochs,2-fold)

- Basemodel: DenseNet121

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/ChestCamera/basemodel.png)

- Generator 
- Epochs =50
- 2-fold
- loss: 0.0569 , acc: 0.9850 , val_loss: 1.6048 , val_acc: 0.6750
- Test results:auc=0.64

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/ChestCamera/week1-1.png)


### Fine-tune

- 初始固定参数不训练，之后从后到前逐渐放开Dense Block参数训练
- layer_number = 610
- loss: 0.1566 , acc: 0.9735 , val_loss: 1.1647 , val_acc: 0.6417
- Test results:auc=0.56

![image](https://github.com/Junya5/DataScience/blob/master/ColonyDetection-Junya5/IMG/ChestCamera/week1-2.png)

* 结果并没有进步，反而比之前还要差一些

* 100epochs
* binary_crossentropy，binary_accuracy
* 测试结果也基本没有改进，可能还是需要从参数训练控制方法上找问题 


### 指定GPU训练并限制GPU用量

```
import os
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF

# 指定第一块GPU可用 
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

config = tf.ConfigProto()  
config.gpu_options.allow_growth=True   #不全部占满显存, 按需分配
sess = tf.Session(config=config)
KTF.set_session(sess)
```