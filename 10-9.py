import threading
import time

# def add(x,y):
#     print('{}+{}={}'.format(x,y,x+y))
#
# t1 = threading.Thread(target=add,name='1',args=(4,5))
# t1.start()
# time.sleep(2)
#
# t2 = threading.Thread(target=add,name = '2',args=(4,),kwargs={'y':6})
# t2.start()
# time.sleep(2)
#
# t3 = threading.Thread(target=add,name='3',kwargs={'x':4,'y':7})
# t3.start()
# def showinfo():
#
#     print('currentthread = {}'.format(threading.current_thread()))
#
#     print('main thread = {}'.format(threading.main_thread()))
#
#     print('active count = {}'.format(threading.active_count()))
# showinfo()


# import logging
#
# FORMAT = '%(asctime)s %(threadName)s %(thread)d %(message)s'
# logging.basicConfig(format=FORMAT,level=logging.INFO)
#
#
# cups = []
# def worker(count=10):
#     logging.info('i am work')
#     while len(cups) < count:
#         time.sleep(0.1)
#         cups.append(1)
#     logging.info('i am finsh.cups={}'.format(len(cups)))
#
# for _ in range(10):
#
#     threading.Thread(target=worker,args=(1000,)).start()

# import time, threading
#
# X = 'abc'
# ctx = threading.local()
# ctx.x = 123  # 主线程中定义x本地属性
# print(ctx)
# print( type(ctx))
#
#

# def work():
#     print(X)
#
#     # print(ctx.x)  # 子线程访问不到
#     print('Good job')
#
#
# threading.Thread(target=work).start()
# for item in range(10):
#   print('\033[40;35;46m {} \033[1m'.format(item), end='')

# 蓝色背景
def blue_print(*s, end='\n'):
    for item in s:
        print('\033[46m {} \033[0m'.format(item), end='')
    print(end=end)

# 高亮，绿色字体，红色背景
def green_print(*s, end='\n'):
    # print('\033[1m {} \033[0m'.format(s), end=end)
    for item in s:
        print('\033[1;32;41m {} \033[0m'.format(item), end='')
    print(end=end)

import sys
# if __name__ == '__main__':
#     # blue_print('asdf 1234')
#     # print('-' * 30)
#     blue_print(123, 'asdf')
#     green_print('adsf')
#     print(file=sys.stdout, sep=' ', end='\n')


import jedi,inspect,howdoi,geopy
from collections import OrderedDict,Counter
x=OrderedDict(a=1,b=2)
y=Counter("hw")
# print(inspect.getsource(inspect.getsource))
# print(inspect.getsource(inspect.getmodule))
print(inspect.currentframe().f_lineno)
print(sys.getsizeof(30))

s='progr  is  awesoem'
print(s.title())
from math import ceil
def chunk(lst,size):
    return list(
        map(lambda x:lst[x*size:x*size+size],list(range(0,ceil(len(lst)/size))))
    )
# print(chunk([1,2,3,4,5],2))
def compact(lst):
    return list(filter(bool,lst))
# print(compact([0,1,False,2,3, 'a' ,'s' ,34]))
# 转换一个二维数组
array=[['a','b'],['c','d'],['e','f']]
transposed=zip(*array)
for i in transposed:
    print(i)
import re
def decapitalize(string):
    return string[:1].lower()+string[1:]
print(decapitalize('FooBar'))
d={'a':1,'b':2}
# print(d.get('c',3))
def spread(arg):
    ret=[]
    for i in arg:
        if isinstance(i,list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
def flatten(lst):
    return  [x for y in lst for x in y]
print(flatten([[1,2,3],[4,5,6]]))
# print(spread([1,2,3,[4,5,6],[7],8,9]))
from copy import deepcopy
from random import randint
def shuffle(lst):
    temp_lst=deepcopy(lst)
    m=len(temp_lst)
    while(m):
        m-=1
        i=randint(0,m)
        temp_lst[m],temp_lst[i]=temp_lst[i],temp_lst[m]
    return temp_lst
foo =[1,2,3]
# print(shuffle(foo))
import operator
action ={
    '+':operator.add,
    '-':operator.sub,
    '*':operator.truediv,
    '/':operator.mul,
    '**':pow
}
# print(action['**'](50,25))

def to_dictionary(keys,values):
    return  dict(zip(keys,values))
keys=['a','b','c']
values=[2,3,4]
# print(to_dictionary(keys,values))

def merge_dictionaries(a,b):
    return {**a,**b}
a={'x':1,'y':2}
b={'y':3,'z':4}
# print(merge_dictionaries(a,b))

def merge_two_dicts(a,b):
    c=a.copy()
    c.update(b)
    return c
a={'x':1,'y':2}
b={'y':3,'z':4}
# print(merge_two_dicts(a,b))

# def difference(a,b):
#     set_a=set(a)
#     set_b=set(b)
#     comparison=set_a.difference(set_b)
#     return list(comparison)
def difference(a,b):
    _b=set(b)
    return [item for item in a if item not in _b]

print(difference([1,2,3],[1,2,4]))
import os
# print(sorted(sys.modules.keys()))
# print(dir(os))

from urllib.parse import urlencode
heardes ={
    '1':'3',
    'dfsdf':'dfsdf',
    'sfsdf':'dfsdf',
}
print(sys.path)
print(urlencode(heardes))
#C:\Users\Administrator\Envs
