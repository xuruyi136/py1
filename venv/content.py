import re,requests,json

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9090"
response = requests.get(url,verify=False)
#将车站的名字和编码进行提取
chezhan_name = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
chezhan_code = dict(chezhan_name)
chezhan_names = dict(zip(chezhan_code.values(),chezhan_code.keys()))
# print(chezhan_names) # CQW CMW
def main():
    date = input("请输入时间(如2019-01-22)：\n")
    from_station = chezhan_code[input("请输入起始站点：\n")]
    to_station = chezhan_code[input("请输入目的站点：\n")]
    url = "https://kyfw.12306.cn/otn/leftTicket/queryA?"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    url=url+"leftTicketDTO.train_date="+date+"&leftTicketDTO.from_station="+from_station+"&leftTicketDTO.to_station="+to_station+"&purpose_codes=ADULT"
    #'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2019-09-17&leftTicketDTO.from_station=ICW&leftTicketDTO.to_station=CQW&purpose_codes=ADULT'
    print(url) #已经检查过生成的URL是正确的
    #request请求获取主页
    r = requests.get(url,headers=headers)
    html = r.text
    tab =json.loads(html)
    for i in tab['data']['result']:
        print(i)
    # r.raise_for_status()   #如果发送了一个错误的请求，会抛出异常
    # r.encoding = r.apparent_encoding
    # showTicket(r.text)
    print(r.text)
def showTicket(html):
    html = json.loads(html)
    # table = PrettyTable(["  车次  ","出发车站","到达车站","出发时间","到达时间"," 历时 ","商务座"," 一等座","二等座","高级软卧","软卧","动卧","硬卧","软座","硬座","无座","其他","备注"])
    for i in html['data']['result']:
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
        #将各项信息提取并赋值
        item = i.split('|')                                 #使用“|”进行分割
        data["station_train_code"]  = item[3]               #获取车次信息，在3号位置
        data["from_station_name"]   = item[6]               #始发站信息在6号位置
        data["to_station_name"]     = item[7]               #终点站信息在7号位置
        data["start_time"]          = item[8]               #出发时间在8号位置
        data["arrive_time"]         = item[9]               #抵达时间在9号位置
        data["lishi"]               = item[10]              #经历时间在10号位置
        data["swz_num"]             = item[32] or item[25]  #特别注意，商务座在32或25位置
        data["zy_num"]              = item[31]              #一等座信息在31号位置
        data["ze_num"]              = item[30]              #二等座信息在30号位置
        data["gr_num"]              = item[21]              #高级软卧信息在21号位置
        data["rw_num"]              = item[23]              #软卧信息在23号位置
        data["dw_num"]              = item[27]              #动卧信息在27号位置
        data["yw_num"]              = item[28]              #硬卧信息在28号位置
        data["rz_num"]              = item[24]              #软座信息在24号位置
        data["yz_num"]              = item[29]              #硬座信息在29号位置
        data["wz_num"]              = item[26]              #无座信息在26号位置
        data["qt_num"]              = item[22]              #其他信息在22号位置
        data["note_num"]            = item[1]               #备注信息在1号位置

        # color = Colored()
        # data["note_num"] = color.white(item[1])
        # #如果没有信息，那么就用“-”代替
        # for pos in name:
        #     if data[pos] == "":
        #         data[pos] = "-"
        #
        # tickets = []
        # cont = []
        # cont.append(data)
        # for x in cont:
        #     tmp = []
        #     for y in name:
        #         if y == "from_station_name":
        #             s = color.green(chezhan_names[data["from_station_name"]])
        #             tmp.append(s)
        #         elif y == "to_station_name":
        #             s = color.red(chezhan_names[data["to_station_name"]])
        #             tmp.append(s)
        #         elif y == "start_time":
        #             s = color.green(data["start_time"])
        #             tmp.append(s)
        #         elif y == "arrive_time":
        #             s = color.red(data["arrive_time"])
        #             tmp.append(s)
        #         elif y == "station_train_code":
        #             s = color.yellow(data["station_train_code"])
        #             tmp.append(s)
        #         else:
        #             tmp.append(data[y])
        #     tickets.append(tmp)
        # for ticket in tickets:
    #         table.add_row(ticket)
    # print(table)

if __name__ == '__main__':
    main()