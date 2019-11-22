# if __name__ == '__main__':
#     import time
#     print (time.ctime(time.time()))
#     print (time.asctime(time.localtime(time.time())))
#     print (time.asctime(time.gmtime(time.time())))
# import re
#
# pattern = re.compile(r'[^a-zA-Z0-9]+')  # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123go的ogle456')
#
# print(result1)
# print(result2)
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simfang.ttf", size=14)

# beijing = [17,17,23,43]
# shanghai = ['19%','4%','23%','54%']
# guangzhou = ['53%','25%','13%','9%']
# shenzhen = ['41%','22%','20%','17%']
#
# label = ['2-3 years','3-4 years','4-5 years','5+ years']
# color = ['red','green','yellow','purple']
#
# indic = []
#
# #我们将数据最大的突出显示
# for value in beijing:
#     if value == max(beijing):
#         indic.append(0.1)
#     else:
#         indic.append(0)
#
# plt.pie(
#     beijing,
#     labels=label,
#     colors=color,
#     startangle=90,
#     shadow=True,
#     explode=tuple(indic),#tuple方法用于将列表转化为元组
#     autopct='%1.1f%%'#是数字1，不是l
# )
#
# plt.title(u'饼图示例——统计北京程序员工龄', FontProperties=font)
# plt.show()

#coding:utf-8

import json
import requests


class LagoupositionSpider():
    name = "LagouPosition"
    totalPageCount = 1
    curpage = 1
    cur = 0
    myurl = 'http://www.lagou.com/jobs/positionAjax.json?'

    headers = {'Cookie':'JSESSIONID=2FC28971BBE032152E26B3EDC53E5856; user_trace_token=20170426193638-4a8fe6d996f3492492303a4d78b079b4; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20170426193639-9caaa97f-2a74-11e7-8138-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; TG-TRACK-CODE=index_search; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1493206604; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1493206703; _ga=GA1.2.736962990.1493206603; LGSID=20170426193639-9caaa76a-2a74-11e7-8138-525400f775ce; LGRID=20170426193818-d7ae7795-2a74-11e7-b3b0-5254005c3644; SEARCH_ID=88bbbc48ca4448218bea2cd41926b5c6','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    city = '杭州'
    kds = ['Python工程师','大数据', '云计算', 'docker', '中间件', 'Node.js', '数据挖掘',
           '自然语言处理', '搜索算法', '精准推荐', '全栈工程师', '图像处理','机器学习', u'语音识别']
    kd = kds[0]

    def start_requests(self):
        post_data = {'first': 'false', 'pn': self.curpage, 'kd': self.kd}
        html = requests.post(self.myurl, data=json.dumps(post_data), headers=self.headers)
        html_text = html.text
        print(html_text)
        return html_text

    def get_result(self):
        result = self.start_requests()
        jdict = json.loads(result)
        jcontent = jdict['content']
        jposresult = jcontent['positionResult']
        jresult = jposresult['result']
        totalPageCount = jposresult['totalCount'] / 15 + 1
        for each in jresult:
            positionName = each['positionName'].encode('gbk')
            companyFullName = each['companyFullName'].encode('gbk')
            workyear = each['workYear'].encode('gbk')
            salary = each['salary'].encode('gbk')
            district = self.city.decode('utf-8').encode('gbk')
            with open('F:\python.csv', 'ab+') as f:
                f.write('%s,%s,%s,%s,%s\n' % (positionName,district,companyFullName,workyear,salary))

    def parse(self):
        if self.curpage <= self.totalPageCount:
            self.curpage += 1
            self.start_requests()
            self.get_result()

if __name__ == '__main__':
    lagouspider = LagoupositionSpider()
    lagouspider.parse()