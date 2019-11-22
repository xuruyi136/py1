#str 对象和 bytes 对象可以使用 .encode() (str -> bytes) 或 .decode() (bytes -> str)方法相互转化
# b = b'china'
# s = b.decode()
# print(s)
# b1 =s.encode()
# print(b1)
# #map、filter（序列过滤）、reduce 用法  操作list

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def f(x):
#     return x*x
# data = list(range(10))
# print(list(map(f, b)))
# print(list(map(lambda x: x * x, data)))
# print(list(filter(lambda x:x %2 ==0, range(10))))
# def f(s):
#     return s[0:1].upper() + s[1:].lower()
# list_ = ['lll', 'lKK', 'wXy']
# a = map(f, list_)
# print(list(a))

# from functools import reduce
# arr = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y : x+y, arr))
#生成器
# def count(n):
#     while n > 0:
#         yield n     # 生成值: n
#         n-=1
# c = count(5)
# print(c.__next__())
#
# def mygenerator():
#     print('start...')
#     yield 5
# print(mygenerator().__next__())
#用yield实现斐波那契数列
# def fibonacci():
#   a=b=1
#   yield a
#   yield b
#   while True:
#     a,b = b,a+b
#     yield b
# for num in fibonacci():
#   if num > 100:
#     break
#   print (num)
from distutils import dist
import time,sys
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
myD = {1: 'a', 2: 'b'}
for key, value in myD.items():
    print(key, value)
i = ['a', 'b']
l = [1, 2]
print (dict([i,l]))
print("Python版本号：",sys.version)
# captcha_result={'err_no': 0, 'err_str': 'OK', 'pic_id': '3080816373051500004', 'pic_str': '56,72|187,68', 'md5': '8a73f928be9f0e38cb112144262282b3'}
# locations = captcha_result.get('pic_str').split('|')
# print(type(locations))
# for location in captcha_result.items():
#     print(location)
