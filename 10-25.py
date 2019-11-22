# import zipfile
# import random
# import time
# import sys
#
#
# class MyIterator():
#     # 单位字符集合
#     letters = 'abcdefghijklmnopqrstuvwxyz012345678'
#     min_digits = 0
#     max_digits = 0
#
#     def __init__(self, min_digits, max_digits):
#         # 实例化对象时给出密码位数范围，一般4到10位
#         if min_digits < max_digits:
#             self.min_digits = min_digits
#             self.max_digits = max_digits
#         else:
#             self.min_digits = max_digits
#             self.max_digits = min_digits
#
#     # 迭代器访问定义
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         rst = str()
#         for item in range(0, random.randrange(self.min_digits, self.max_digits + 1)):
#             rst += random.choice(MyIterator.letters)
#         return rst
#
#
# def extract():
#     start_time = time.time()
#     zfile = zipfile.ZipFile("python.zip")
#     for p in MyIterator(5, 6):
#         try:
#             zfile.extractall(path=".", pwd=str(p).encode('utf-8'))
#             print("the password is {}".format(p))
#             now_time = time.time()
#             print("spend time is {}".format(now_time - start_time))
#             sys.exit(0)
#         except Exception as e:
#             pass
#
#
# if __name__ == '__main__':
#     extract()

import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#
#
# def main():
#     try:
#         s = Scheduler()
#         s.run()
#     except:
#         main()

def create_class(name):
    if name=='user':
       class User:
        def __str__(self):
            return "user"
       return User
#type动态创建类
# User =type("User",(),{})

class BaseClass():
    def answer(self):
        return  'i am user'

def say(self):
    return 'i am111 user'
    # return self.name


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
      return  type.__new__(cls,*args,**kwargs)
#什么是元类，元类是创建类的类，对象《- class(对象）《type
class User(metaclass=MetaClass):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'user'


if __name__ == '__main__':
    # Myclass = create_class("user")
    # my_obj = Myclass()
    # print(type(my_obj))

    User =type("User",(BaseClass,),{"name":"user","say":say})
    My_obj = User()
    print(My_obj.answer())
    # My_obj = User('body1')
    # print(My_obj.name)
    # main()

# class Foo(object):
#     pass
# Foo = type('Foo', (BaseClass, ), {})
# print (Foo)
# print(Foo().answer())

class MyList(object):
    """自定义的一个可迭代对象"""

    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""

    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    for num in mylist:
        print(num)






