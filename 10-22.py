# coding: utf-8
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor, Executor

import time


def spider(page):
    time.sleep(page)
    print(f"crawl task{page} finished")
    return page

with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容纳数量为5的线程池
    task1 = t.submit(spider, 1)
    task2 = t.submit(spider, 2)  # 通过submit提交执行的函数到线程池中
    task3 = t.submit(spider, 3)

    print(f"task1: {task1.done()}")  # 通过done来判断线程是否完成
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")

    time.sleep(2.5)
    print(f"task1: {task1.done()}")
    print(f"task2: {task2.done()}")
    print(f"task3: {task3.done()}")
    print(task1.result())  # 通过result来获取返回值
    print(task2.result())
    print(task3.result())

# def main():
#     with ThreadPoolExecutor(max_workers=8) as t:
#         obj_list = []
#         begin = time.time()
#         for page in range(1, 15):
#             obj = t.submit(spider, page)
#             obj_list.append(obj)
#
#         for future in as_completed(obj_list):
#             data = future.result()
#             print(data)
#             print('*' * 50)
#         times = time.time() - begin
#         print(times)