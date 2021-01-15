import unittest

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

# 类继承机制允许多个基类，派生类可以覆盖它基类的任何方法，一个方法可以调用基类中相同名称的的方法。
# 对象可以包含任意数量和类型的数据。
# 和模块一样，类也拥有 Python 天然的动态特性：它们在运行时创建，可以在创建后修改。
class TestClass(unittest.TestCase):
    def test_class(self):
        pass

    def test_scope(self):
        def scope_test():
            def do_local():
                spam = "local spam"

            def do_nonlocal():
                nonlocal spam
                spam = "nonlocal spam"

            def do_global():
                global spam
                spam = "global spam"

            spam = "test spam"
            do_local()
            print("After local assignment:", spam)
            do_nonlocal()
            print("After nonlocal assignment:", spam)
            do_global()
            print("After global assignment:", spam)

        x = scope_test();
        print("In global scope:", spam)

    def test_variable(self):
        class Dog:
            kind = 'canine'  # class variable shared by all instances

            def __init__(self, name):
                self.name = name  # instance variable unique to each instance

        d = Dog('Fido')
        e = Dog('Buddy')

        print(d.kind)
        print(e.kind)

    def test_multiextends(self):
        pass

    def test_private(self):
        # 大多数 Python 代码都遵循这样一个约定：带有一个下划线的名称 (例如 _spam) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。
        # 这应当被视为一个实现细节，可能不经通知即加以改变。

        class Mapping:
            def __init__(self, iterable):
                self.items_list = []
                self.__update(iterable)

            def update(self, iterable):
                for item in iterable:
                    self.items_list.append(item)

            __update = update  # private copy of original update() method

        class MappingSubclass(Mapping):
            def update(self, keys, values):
                # provides new signature for update()
                # but does not break __init__()
                for item in zip(keys, values):
                    self.items_list.append(item)

        data = [1, 2, 3, 4, 5, 6, 7, 8]
        container = MappingSubclass(data)
        container.update([1, 2, 3, 4], [5, 6, 7, 8])

    def test_empty(self):
        class Employee:
            pass

        john = Employee()  # Create an empty employee record

        # Fill the fields of the record
        john.name = 'John Doe'
        john.dept = 'computer lab'
        john.salary = 1000

        print(john)

    def test_iterator(self):
        class Reverse:
            def __init__(self, data):
                self.data = data
                self.index = len(data)

            def __iter__(self):
                return self

            def __next__(self):
                if self.index == 0:
                    raise StopIteration
                self.index = self.index - 1
                return self.data[self.index]

            pass

        rev = Reverse('hello world')
        it = iter(rev)

        for ch in rev:
            print(ch)

    # Generator 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似标准的函数，但当它们要返回数据时会使用 yield 语句。
    # 每次对生成器调用 next() 时，它会从上次离开位置恢复执行（它会记住上次执行语句时的所有数据值）。
    def test_generator(self):
        for ch in reverse("hello world"):
            print(ch)

        sum(i*i for i in range(10))



    pass
