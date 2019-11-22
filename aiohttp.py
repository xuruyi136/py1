# import asyncio,aiohttp

# async def fetch_async(url):
#     print(url)
#     async with aiohttp.request("GET",url) as r:
#         # 或者直接await r.read()不编码，直接读取，适合于图像等无法编码文件
#         reponse = await r.text(encoding="utf-8")
#         print(reponse)
#
# tasks = [fetch_async('http://www.baidu.com/'), fetch_async('http://www.chouti.com/')]
#
# event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
# event_loop.close()
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import asyncio,time
# import multiprocessing
# multiprocessing
# async def do_some_work(x):  # 使用async关键字定义协程
#     print('Waiting: ', x)
#
# coroutine = do_some_work(2)  # 创建协程对象
# loop = asyncio.get_event_loop()  # 创建一个事件循环（池）
# loop.run_until_complete(coroutine)
# _now = lambda : time.time()
# print(_now())


from multiprocessing import Pool,Queue,Manager
import os
def run_proc(name,q):
    print('Run Child process %s (%s)' % (name, os.getpid()))
    q.put('value')
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    q = Queue()
    p = Pool(2)
    L = [1,2]
for l in L:
    p.apply_async(run_proc,args=(l,q))
    print('Child Process will start')
    p.close()
    p.join()
    print('Child process end.')
    print(q.get())


