#!/usr/bin/python3
# FileName: property.py
# Author  : XuRuYi
# Date    : 2019-10-20 16:05
# IDE     : PyCharm
#动态属性
from datetime import date, datetime


class User:
    def __init__(self, name, birthady):
        self.name = name
        self.birthady = birthady
        self._age=0
    #
    # def get_age(self):
    #     return datetime.now().year-self.birthady.year
    @property
    def age(self):
        return datetime.now().year-self.birthady.year

    @age.setter
    def age(self,value):
        self.age=value


if __name__ == "__main__":
    user = User('body', date(year=1987, month=1, day=1))
    print('in{}file'.format(__file__))
    user._age=30
    print(user._age)
    # print(user.get_age())
    print(user.age)