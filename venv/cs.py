import requests
import json

start_num = 0  # 每一页起始数变量
count = 2  # 总计数变量
for i in range(5):
    str1 = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=2&cityId=551&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3'.format(start_num)
    start_num += 90  # 对json请求链接分析后，发现每页只有90条数据，后一页起始数等于前一页起始数加90
    response = requests.get(str1)  # 第一个页面的json请求链接
    json_str = response.text
    json_dict = json.loads(json_str)
    results = json_dict['data']['results']
    for item_dict in results:
        company = item_dict['company']['name']
        job_name = item_dict['jobName']
        # job_type = item_dict['jobType']
        job_type = json_dict.get('data').get('results')[0].get('jobType').get('items')[0].get('name')
        salary = item_dict['salary']
        city = item_dict['city']['display']
        edu = item_dict['eduLevel']['name']
        workingExp = item_dict['workingExp']['name']
        welfare = '、'.join(item_dict['welfare'])  # '、'.join()：使用、字符将列表中的每一个元素拼接起来，得到一个字符串
        count += 1
        print('公司名称：{}  招聘职位：{}  职位类型：{}  薪资：{}  城市：{}  学历要求：{}  工作经验：{}  福利待遇：{}'.format(company, job_name, job_type, salary, city, edu, workingExp, welfare))

print('共', count, '条数据')


