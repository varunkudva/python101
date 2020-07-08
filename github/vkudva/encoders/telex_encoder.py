# encode
'''
Class to
'''

from collections import Counter

from github.vkudva.encoders.encoder_factory import BaseSerDes

ENCODE_MAP = {
    '.': 'DOT',
    ',': 'COMMA',
    '?': 'QUESTION MARK',
    '!': 'EXCLAMATION MARK'
}


class TelexSerdes(BaseSerDes):
    """

    """

    def __init__(self):
        super().__init__("telex")

    def encode(self, input):
        """
        example: "test., this code?"
        :param input: string
        :return:
        """
        # count space required for additional characters
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
    print(TelexSerdes().encode("test., this code?"))
