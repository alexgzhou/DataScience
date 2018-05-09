import numpy as np
import cPickle as p #python3为pickle python2为cPickle tensorflow中直接从pandas库中调用

frequency_boundary = [(1, 3), (4, 7), (8, 13), (14, 30), (31, 50)] #5个频率带

NUM_POS = 32
NUM_SPECTRUM = 5
NUM_DEFAULT_CHANNEL = 40
NUM_LABEL = 4 #？
NUM_CHANNEL = NUM_POS * NUM_SPECTRUM
NUM_POINT = 8064
NUM_SAMPLING = 128
NUM_VIDEO = 40
NUM_INTERVIEWEE = 32
NUM_OUTPUT_CLASS = 3
NUM_SPAN = NUM_POINT / NUM_SAMPLING
NUM_SPLITTED = NUM_SPAN

def unpickle(file):
    f = open(file, 'rb')#只读二进制
    dict = p.load(f) 
    f.close()
    return dict

def to_x(data):
    data.resize(len(data) * NUM_VIDEO, NUM_DEFAULT_CHANNEL, NUM_POINT)
    size_data = np.shape(data)
    num_data = size_data[0]
    # Processing
    result = np.zeros((num_data * NUM_SPLITTED, NUM_CHANNEL))
    for sample_index in range(num_data):
        for channel_idx in range(NUM_POS):
            for time_frame in range(NUM_SPAN):
                FFT = np.fft.fft(data[sample_index, channel_idx, time_frame * NUM_SAMPLING:(time_frame + 1) * NUM_SAMPLING])
                for frequency_channel in range(NUM_SPECTRUM):
                    start, end = frequency_boundary[frequency_channel]
                    frequency = FFT[start: end+1]
                    result[sample_index * NUM_SPAN + time_frame, channel_idx * NUM_SPECTRUM + frequency_channel] = np.vdot(frequency, frequency).real
    #Normalizeation
    return result

def to_y(data):
    data.resize(len(data) * NUM_VIDEO, NUM_LABEL)
    value_class = map(lambda x: 0 if x <= 3.0 else 1 if x <= 6.0 else 2,
            data[:, 0])
    unique, counts = np.unique(value_class, return_counts=True)
    print(dict(zip(unique, counts)))
    n_data = len(value_class)
    res = np.zeros((n_data, NUM_OUTPUT_CLASS))
    res[np.arange(n_data), value_class] = 1
    # features were divided.
    return np.repeat(res, NUM_SPLITTED, axis = 0)


if __name__ == "__main__":
    pre_batch = 'D:/Year4/DataScience/EmotionRecognition_XLX/source/data_preprocessed_python/' #。dat数据路径
    whole_data = np.array([unpickle(pre_batch + 's%.2d.dat'%i) for i in range(1, NUM_INTERVIEWEE + 1)])
    datatox = np.array(map(lambda x: x["data"], whole_data))#data：40*40*8064
    datatoy = np.array(map(lambda x: x["labels"], whole_data))#labels:40*4
    whole_x = to_x(datatox)
    whole_y = to_y(datatoy)
    with open(pre_batch + 'FlattenedPSD.dat', 'wb') as f:
        p.dump({'x': whole_x, 'y': whole_y}, f)
