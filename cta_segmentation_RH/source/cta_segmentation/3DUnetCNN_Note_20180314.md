# 3D U-Net Convolution Neural Network with Keras
## Tutorial using BRATS Data
### Training
1. Download the BRATS 2017 [GBM](https://app.box.com/s/926eijrcz4qudona5vkz4z5o9qfm772d) and 
[LGG](https://app.box.com/s/ssfkb6u8fg3dmal0v7ni0ckbqntsc8fy) data. Place the unzipped folders in the 
```brats/data/original``` folder.```需要翻墙```

2. Install dependencies: 
```
nibabel,
keras,
pytables,
nilearn,
SimpleITK,
nipype
```
(the last two are for preprocessing only)```还需下载安装sklearn与TensorFlow-GPU```

3. Install [ANTs N4BiasFieldCorrection](https://github.com/stnava/ANTs/releases) and add the location of the ANTs 
binaries to the PATH environmental variable.```OS X下修改完bash.profile之后要用source ~/.bash_profile使其立即生效```

4. Add the repository directory to the ```PYTONPATH``` system variable:
```
$ export PYTHONPATH=${PWD}:$PYTHONPATH
```
```
使用：
$ python
>>> import sys
>>> sys.path
查询是否增加完成
```
5. Convert the data to nifti format and perform image wise normalization and correction:

cd into the brats subdirectory:
```
$ cd brats
```
Import the conversion function and run the preprocessing:
```
$ python
>>> from preprocess import convert_brats_data
>>> convert_brats_data("data/original", "data/preprocessed")
```
6. Run the training:

To run training using the original UNet model:
```
$ python train.py
```

To run training using an improved UNet model (recommended): 
```
$ python train_isensee2017.py
```
**If you run out of memory during training:** try setting 
```config['patch_shape`] = (64, 64, 64)``` for starters. 
Also, read the "Configuration" notes at the bottom of this page.

