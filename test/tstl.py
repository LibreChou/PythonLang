import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_pip(self):
        # pip install requests==2.6.0
        # pip freeze > requirements.txt 生成一个已安装包列表文件
        pass



if __name__ == '__main__':
    unittest.main()
