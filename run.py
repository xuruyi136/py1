# def create_class(name):
#     if name=='user':
#        class User:
#         def __str__(self):
#             return "user"
#        return User
# #type动态创建类
# # User =type("User",(),{})
#
# class BaseClass():
#     def answer(self):
#         return  'i am user'
#
#     def say(self):
#          return 'i am method'
#     # return self.name
#
#
# class MetaClass(type):
#     def __new__(cls, *args, **kwargs):
#       return  type.__new__(cls,*args,**kwargs)
# #什么是元类，元类是创建类的类，对象《- class(对象）《type
# class User(object,metaclass=MetaClass):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'user'
#
#
# if __name__ == '__main__':
#     # Myclass = create_class("user")
#     # my_obj = Myclass()
#     # print(type(my_obj))
#
#     User =type("User",(BaseClass,),{"name":"user","say":say})
#
#     print(User().say())

    # My_obj = User('body1')
    # print(My_obj.name)

class Mymeta(type):

    def __call__(self, *args, **kwargs):          #会在调用对象时自动触发，此时的对象时一个类，即People
        print(self) # self是People
        print(args)
        print(kwargs)
        # return 123
        """调用类产生一个对象，发生两件事"""       #和class定义类，调用类一样发生两件事
        # 1、先造出一个People的空对象
        obj=self.__new__(self)                   #造出了一个自定义类People的空对象
        # 2、为该对空对象初始化独有的属性
        # print(args,kwargs)
        self.__init__(obj,*args,**kwargs)        #对空对象进行初始化，空对象传入，以及参数原封不动的传入

        # 3、返回一个初始好的对象
        return obj                               #将造出的对象返回，

'''**********************************看成一个对象************************************************'''
class People(object,metaclass=Mymeta):           #自定义类People，元类是Mymeta,元类必须继承type类，否则就不是元类
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('%s is eating' %self.name)


    def __new__(cls, *args, **kwargs):           #对象自己中有__new__属性,先从对象自己的名称空间中找，自己没有在到自己的类中找
        print(cls)
        # cls.__new__(cls) # 错误                 #自己有调用了自己的__new__,这样就出现无线递归，所以会报错
        obj=super(People,cls).__new__(cls)       #自己中有，我们任然让其取继承父类中的__new__属性,来产生一个空对象，然后将对象初始化，拿到一个返回值
        return obj
# obj1=People('egon1',age=18)
# print(obj1.__dict__)
# print(obj1.name)
# print(obj1.age)
# # obj2=People('egon2',age=18)
# print(obj1)
# print(obj2)

# obj=People('egon',age=18)
# print(obj.__dict__)
# print(obj1.name)
# obj1.eat()
# class Foo:
#     def __call__(self, *args, **kwargs):
#         print(self)      #<__main__.Foo object at 0x000002193E892E10>
#         print(args)       #(1, 2, 3)----------------*args接收位置参数，存成元组的形式
#         print(kwargs)     #{'x': 1, 'y': 2}---------**kwargs接收关键字参数，存成字典的形式
#
#
# print(u'顺序抓取')
# import requests
# requests.get(allow_redirects=False)
#
# HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
#            'Accept-Language': 'zh-CN,zh;q=0.8',
#            'Accept-Encoding': 'gzip, deflate', }
# URLS = ['http://www.cnblogs.com/moodlxs/p/3248890.html',
#         'https://www.zhihu.com/topic/19804387/newest',
#         'http://blog.csdn.net/yueguanghaidao/article/details/24281751',
#         'https://my.oschina.net/visualgui823/blog/36987',
#         'http://blog.chinaunix.net/uid-9162199-id-4738168.html',
#         'http://www.tuicool.com/articles/u67Bz26',
#         'http://rfyiamcool.blog.51cto.com/1030776/1538367/',
#         'http://itindex.net/detail/26512-flask-tornado-gevent']
#
#
# def thread():
#     from threading import Thread
#     import requests
#     import time
#     urls = URLS
#     headers = HEADERS
#     headers['user-agent'] = "Mozilla/5.0+(Windows+NT+6.2;+WOW64)+AppleWebKit/537.36+" \
#                             "(KHTML,+like+Gecko)+Chrome/45.0.2454.101+Safari/537.36"
#
#     def get(url):
#         try:
#             r = requests.get(url, allow_redirects=False, timeout=2.0, headers=headers)
#         except:
#             pass
#         else:
#             print(r.status_code, r.url)
#
#     print(u'多线程抓取')
#     ts = [Thread(target=get, args=(url,)) for url in urls]
#     starttime = time.time()
#     for t in ts:
#         t.start()
#     for t in ts:
#         t.join()
#     endtime = time.time()
#     print(endtime - starttime)
#
#
# thread()

print(int('101',base=5))
# help(int)

import re
string1 = """<div>静夜思
窗前明月光
疑是地上霜
举头望明月
低头思故乡
</div>"""

tuple1 = (1,2,'爱老虎油')


fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
['BANANA', 'APPLE', 'LIME']

# List and the enumerate function
import threading
import time

mutex = threading.BoundedSemaphore(2)

def worker(num):
    time.sleep(1)
    mutex.acquire()
    print( "this is ",num)
    mutex.release()
def worker1(num):
    time.sleep(1)
    mutex.acquire()
    print( "this is ",num)
    mutex.release()
if __name__ == '__main__':
    # for i in range(10):
        # th = threading.Thread(target=worker, args=(i,), name="thread %d" % i)
        # th.start()
    th = [threading.Thread(target=worker, args=(i,)) for i in range(0,10)]
    th1 = [threading.Thread(target=worker1, args=(i,)) for i in range(0, 10)]
    for t in th:
        t.start()
    for t in th1:
        t.start()