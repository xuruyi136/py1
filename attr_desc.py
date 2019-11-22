#!/usr/bin/python3
# FileName: attr_desc.py
# Author  : XuRuYi
# Date    : 2019-10-20 16:24
# IDE     : PyCharm
from datetime import date, datetime
import numbers
#属性描述符
class IntField:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise  ValueError('int value need')
        if value<0:
            raise ValueError('positive value need')
        self.value =value
    def __delete__(self, instance):
        pass
class NoDataIntField:
    #非属性描述符
    def __get__(self, instance, owner):
        return self.value
class User:
    age = IntField()

# class User:
#     def __init__(self, name, email, birthady):
#         self.name = name
#         self.email = email
#         self.birthady = birthady
#         self._age = 0
#
#     # def get_age(self):
#     #     return datetime.now().year-self.birthady.year
#     @property
#     def age(self):
#         return datetime.now().year - self.birthady.year
#
#     @age.setter
#     def age(self, value):
#         #检查是否是字符串类型
#         self.age = value


if __name__ == "__main__":
    # user = User('body', date(year=1987, month=1, day=1))
    # print('in{}file'.format(__file__))
    # user._age = 30
    # print(user._age)
    # print(user.get_age())
    # print(user.age)


    user = User()
    user.age=1
    print(user.age)