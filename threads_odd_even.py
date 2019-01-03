#!/usr/bin/env python
"""
Print odd even numbers using 2 threads with wait-notify

"""
import sys
import threading

class SharedObject(object):
    def __init__(self):
        self.odd_flag = True


class evenThread(threading.Thread):
    def __init__(self, name, sh_obj, count=10):
        super(evenThread, self).__init__(name=name)
        self.seed = 2
        self.sh_obj = sh_obj
        self.count = count
    def run(self):
        for loop in range(self.count):
            while self.sh_obj.odd_flag:
                # wait till odd flag is false
                pass

            print("{}: {}".format(self.getName(), self.seed))
            self.seed += 2
            self.sh_obj.odd_flag = True

class oddThread(threading.Thread):
    def __init__(self, name, sh_obj, count=10):
        super(oddThread, self).__init__(name=name)
        self.seed = 1
        self.sh_obj = sh_obj
        self.count = count
    def run(self):
        for loop in range(self.count):
            while not self.sh_obj.odd_flag:
                # wait till odd flag is true
                pass

            print("{}: {}".format(self.getName(), self.seed))
            self.seed += 2
            self.sh_obj.odd_flag = False


if __name__ == '__main__':
    sh_obj = SharedObject()
    odd = oddThread('odd-thread', sh_obj)
    even = evenThread('even-thread', sh_obj)
    odd.start()
    even.start()
