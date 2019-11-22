# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# d = expected_conditions.text_to_be_present_in_element(('name', 'tj_trnews'), '434')(driver)
# expected_conditions.text_to_be_present_in_element
# print(d)
# import re
# s = "TheLongAndWindingRoad ABC A123B45"
# print(re.sub( r"([A-Z])", r" \1", s).split())
# print(re.findall('[A-Z][^A-Z]*', 'TheLongAndWindingRoad'))

from time import time

q = input('What do you want to type? ')
a = ' '
record = []
while a != '':
    start = time()
    a = input('Type: ')
    end = time()
    v = end-start
    record.append(v)
    if a == q:
        print('Time taken to type name: {:.2f}'.format(v))
    else:
        break
for i in record:
    print('{:.2f} seconds.'.format(i))
# driver = webdriver.Chrome()
# driver.quit()
# # coding=utf-8
# '''
# Created on 2016-7-22
# @author: Jennifer
# Project:使用有道翻译测试用例
'''
# exp4 = lambda x:x+1
# print(exp4(1))
#
# list1 = [3,5,-4,-1,0,-2,-6]
# def get_abs(x):
#     return abs(x)
# sorted(list1,key=get_abs)
# print(get_abs(0.6))
# def sum(x, y):
#     return x + y
# print(sum(x=5,y=3))
#
# p = lambda x,y:x+y
# print(p(5,3))
#
# a=lambda x:x*x
# print(a(3))

# from selenium import webdriver
# import unittest, time
#
#
# class YoudaoTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
#         self.base_url = "http://www.youdao.com"
#
#     def test_youdao(self):
#         driver = self.driver
#         driver.get(self.base_url + "/")
#         driver.find_element_by_id("translateContent").clear()
#         driver.find_element_by_id("translateContent").send_keys(u"你好")
#         driver.find_element_by_id("translateContent").submit()
#         time.sleep(3)
#         page_source = driver.page_source
#         self.assertIn("hello", page_source)
#
#     def tearDown(self):
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     unittest.main()
# from urllib import parse
'''
# import requests
# data=requests.get('http://www.baidu.com')
# '''
# # 桌面编程包
# import tkinter as tk
# # 消息盒子，提示用户使用软件的方法，例如：消息对话框
# import tkinter.messagebox as msgbox
# # 控制浏览器
# import webbrowser
# # 正则表达式 过滤数据
# import re
# '''
# '''
# class App:
#     # 重写构造方法
#     def _init_(self, width=500, height=300):
#         # 定义类属性
#         self.w = width
#         self.h = height
#         self.title = 'vip视频解析助手'
#         self.root = tk.Tk(className=self.title)
#         self.url = tk.stringVar()
#         # 定义哪个播放源
#         self.v = tk.IntVar()
#         self.set(1)
#         # 软件空间划分
#         frame_1 = tk.Frame(self.root)
#         frame_2 = tk.Frame(self.root)
#         # 控件内容设置
#         group = tk.label(frame_1, text='暂时只有一个视频播放通道：', padx=10, pady=10)
#         tb = tk.Radiobutton(frame_1, text='唯一通道', variable=self.v, value=1, width=10, height=10)
#         label = tk.label(frame_2, text='请输入视频连接：')
#         entry = tk.entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
#         play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)
#         # 控件布局
#         frame_1.pack()
#         frame_2.pack()
#         # 确定位置
#         group.grid(row=0, column=0)
#         tb.grid(row=0, column=1)
#         label.grid(row=0, column=0)
#         entry.grid(row=0, column=1)
#         play.grid(row=0, column=2, ipadx=10, ipady=10)  # 按钮大小
#     # 定义播放按钮功能
#     def video_play(self):
#      # 第三方的视频解析网站地址
#         port = 'http://www.wmxz.wang/video.php?url='
#         # 使用正则表达式，判断用户输入的网址是否合法
#         if re.match(r'^https?:/{2}\w.+$', self.url.get()):
#         # 拿到用书输入的网址
#             ip =self.url.get()
#         # 对网址做解析
#             ip = parse.quote_plus(ip)
#         # 使用浏览器打开网址
#             webbrowser.open(port + ip)
#         else:
#             msgbox.showerror(title='错误', message='视频连接地址无效或无地址')
#      # 软件启动函数
#
#     def loop(self):
#         self.root.resizable(True, True)
#         self.root.mainloop()
# # 函数入口
# if __name__== "__main__":
#         app = App()
#         app.loop()