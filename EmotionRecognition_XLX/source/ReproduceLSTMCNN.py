# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import tflearn
import numpy as np
import tensorflow as tf
import scipy.io as sio
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.helpers.regularizer import add_weights_regularizer
from tflearn.layers.core import flatten, dropout
from tflearn.layers.conv import conv_2d, max_pool_2d, avg_pool_2d
from tflearn.layers.normalization import local_response_normalization

DATA_PATH = '~/xlx/'

# Constant Value
NUM_INTERVIEW = 32
NUM_FRAME = 63
NUM_SCALE = 32
NUM_CHANNEL = 32
NUM_VIDEO = 40

NUM_TRAIN = 28
NUM_TEST = 4
NUM_OUTPUT_CLASS = 2
SIZE_TRAIN = NUM_TRAIN * NUM_VIDEO
SIZE_TEST = NUM_TEST * NUM_VIDEO


## Data
# Grab the prepocessed data from data folder
print('Start Loading Data')
wholeX = sio.loadmat('CWTX_Normalized.mat')['WholeX']
dataY = sio.loadmat('CWTY_Normalized.mat')['WholeY'][0]
wholeY = np.zeros((NUM_VIDEO * NUM_INTERVIEW, 2))
wholeY[dataY >= 5, 1] = 1  #724
wholeY[dataY < 5, 0] = 1  #556
# To test whether the network is trainable (in very low standard)
# wholeX[dataY >= 5] = np.ones([NUM_FRAME, NUM_CHANNEL, NUM_SCALE])
# wholeX[dataY < 5] = np.zeros([NUM_FRAME, NUM_CHANNEL, NUM_SCALE])
trainX, trainY = wholeX[:SIZE_TRAIN , :, :], wholeY[:SIZE_TRAIN, :]
testX, testY = wholeX[SIZE_TRAIN:, :, :], wholeY[SIZE_TRAIN:, :]
print('Finish Loading Data')

cnt_class_1 = 0
index_train = np.ones(SIZE_TRAIN, dtype=np.bool)
for i in range(SIZE_TRAIN):
    if dataY[i] >= 5:
        if cnt_class_1 <= 556: cnt_class_1 += 1
        else: index_train[i] = False
trainX = trainX[index_train]
trainY = trainY[index_train]
print(trainX.shape)
print(trainY.shape)

## Network
# TODO: Make sure the CNN Model is truly reused
def CNNModel(x, reuse=False):
    conv_1 = conv_2d(x, 8, [32, 1], activation='relu', regularizer="L2", scope='conv_1', reuse=reuse)
    avg_pool_1 = avg_pool_2d(conv_1, [1, 2])
    output_layer_1 = local_response_normalization(avg_pool_1)

    conv_2 = conv_2d(output_layer_1, 16, [1, 1], activation='relu', regularizer="L2", scope='conv_2', reuse=reuse)
    avg_pool_2 = avg_pool_2d(conv_2, [1, 2])
    output_layer_2 = local_response_normalization(avg_pool_2)

    output_conv = flatten(output_layer_2)

    return output_conv

def FCModel(x, reuse=False):
    network =  tflearn.fully_connected(x, 256, activation='relu', regularizer='L2', scope='fc_1', reuse=reuse)
    network = dropout(network, 0.8)
    return tflearn.fully_connected(network, NUM_OUTPUT_CLASS, activation='softmax', regularizer='L2', scope='fc_2', reuse=reuse)


# Network building
input_ = tflearn.input_data([None, NUM_FRAME, NUM_CHANNEL, NUM_SCALE])

# Construct a sequence for the input of LSTM. The size is NUM_FRAME
# TODO: Wrap it with the FCModel code if confirm the model is truly reused
lstm_input = []
for frame_index in range(NUM_FRAME):
    frame_input = tf.reshape(input_[:, frame_index, :, :], [-1, NUM_CHANNEL, NUM_SCALE, 1])
    lstm_input.append(CNNModel(frame_input, reuse=(True if frame_index > 0 else False)))
lstm_input = tf.stack(lstm_input, 1) #old is pack

seq_lstm = tflearn.lstm(lstm_input, 128, dropout=0.5, return_seq=True)

fc_output = []
for frame_index in range(NUM_FRAME):
    frame_input = seq_lstm[frame_index]
    fc_output.append(FCModel(frame_input, reuse=(True if frame_index > 0 else False)))
fc_output = tf.stack(fc_output, 0)

avg_output = tf.reduce_mean(fc_output, 0)
# For test purpose, use a simple network to predict
# avg_output = tflearn.fully_connected(input_, NUM_OUTPUT_CLASS, activation='softmax', regularizer='L2') 
net = tflearn.regression(avg_output, optimizer='sgd', learning_rate=1e-2, loss='categorical_crossentropy')

# Training
model = tflearn.DNN(net, tensorboard_verbose=0)
print('Start Training')
model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True, batch_size=16, n_epoch=10)
unique, counts = np.unique(np.argmax(model.predict(testX), axis=1), return_counts=True)
print(dict(zip(unique, counts)))