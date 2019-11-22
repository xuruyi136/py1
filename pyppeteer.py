import asyncio
# from pyppeteer import launch
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('http://example.com')
#     await page.screenshot({'path': 'example.png'})
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())
import sys
import os,random
print(os.path.dirname(sys.executable))

# Location: e:\program files (x86)\python\lib\site-packages
#
import os
import sys
from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

log_file_path = os.path.join(BASE_DIR, 'Log/my.log')
err_log_file_path = os.path.join(BASE_DIR, 'Log/err.log')

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
# logger.add(s)
logger.add(log_file_path, rotation="500 MB", encoding='utf-8')  # Automatically rotate too big file
logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8',
           level='ERROR')  # Automatically rotate too big file
logger.debug("That's it, beautiful and simple logging!")
logger.debug("中文日志可以不")
# logger.error("严重错误")
class xici():
    def __init__(self):
        pass
    def get(self):
        return '2'
class gatherproxy():
    def __init__(self):
        pass
    def get(self):
       return '1'
# print( random.choice('tomorrow') )
# a=[xici(),2,3]
# print(a[0].get())
# # for i in a:
# #     print(i)
# free_proxy_sources = [xici(), gatherproxy()]
# free_proxy_source = random.choice(free_proxy_sources)

# cmd="""
# x=1
# def func(self):
#     pass
# """
# class_dic={}
# exec(cmd,{},class_dic)     #exec会将cmd字符串中的代码拿出来执行一次，将产生的名字丢掉事先定义好的class_dic空字典中

# print(class_dic)
class_name='People'         #类名，是一个字符串，---------由上面的class定义类我们知道，创建类的三要素：类名，基类，类的名称空间
class_bases=(object,)       #基类，----------------------我们通过__bases__,知道基类是一个元组的形式
class_dic={}                #类的名称空间，---------------通过__dict__,知道类的名称空间的是一个字典
class_body="""              
country='China'
def __init__(self,name,age):
    self.name=name
    self.age=age

def eat(self):
    print('%s is eating' %self.name)
"""                          #--------将类体代码放到一个字符串中
exec(class_body,{},class_dic)
# print(class_dic)
class People: #People=type(...)--------默认的元类type实例化出一个对象Pelple,实例化的结果也是一个对象
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('%s is eating' %self.name)
peo=People('EGON',18)
People1=type(class_name,class_bases,class_dic)      #将事先定义好的类的三要素放到当做参数传给元类，调用元类即产生对象
print(People1)             #--------<class '__main__.People'>自定义类产生的结果
obj1=People1('egon',18)
print(People)              #--------<class '__main__.People'>，class定义类产生的结果
obj=People('egon',18)
obj1.eat()
obj.eat()
# for ip_port  in free_proxy_sources:
#     print(ip_port.get())
   # print(ip_port)
# import json,math
#
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no' : 1,
#     'name' : 'W3CSchool',
#     'url' : 'http://www.w3cschool.cn'
# }
#
# s = 'abdcf'
# a=eval('['+','.join([repr(i) for i in s])+']')
# b=','.join([str(i) for i in s])
# print('The value of PI is approximately {}.'.format(math.pi))
#
# a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
# print(type(a))
# b = eval(a)
# print(type(b))
# print(b)

