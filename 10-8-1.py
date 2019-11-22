# import os
# import time
# from io import BytesIO
# from PIL import Image
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from os import listdir
# browser = webdriver.Chrome()
# browser.set_window_size(800, 600)
# wait = WebDriverWait(browser, 20)
# browser.get('https://www.baidu.com/')
# time.sleep(2)
# screenshot = browser.get_screenshot_as_png()
# screenshot = Image.open(BytesIO(screenshot))
# browser.get_screenshot_as_file('test.png')
# print("浏览器size:", browser.get_window_size())
# print("全图size:", screenshot.size)
# browser.close()
import random
ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
# 在User-Agent列表中随机选择一个User-Agent
from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
import time
def scroll_foot(self):
    '''
    滚动条拉到底部
    :return:
    '''
    js = "var q=document.documentElement.scrollTop=10000"
    #将滚动条移动到页面的顶部
    js="var q=document.documentElement.scrollTop=0"
    return self.driver.execute_script(js)

#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    )
# path = r'C:\Users\Administrator\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# driver = webdriver.PhantomJS(path)
driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe',desired_capabilities=dcap,service_args=['--ignore-ssl-errors=true'])
# 发起url请求
url = 'https://www.baidu.com'
driver.get(url)
for i in range(1, 5):
    d=driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    print(d)
source = driver.page_source
geturl = driver.current_url
print(geturl)
driver.set_window_size(1280,800) # 分辨率 1280*800
time.sleep(1)
print(driver.title,driver.get_window_size())
# 发起请求前，可以让url表示的页面动态加载出更多的数据


# time.sleep(3)
# # 截图
# browser.save_screenshot('1.png')
#
# # 执行js代码（让滚动条向下偏移n个像素（作用：动态加载了更多的电影信息））
# js = 'document.body.scrollTop=2000'
# browser.execute_script(js)  # 该函数可以执行一组字符串形式的js代码
# time.sleep(4)
# browser.save_screenshot('2.png')
# time.sleep(2)
# content = browser.page_source
# with open('./pyJS.html', 'w', encoding='utf-8') as f:
#     f.write(content)
# 使用爬虫程序爬去当前url中的内容
driver.quit()
