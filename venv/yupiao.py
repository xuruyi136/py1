#1.1 现有字典 dict={‘a’:24，‘g’:52，‘i’:12，‘k’:33}请按字典中的 value 值进行排序？
dict={'a':'24','g':'52','i':'12','k':'33'}
print(sorted(dict.items(),key=lambda x:x[1]))
#请反转字符串“sStr”
print("sStr"[::-1])
# 将字符串”k:1|k1:2|k2:3|k3:4”，处理成Python字典：{k:1， k1:2， … } # 字 典里的K作为字符串处理
str1 = "k:1|k1:2|k2:3|k3:4"
def srt2dict(str1):
    dict={}
    for items in str1.split("|"):
        k,v=items.split(":")
        dict[k]=v
    return dict
print(srt2dict(str1))
#请按alist中元素的age由大到小排序
alist=[{'name':'a','age':10},{'name':'b','age':20},{'name':'c','age':30}]
# alist=[{'name':'a','age':10},{'name':'b','age':20},{'name':'c','age':30}]
def sort_by_age(alist):
    return sorted(alist,key=lambda x:x["age"],reverse=True)
print(sort_by_age(alist))
#写一个列表生成式，产生一个公差为11的等差数列
print([x*11 for x in range(10)])
#给定两个列表，怎么找出他们相同的元素和不同的元素?
list1 = [1,2,3]
list2 = [3,4,5]
set1 = set(list1)
set2 = set(list2)
print(set1&set2)
print(set1^set2)
#请写出一段Python代码实现删除一个list里面的重复元素?
l1 = ['b','c','d','b','c','a','a']
print(list(set(l1)))
#如果想要保持他们原来的排序：用list类的sort方法：

l1 = ['b','c','d','b','c','a','a']
# print(list(set(l1)))
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)
#也可以这样写：
l1 = ['b','c','d','b','c','a','a']
l2 = sorted(set(l1),key=l1.index)
print(l2)
#也可以使用遍历：
l1 = ['b','c','d','b','c','a','a']
l2 = []
for i in l1:
    if not i in l2:
        l2.append(i)
print(l2)
#新的默认列表只在函数被定义的那一刻创建一次。当extendList被没有指定特定参数list调用时，这组list的值
#随后将被使用。这是因为带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。
def extendlist(val, list=[]):
    list.append(val)
    return list
list1 = extendlist(10)
list2 = extendlist(123, [])
list3 = extendlist('a')
print("list1 = %s" %list1)
print("list2 = %s" %list2)
print("list3 = %s" %list3)
#获取1~100被7整除的偶数？
def A():
    L=[]
    for i in range(1,100):
        if i%7==0:
            L.append(i)
    return L
print(A())

#快速去除列表中的重复元素

# In [4]: a = [11,22,33,33,44,22,55]
# In [5]: set(a)
# Out[5]: {11, 22, 33, 44, 55}
#交集：共有的部分

a = {71,72,73,74,75}
b = {72,74,75,76,77}
a&b
#{72, 74, 75}
#并集：总共的部分

a = {21,22,23,24,25}
b = {22,24,25,26,27}
a | b
#{21, 22, 23, 24, 25, 26, 27}
#差集：另一个集合中没有的部分

a = {51,52,53,54,55}
b = {52,54,55,56,57}
b - a
#{66, 77}
#对称差集(在a或b中，但不会同时出现在二者中)

a = {91,92,93,94,95}
b = {92,94,95,96,97}
a ^ b
#{11, 33, 66, 77}