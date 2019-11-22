# from __future__ import print_function
# import time
# import gevent

# start = time.time()
# for _ in range(4):
#     pool.spawn(time.sleep, 1)
# gevent.wait()
# delay = time.time() - start
# print('Running "time.sleep(1)" 4 times with 3 threads. Should take about 2 seconds: %.3fs' % delay)
# # print(help(gevent))
# words = ['China','America','England']
# url_base='http:baidu'
#
# import gevent
# from gevent.lock import Semaphore
# sem = Semaphore(1)
# def f1():
#     for i in range(5):
#         sem.acquire()
#         print ('run f1, this is ', i)
#         sem.release()
#         gevent.sleep(1)
#
#
# def f2():
#     for i in range(5):
#         sem.acquire()
#         print ('run f2, that is ', i)
#         sem.release()
#         gevent.sleep(0.3)
#

#!/usr/bin/python
#!/usr/bin/python


from concurrent.futures import ProcessPoolExecutor
import os
from math import *
import time
import threading
import pymysql
str1 = '\u4f60\u597d\u4e16\u754c'
str2 = U'\u4f60\u597d\u4e16\u754c'
print(str1)
print(str2)

# import pymongo
# client = pymongo.MongoClient('192.168.43.128', 27017)    # 连接服务器，需要先开启服务
# db = client['mydb']  # 选择数据库
#
# data = db["images"].find().limit(1)   # 集合名
# for i in data:
#     print(i)
#
import redis
redb = redis.StrictRedis(host='127.0.0.1', port=6379, password=None, decode_responses=True)
# redb.set('mylist','11111')
redb.hset('apple', 'apple', '苹果');
s=redb.hvals('accounts:weibo')  #name
# redb.zadd('proxies',{'11111111':10})
print(redb.type('mylist')) #判断类型
print(s)

# https://www.jianshu.com/p/274c6a140303
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='123456',
#     database='mysql',
#     port=3306,
#     charset='utf8')
# cursor = conn.cursor()
# cursor.execute('select Host,User,File_priv from user')
# results = cursor.fetchall()
# print('编号\t\t\t名称\t\t所在地')
# for dept in results:
#     print(dept[0], end='\t')
#     print(dept[1], end='\t')
#     print(dept[2])
# conn.close()




# program = 'a = 5\nb=10\nprint("Sum =", a+b)'
# exec(program)
# exec('print(dir())')
# exec('print(dir())')
#
# exec('print(dir())', {'__builtins__': None}, {'print': print, 'dir': dir})
# globalsParameter = {'__builtins__': None, 'print': print, 'dir': dir}
# exec('print(dir())', globalsParameter)

#
# def print_hello(n):
#     print("I'm number {} say hello in pid {}".format(n, os.getpid()))

# print(print_hello(1))
# map(func, *iterables, timeout=None, chunksize=1)
# if __name__=='__main__':
#     with ProcessPoolExecutor(max_workers=10) as executor:
#         executor.map(print_hello, range(10))

# print(list(map(lambda x , y : x + y, [2,4,6],[3,2,1])))
# print(list (map(int, {1:2,2:3,3:4})))
# print(list(map(lambda x , y : x ** y, [2,4,6],[3,2,1])))
# print(list(map(lambda x: x * x, range(10))))


# arr = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y : x+y, arr))


import random
print(random.randint(1,10))
print(os.path.dirname(os.path.dirname(__file__)))