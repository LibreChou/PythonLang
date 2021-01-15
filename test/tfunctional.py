import unittest


class FunctionCase(unittest.TestCase):
    def test_del(self):
        # Strategy:  Iterate over a copy
        users = {}
        for user, status in users.copy().items():
            if status == 'inactive':
                del users[user]

        # Strategy:  Create a new collection
        active_users = {}
        for user, status in users.items():
            if status == 'active':
                active_users[user] = status

    def test_range(self):
        #range() 所返回的对象在许多方面表现得像一个列表，但实际上却并不是。
        # 此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，这样就能节省空间。
        pass

    def test_sum(self):
        print(sum(range(45)))

if __name__ == '__main__':
    unittest.main()
