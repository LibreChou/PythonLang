import unittest


class TestContainer(unittest.TestCase):
    def test_set(self):
        basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
        print(basket)

        a = set('abracadabra')
        b = set('alacazam')

        print('a=', a, 'b=', b)

        print(a - b)  # letters in a but not in b

        print(a | b)  # letters in a or b or both

        print(a & b)  # letters in both a and b

        print(a ^ b)  # letters in a or b but not both

        b = [x for x in 'abracadabra' if x not in 'abc']
        print(b)

        c = {x for x in 'abracadabra' if x not in 'abc'}
        print(c)
        pass

    def test_dict(self):
        tel = {'jack': 4098, 'sape': 4139}
        print(tel)

        a = {x: x ** 2 for x in range(10)}
        print(a)
        pass

    def test_loop(self):
        knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        for k, v in knights.items():
            print(k, v)

        for i, v in enumerate(['tic', 'tac', 'toe']):
            print(i, v)

        questions = ['name', 'quest', 'favorite color']
        answers = ['lancelot', 'the holy grail', 'blue']

        for q, a in zip(questions, answers):
            print("what's your {0}? It is  {1}".format(q, a))

        pass


if __name__ == '__main__':
    unittest.main()
