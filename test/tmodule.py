import unittest
import fibo


class TestModule(unittest.TestCase):
    def test_fibo(self):
        print(fibo.fib(1000))
        print(fibo.__name__)
        pass



if __name__ == '__main__':
    unittest.main()
