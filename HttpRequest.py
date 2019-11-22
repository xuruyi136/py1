import requests
import abc

'''
请求方法抽象类
'''


class AbsMethod:

    @abc.abstractmethod
    def request(self, url, attach):
        pass


'''
Get 方法
'''


class Get(AbsMethod):
    '''
    请求
    '''

    def request(self, url, attach) -> requests.Response:
        res = requests.post(url, attach)
        if not res.ok:
            return res.raise_for_status()
        return res


'''
Post 方法
'''


class Post(AbsMethod):
    '''
    请求
    '''

    def request(self, url, attach) -> requests.Response:
        res = requests.get(url, attach)
        if not res.ok:
            return res.raise_for_status()
        return res


'''
方法工厂
'''


class MethodFactory:
    def create(self, method: str) -> AbsMethod:
        return eval(method)()


'''
http 请求
'''


class HttpReuqest:

    '''
    发送求请
    '''
    @staticmethod
    def send(url, attach = {}, method='Get') -> requests.Response:
        factory = MethodFactory()
        target = factory.create(method)
        return target.request(url, attach)

from typing import List, Tuple, Dict
def add(a:int, string:str, f:float, b:bool) -> Tuple[List, Tuple, Dict, bool]:
    list1 = list(range(a))
    tup = (string, string, string)
    d = {"a":f}
    bl = b
    return list1, tup, d,bl
print(add(5,"hhhh", 2.3, False))
from typing import List
def func(a, string):
    list1 = []
    list1.append(a)
    list1.append(string)
    return list1
    print(list1)

