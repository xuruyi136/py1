# import requests,json
# url = 'https://www.lagou.com/jobs/positionAjax.json'
# data = {
#     'first': 'true',
#     'pn': '1',
#     'kd': 'python'
# }
# headers ={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
#     'Accept': 'application/json, text/javascript, */*; q=0.01'
# }
# response = requests.post(url=url,data=data,headers=headers)
# json_str = response.text
# # json_dict = json.loads(json_str)
# # res = requests.get('https://www.lagou.com/gongsi/0-1-0-0.json', headers=headers, data=form_data,proxies=get_ip())
# # print(res.text)
# print(json_str)
# # for item_dict in json_dict:
#     # name = item_dict.get('contect')[1]
#     # print(name)
import requests
import time
import json

def main(pages):
    # 主url'https://www.lagou.com/jobs/list_python?city=%E9%87%8D%E5%BA%86&cl=false&fromSearch=true&labelWords=&suginput='
    url1 = 'https://www.lagou.com/jobs/list_python?city=%E9%87%8D%E5%BA%86&cl=false&fromSearch=true&labelWords=&suginput='
    # ajax请求
    url = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false"
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://www.lagou.com/jobs/list_python?px=default&city=%E9%87%8D%E5%BA%86',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Host': 'www.lagou.com'
    }
    # 通过data来控制翻页

    for page in range(1, pages):
        data = {
            'first': 'false',
            'pn': page,
            'kd': 'python'
        }
        #获取cookice的消息
        s = requests.Session()  # 建立session

        s.get(url=url1, headers=headers, timeout=3)
        cookie = s.cookies  # 获取cookie
        # print(cookie)
        respon = s.post(url=url, headers=headers, data=data, cookies=cookie, timeout=3)
        # print(respon)
        # print(respon.text)
        time.sleep(7)
        # print(respon.content.decode())
        json_data = json.loads(respon.text)

        for i in range(len(json_data['content']['positionResult']['result'])):
            ret = {}
            ret['岗位名称'] = json_data['content']['positionResult']['result'][i]['positionName']
            ret['工资'] = json_data['content']['positionResult']['result'][i]['salary']
            ret['城市'] = json_data['content']['positionResult']['result'][i]['city']
            ret['工作类型'] = json_data['content']['positionResult']['result'][i]['jobNature']
            ret['公司特点'] = json_data['content']['positionResult']['result'][i]['positionAdvantage']
            ret['地区'] = json_data['content']['positionResult']['result'][i]['district']
            ret['发布时间'] = json_data['content']['positionResult']['result'][i]['createTime']
            print(ret)

        #     with open('工作1.json', 'a',encoding="utf-8")as f:
        #         f.write(json.dumps(ret, ensure_ascii=False)+',\n')
main(2)
