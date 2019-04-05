# coding=utf-8
#!/usr/bin/env python
from abc import ABC, abstractmethod

class InputData(ABC):
    """
    base class for reading input data
    """
    @abstractmethod
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    """
    Reads input data from disk path
    """
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

class NetworkInputData(InputData):
    """
    Reads data from network
    """
    def __init__(self, intf):
        super().__init__()
        self.intf = intf

    def read(self):
        # return open(tcpdump intf)
        pass

InputData().read()
