import unittest


class ListCase(unittest.TestCase):
    def test_operator(self):
        squares = [1, 4, 9, 16, 25]
        print(squares[:])
        print(squares + [36, 49, 64, 81, 100]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        pass

    def test_list(self):
        squares = []
        for x in range(10):
            squares.append(x ** 2)
        print(squares)

        squares = list(map(lambda x: x ** 2, range(10)))
        print(squares)

        #列表推导式的结构是由一对方括号所包含的以下内容：
        # 一个表达式，后面跟一个 for 子句，然后是零个或多个 for 或 if 子句。
        #  其结果将是一个新列表，由对表达式依据后面的 for 和 if 子句的内容进行求值计算而得出。
        #  举例来说，以下列表推导式会将两个列表中不相等的元素组合起来:

        squares = [x ** 2 for x in range(10)]
        print(squares)

    def test_del(self):
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        del a[0]
        print(a)

        del a[2:4]
        print(a)

        del a[:]
        print(a)

    def test_tuple(self):
        t = 12345, 54321, 'hello!'
        u = t, (1, 2, 3, 4, 5)



if __name__ == '__main__':
    unittest.main()
