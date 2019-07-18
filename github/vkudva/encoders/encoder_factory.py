# coding=utf-8
class BaseSerDes(object):
    " Abstract class for encoder"
    def __init__(self):
        pass
    def encode(self, input):
        pass
    def decode(self, input):
        pass

