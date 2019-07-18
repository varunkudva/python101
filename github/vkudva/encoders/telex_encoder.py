# encode
'''
Class to
'''

from encoder_factory import BaseSerDes
from collections import Counter

ENCODE_MAP = {
    '.': 'DOT',
    ',': 'COMMA',
    '?': 'QUESTION MARK',
    '!': 'EXCLAMATION MARK'
}

class TelexSerdes(object):
    def __init__(self):
        pass
    def encode(self, input):
        """
        example: "test., this code?"
        :param input: string
        :return:
        """
        char_counter = Counter(input)
        write_idx = len(input)
        for char, count in char_counter.items():
            if char in ENCODE_MAP.keys():
                write_idx += count * (len(ENCODE_MAP[char]) - 1)

        res = [''] * write_idx
        write_idx = 0
        for char in input:
            if char in ENCODE_MAP.keys():
                res[write_idx: len(ENCODE_MAP[char])+1] = ENCODE_MAP[char]
                write_idx += len(ENCODE_MAP[char])
            else:
                res[write_idx] = char
                write_idx += 1
        return ''.join(res)

    def decode(self, input):
        pass


if __name__ == '__main__':
    print TelexSerdes().encode("test., this code?")

