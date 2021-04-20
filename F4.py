# -*- coding: utf-8 -*-
from Jsteg import Jsteg


class F4(Jsteg):
    def __init__(self):
        Jsteg.__init__(self)

    def set_sequence_after_dct(self, sequence_after_dct):
        self.sequence_after_dct = sequence_after_dct
        sum_len = len(self.sequence_after_dct)
        zero_len = len([i for i in self.sequence_after_dct if i == 0])
        one_len = len([i for i in self.sequence_after_dct if i in (-1, 1)])
        self.available_info_len = sum_len-zero_len-one_len  # 不是特别可靠
        print("Load>> 大约可嵌入", sum_len-zero_len-int(one_len/2), 'bits')
        print("Load>> 最少可嵌入", self.available_info_len, 'bits\n')

    def _write(self, index, data):
        origin = self.sequence_after_dct[index]
        if origin == 0:
            return False
        elif origin == 1 and data == 0:
            self.sequence_after_dct[index] = 0
            return False

        elif origin == -1 and data == 1:
            self.sequence_after_dct[index] = 0
            return False

        lower_bit = origin % 2

        if origin > 0:
            if lower_bit != data:
                self.sequence_after_dct[index] = origin-1
        else:
            if lower_bit == data:
                self.sequence_after_dct[index] = origin+1
        return True

    def _read(self, index):
        if self.sequence_after_dct[index] > 0:
            return self.sequence_after_dct[index] % 2
        elif self.sequence_after_dct[index] < 0:
            return (self.sequence_after_dct[index]+1) % 2
        else:
            return None


if __name__ == "__main__":
    f4 = F4()
    # 写
    sequence_after_dct = [-1, 0, 1]*100+[i for i in range(-7, 500)]
    f4.set_sequence_after_dct(sequence_after_dct)
    info1 = [0, 1, 0, 1, 1, 0, 1, 0]
    f4.write(info1)
    # 读
    sequence_after_dct2 = f4.get_sequence_after_dct()
    f4.set_sequence_after_dct(sequence_after_dct2)
    info2 = f4.read()
    print(info2)
