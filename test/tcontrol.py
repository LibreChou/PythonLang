import unittest


def def_change(a, L=[]):
    L.append(a)
    return L


def def_nochange(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# 字典参数
# 当存在一个形式为 **name 的最后一个形参时，它会接收一个字典 (参见 映射类型 --- dict)，
# 其中包含除了与已有形参相对应的关键字参数以外的所有关键字参数。
# 这可以与一个形式为 *name，接收一个包含除了与已有形参列表以外的位置参数的 元组 的形参 (将在下一小节介绍) 组合使用 (*name 必须出现在 **name 之前。)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


class ControlCase(unittest.TestCase):
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
        # range() 所返回的对象在许多方面表现得像一个列表，但实际上却并不是。
        # 此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，这样就能节省空间。
        pass

    def test_sum(self):
        print(sum(range(45)))

    def test_return(self):
        # return 语句会从函数内部返回一个值。 不带表达式参数的 return 会返回 None。 函数执行完毕退出也会返回 None。
        pass

    def test_default(self):
        print(def_change(1))
        print(def_change(2))
        print(def_change(3))

        print(def_nochange(1))
        print(def_nochange(2))
        print(def_nochange(3))

    def test_keyarg(self):
        cheeseshop("Limburger", "It's very runny, sir.",
                   "It's really very, VERY runny, sir.",
                   shopkeeper="Michael Palin",
                   client="John Cleese",
                   sketch="Cheese Shop Sketch")

    def test_unpack(self):
        print(list(range(3, 6)))

        args = [3, 6]
        print(list(range(*args)))

    def parrot(self, voltage, state='a stiff', action='voom'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.", end=' ')
        print("E's", state, "!")

    def test_unpack_map(self):
        d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
        self.test_default()

    def test_lambda(self):
        pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
        pairs.sort(key=lambda t: t[0])
        print(pairs)

        pairs.sort(key=lambda t: t[1])
        print(pairs)

    def anno(self, ham: str, eggs: str = 'eggs') -> str:
        print("Annotations:", self.anno.__annotations__)
        print("Arguments:", ham, eggs)
        return ham + 'and' + eggs

    def test_annotations(self):
        ret = self.anno('spam')
        print('result=', ret)


if __name__ == '__main__':
    unittest.main()


