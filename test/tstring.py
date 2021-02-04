import unittest
import sys

print(sys.argv)

import cupy as np
np.cuda.set_allocator(np.cuda.MemoryPool().malloc)

print('\033[92m' + '-' * 60 + '\033[0m')
print(' ' * 23 + '\033[92mGPU Mode (cupy)\033[0m')
print('\033[92m' + '-' * 60 + '\033[0m\n')


class StringCase(unittest.TestCase):
    def test_pring(self):
        print('1 C:\some\name')
        print("2 C:\some\name")
        print(r"3 C:\some\name")

        print("""\
                Usage: thingy [OPTIONS]
                     -h                        Display this usage message
                     -H hostname               Hostname to connect to
                """)

    def test_index(self):
        word = 'Python'
        #切片中的越界索引会被自动处理:
        print(word[:3])
        print(word[3:])
        #Python 中的字符串不能被修改，它们是 immutable 的。
        # 因此，向字符串的某个索引位置赋值会产生一个错误:


if __name__ == '__main__':
    unittest.main()
