# import os
# list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# tuple1=tuple(list1)
# print(list1)
# print(tuple1)
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(type(baske
# !/usr/bin/python3


# -*- coding: UTF-8 -*-
# Filename : test.py
# author by : www.runoob.com

# Python 斐波那契数列实现

# 获取用户输入数据
# nterms = int(input("你需要几项？"))
#
# # 第一和第二项
# n1 = 0
# n2 = 1
# count = 2
#
# # 判断输入的值是否合法
# if nterms <= 0:
#     print("请输入一个正整数。")
# elif nterms == 1:
#     print("斐波那契数列：")
#     print(n1)
# else:
#     print("斐波那契数列：")
#     print(n1, ",", n2, end=" , ")
#     while count < nterms:
#         nth = n1 + n2
#         print(nth, end=" , ")
#         # 更新值
#         n1 = n2
#         n2 = nth
#         count += 1

# url = "xxxxx"
# str000='/home/aqonvs.jpg'
# newname = str000.split('/')
# print (newname[len(newname)-1])
# files = {'file':(newname,open('/home/aqonvs.jpg','rb'),'image/jpg')}

# import urllib.request
# keyworld="渴望飞的鱼"
# key=urllib.request.quote(keyworld)
# url="https://www.baidu.com/s?wd="+key
# print(url)
# req=urllib.request.Request(url)
# data=urllib.request.urlopen(req).read()
# fhandle=open('D:/爬虫/抓取文件/2018110205.html','wb')
# fhandle.write(data)

#python 火车票信息的查询
import requests,re,json
from prettytable import PrettyTable
from colorama import init,Fore
# from content import chezhan_code,chezhan_names
# self.browser = browser
session = requests.session()
# pictor = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
# verify_url = 'http://littlebigluo.qicp.net:47720/'  # 验证码识别网址，返回识别结果
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Referer': 'http://littlebigluo.qicp.net:47720/'
}
url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9110"
response = requests.get(url,verify=False)
#将车站的名字和编码进行提取
chezhan_name = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
chezhan_code = dict(chezhan_name)
chezhan_names = dict(zip(chezhan_code.values(),chezhan_code.keys()))

class Colored(object):
    def yeah(self,s):
        return Fore.LIGHTCYAN_EX + s + Fore.RESET
    def green(self,s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET
    def yellow(self,s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET
    def white(self,s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET
    def blue(self,s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

# txt=requests.get(url).text
# inf=txt[:-2].split("@")[1:]
# stations={}
# for record in inf:
#     rlist=record.split("|")
#     stations[rlist[2]]={"cn":rlist[1],"qp":rlist[3],"jp":rlist[4]}  #把车站编码当作key
# print(stations)
# def getcode(t):
#     while True:
#         s1=input("%s站:"%t)
#         r1=[]
#         for id,station in stations.items():
#             if s1 in station.values():
#                 r1.append((id,station))
#         if r1:
#             break
#         print("没有这个车站。")
#         print("请重新输入。")
#     if len(r1)==1:
#         sid=r1[0][0]
#     else:
#         print("你需要在以下车站里选择:")
#         for i in range(len(r1)):
#             print(i+1,r1[i][1]["cn"])
#         sel=int(input("你的选择是:"))-1
#         sid=r1[sel][0]
#     return sid
fromstation=chezhan_code[input("请输入起始站点：\n")]
tostation=chezhan_code[input("请输入目的站点：\n")]
chufatime=input("请输入时间(如2019-01-22)：\n")

url='https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(chufatime,fromstation,tostation)
print(url)
html=requests.get(url,headers=headers).content
ai = json.loads(html)
table = PrettyTable(
        ["  车次  ", "出发车站", "到达车站", "出发时间", "到达时间", " 历时 ", "商务座", " 一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座",
         "无座", "其他", "备注"])
result=[]
for i in ai['data']['result']:
    name = [
        "station_train_code",
        "from_station_name",
        "to_station_name",
        "start_time",
        "arrive_time",
        "lishi",
        "swz_num",
        "zy_num",
        "ze_num",
        "dw_num",
        "gr_num",
        "rw_num",
        "yw_num",
        "rz_num",
        "yz_num",
        "wz_num",
        "qt_num",
        "note_num"
    ]
    data = {
        "station_train_code": '',
        "from_station_name": '',
        "to_station_name": '',
        "start_time": '',
        "arrive_time": '',
        "lishi": '',
        "swz_num": '',
        "zy_num": '',
        "ze_num": '',
        "dw_num": '',
        "gr_num": '',
        "rw_num": '',
        "yw_num": '',
        "rz_num": '',
        "yz_num": '',
        "wz_num": '',
        "qt_num": '',
        "note_num": ''
    }
    # 将各项信息提取并赋值
    item = i.split('|')  # 使用“|”进行分割
    data["station_train_code"] = item[3]  # 获取车次信息，在3号位置
    data["from_station_name"] = item[6]  # 始发站信息在6号位置
    data["to_station_name"] = item[7]  # 终点站信息在7号位置
    data["start_time"] = item[8]  # 出发时间在8号位置
    data["arrive_time"] = item[9]  # 抵达时间在9号位置
    data["lishi"] = item[10]  # 经历时间在10号位置
    data["swz_num"] = item[32] or item[25]  # 特别注意，商务座在32或25位置
    data["zy_num"] = item[31]  # 一等座信息在31号位置
    data["ze_num"] = item[30]  # 二等座信息在30号位置
    data["gr_num"] = item[21]  # 高级软卧信息在21号位置
    data["rw_num"] = item[23]  # 软卧信息在23号位置
    data["dw_num"] = item[27]  # 动卧信息在27号位置
    data["yw_num"] = item[28]  # 硬卧信息在28号位置
    data["rz_num"] = item[24]  # 软座信息在24号位置
    data["yz_num"] = item[29]  # 硬座信息在29号位置
    data["wz_num"] = item[26]  # 无座信息在26号位置
    data["qt_num"] = item[22]  # 其他信息在22号位置
    data["note_num"] = item[1]  # 备注信息在1号位置

    color = Colored()
    data["note_num"] = color.white(item[1])
    # 如果没有信息，那么就用“-”代替
    for pos in name:
        if data[pos] == "":
            data[pos] = "-"
    tickets = []
    cont = []
    cont.append(data)
    for x in cont:
        tmp = []
        for y in name:
            if y == "from_station_name":
                s = color.green(chezhan_names[data["from_station_name"]])
                tmp.append(s)
            elif y == "to_station_name":
                s = color.yeah(chezhan_names[data["to_station_name"]])
                tmp.append(s)
            elif y == "start_time":
                s = color.green(data["start_time"])
                tmp.append(s)
            elif y == "arrive_time":
                s = color.yeah(data["arrive_time"])
                tmp.append(s)
            elif y == "station_train_code":
                s = color.yellow(data["station_train_code"])
                tmp.append(s)
            else:
                tmp.append(data[y])
        tickets.append(tmp)
    for ticket in tickets:
        table.add_row(ticket)
print(table)

