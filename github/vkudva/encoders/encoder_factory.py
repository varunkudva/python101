# coding=utf-8
class BaseSerDes(object):
    " Abstract class for encoder"

    def __init__(self, name):
        self.name = name

    def encode(self, input):
        pass

    def decode(self, input):
        pass
