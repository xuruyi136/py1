li = [1, 4, 5, 6, 7, 9, 11, 14, 16]
# print(li[-4:-2])

li = [1, 2, 3, 4]
# print(li[:0])
dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A0 = dict(zip((1,2,3,4,5),('a','b','c','d','e')))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
# print(A6)


import time
import datetime
t = time.time()
# print (t)            #原始时间数据
# print (int(t))         #秒级时间戳
# print (round(t * 1000))  #毫秒级时间戳
# print (int(round(t * 1000000))) #微秒级时间戳


ts = int(round(t * 1000000))
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(round(ts/1000000))))
print(dt)

import json

student={
    "name":"liuming",
    "age":18,
    "mobile":"15847562589"
}

# print(student)
# for i in student.items():
#     print(i[0])
# stu_json = json.dumps(student)
# print(stu_json)
# print("JSON对象：{0}".format(stu_json))
# stu_dict = json.loads(stu_json)
# print(stu_dict)

def func_01():
    x=5
    def func_02():
         nonlocal x
         x *= x
         return x
    func_02()
    print(x)
func_01()

def test() -> [1, 2, 3, 4, 5]:
    pass
print(test.__annotations__)

