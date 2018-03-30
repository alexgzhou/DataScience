# coding:utf-8

import time
import json

class Log:

    def __init__(self, name=None):

        if name is None:
            time_stamp = self.get_time_stamp()
            self.file = open('../log/log-%s.txt' % time_stamp, 'a')
        else:
            self.file = open('../log/log-%s.txt' % str(name), 'a')

        self.code = json.load(open('./code.json'))
        self.file.write('\r\n')
        self.file.flush()

    @ staticmethod
    def get_time_stamp():
        return time.strftime('%Y-%m-%d-%H-%M-%S')

    def write_log(self, line):
        s = self.get_time_stamp() + ': ' + line + '\r\n'
        self.file.write(s)
        self.file.flush()

    def write_format_log(self, behave, dataset, algorithm, fold=None):

        try:
            s = 'code=%d, dataset=%s, algorithm=%s, fold=%s, behave=%s' \
                % (self.code[behave], dataset, algorithm, fold, behave)
            self.write_log(s)

        except:
            raise 'behave \'' + behave + '\' not exists'
