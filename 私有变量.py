__author__ = "some_author"


class TestDemo(object):
    """
    Python变量命名用法（以字符或者下划线开头，可以包括字母、数字、下划线，区别大小写）
    一般变量
    常量
    私有变量
    内置变量

    类的私有变量和私有方法
    在Python中可以通过在属性变量名前加上双下划线定义属性为私有属性
    特殊变量命名

    1、 _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。

    2、 __xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）

    3、 __xx__定义的是特列方法。用户控制的命名空间内的变量或是属性，如init , __import__或是file 。只有当文档有说明时使用，不要自己定义这类变量。 （就是说这些是python内部定义的变量名）

    在这里强调说一下私有变量,python默认的成员函数和成员变量都是公开的,没有像其他类似语言的public,private等关键字修饰.但是可以在变量前面加上两个下划线"_",这样的话函数或变量就变成私有的.这是python的私有变量轧压(这个翻译好拗口),英文是(private name mangling.) **情况就是当变量被标记为私有后,在变量的前端插入类名,再类名前添加一个下划线"_",即形成了_ClassName__变量名.**

    Python内置类属性
    __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
    __doc__ :类的文档字符串
    __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
    __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

    """

    FINAL_VAR = "V1.0"  # 常量，不可修改的变量，以大写字母或加下划线命名，这个只是约定，即使更改了也不会报错

    class_name = "TestDemo"  # 常见变量命名，

    __maker__ = 'libingxian'  # 内置变量，两个前置下划线和两个后置下划线，内置对象所具有，声明时不可与内置变量名的重复

    def __init__(self):
        self.__private_var = "private"  # 私有变量，以两个前置下划线开头，只能在本类中使用，类外强制访问会报错
        self.public_var = "public"  # 一般变量

    def __private_method(self):  # 私有方法，以两个下划线开头、字母小写，只能在本类中使用，类外强制访问会报错
        print("i am private")
    def public_method(self):
        print("i am public")



test_demo = TestDemo()
# print(test_demo._TestDemo__private_var)
# print(test_demo.FINAL_VAR)  # 访问常量
# print(test_demo.public_var)  # 访问一般变量
# print(test_demo.__private_var) # 访问私有变量，运行会报错
# test_demo.__private_method() # 访问私有方法，运行会报错
# print(__author__)
# print(test_demo.__doc__)
# print(test_demo.__maker__)
# test_demo.public_method()

class A(object):
    '''
    fgfgdf
    '''
    def __init__(self):
        self.__data = []  # 翻译成 self._A__data=[]

    def add(self, item):
        self.__data.append(item)  # 翻译成 self._A__data.append(item)

    def __printData(self):
        print(self.__data)  # 翻译成 self._A__data
a = A()
a.add('hello')
#调用私有变量了
print(a._A__data)
#调用私有方法了
a._A__printData()
