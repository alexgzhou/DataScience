import numpy as np
from itertools import product
import cPickle as p

frequency_boundary = [(1, 3), (4, 7), (8, 13), (14, 30), (31, 50)]

NUM_POS = 32
NUM_SPECTRUM = 5
NUM_DEFAULT_CHANNEL = 40
NUM_LABEL = 4
NUM_CHANNEL = NUM_POS * NUM_SPECTRUM
NUM_POINT = 8064
NUM_SAMPLING = 128
NUM_VIDEO = 40
NUM_INTERVIEWEE = 32
NUM_OUTPUT_CLASS = 3
NUM_SPAN = NUM_POINT / NUM_SAMPLING
SIZE_WINDOW = 9
NUM_SPLITTED = NUM_SPAN / SIZE_WINDOW

def unpickle(file):
    f = open(file, 'rb')
    dict = p.load(f)
    f.close()
    return dict

def to_x(data):
    num_data = len(data)
    data.resize(num_data * NUM_VIDEO, NUM_DEFAULT_CHANNEL, NUM_POINT)
    size_data = np.shape(data)
    num_sample = size_data[0]
    # Processing
    result = np.zeros((num_sample * NUM_SPLITTED, SIZE_WINDOW, NUM_CHANNEL))
    for sample_index, channel_index, time_frame in product(range(num_sample), range(NUM_POS), range(NUM_SPAN)):
        FFT = np.fft.fft(data[sample_index, channel_index, time_frame * NUM_SAMPLING:(time_frame + 1) * NUM_SAMPLING])
        for frequency_channel in range(NUM_SPECTRUM):
            start, end = frequency_boundary[frequency_channel]
            frequency = FFT[start: end+1]
            result[(sample_index/SIZE_WINDOW) * NUM_SPLITTED + time_frame, 
                    sample_index % SIZE_WINDOW,
                    channel_index * NUM_SPECTRUM + frequency_channel] \
            = np.log(np.vdot(frequency, frequency).real)
    #Normalizeation
    maxs = np.max(np.abs(result), axis = 0)
    maxs = np.max(maxs, axis = 0)
    for i in range(NUM_CHANNEL):
        result[:, :, i] /= maxs[i]
    return result

def to_y(data):
    data.resize(len(data) * NUM_VIDEO, NUM_LABEL)
    value_class = map(lambda x: 0 if x <= 3.0 else 1 if x <= 6.0 else 2, data[:, 0])
    unique, counts = np.unique(value_class, return_counts=True)
    print(dict(zip(unique, counts)))
    n_data = len(value_class)
    res = np.zeros((n_data, NUM_OUTPUT_CLASS))
    res[np.arange(n_data), value_class] = 1
    # features were divided.
    return np.repeat(res, NUM_SPLITTED, axis = 0)


if __name__ == "__main__":
    pre_batch = 'D:/Year4/DataScience/EmotionRecognition_XLX/source/data_preprocessed_python/'
    whole_data = np.array([unpickle(pre_batch + 's%.2d.dat'%i) for i in range(1, NUM_INTERVIEWEE + 1)])
    tempx = map(lambda x: x["data"], whole_data)
    tempy = map(lambda x: x["labels"], whole_data)
    arrayx = np.array(tempx)
    arrayy = np.array(tempy)
    whole_x = to_x(arrayx)
    whole_y = to_y(arrayy)
    print whole_x.shape # (8960, 9, 160)
    print whole_y.shape # (8960, 3)
    print whole_x[100, :, :]
    with open(pre_batch + 'SplittedFlattenedPSD.dat', 'wb') as f:
        p.dump({'x': whole_x, 'y': whole_y}, f)
