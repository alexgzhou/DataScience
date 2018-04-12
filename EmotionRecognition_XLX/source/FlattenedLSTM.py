
from __future__ import division, print_function, absolute_import

import cPickle as p
import tflearn
import numpy as np
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.helpers.regularizer import add_weights_regularizer
from tflearn.layers.core import flatten
from tflearn.datasets import imdb

#DATA_PATH = 'D:/Year4/DataScience/EmotionRecognition_XLX/source/data_preprocessed_python/'
NUM_DEFAULT_CHANNEL = 40

NUM_POS = 32
NUM_SPECTRUM = 5
NUM_LABEL = 4
NUM_POINT = 8064
NUM_SAMPLING = 128
NUM_VIDEO = 40
NUM_INTERVIEWEE = 32
NUM_OUTPUT_CLASS = 3
SIZE_WINDOW = 9
NUM_CHANNEL = NUM_POS * NUM_SPECTRUM
NUM_SPAN = NUM_POINT // NUM_SAMPLING
NUM_SPLITTED = NUM_SPAN // SIZE_WINDOW

NUM_TRAIN = 28
NUM_TEST = 4
SIZE_TRAIN = NUM_TRAIN * NUM_VIDEO * NUM_SPLITTED
SIZE_TEST = NUM_TEST * NUM_VIDEO * NUM_SPLITTED

with open('SplittedFlattenedPSD.dat', 'rb') as f: 
    whole_data = p.load(f)
wholeX, wholeY = whole_data['x'], whole_data['y']
trainX, trainY = wholeX[:SIZE_TRAIN , :, :], wholeY[:SIZE_TRAIN, :]
testX, testY = wholeX[SIZE_TRAIN:, :, :], wholeY[SIZE_TRAIN:, :]

# Network building
input_ = tflearn.input_data([None, SIZE_WINDOW, NUM_CHANNEL])
lstm_1 = tflearn.lstm(input_, 200, dropout=0.8, return_seq=True)
# tflearn.helpers.regularizer.add_weights_regularizer(lstm_1, loss='L2')
# net = tflearn.lstm(net, 200, dropout=0.8)
# tflearn.add_weights_regularization(net, loss='L2')
fc_1 = tflearn.fully_connected(tflearn.layers.core.flatten(lstm_1), NUM_OUTPUT_CLASS, activation='softmax', regularizer='L2')
net = tflearn.regression(fc_1, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy')

# Training
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True, batch_size=16)
unique, counts = np.unique(np.argmax(model.predict(testX), axis=1), return_counts=True)
print(dict(zip(unique, counts)))
