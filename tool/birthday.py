# coding=utf-8
from time import *
import sys
import requests
import json
import random
import datetime

def generator(y,m,d):
    codelist = []
    with open(r'D:\TS_apiTest\tool\idno.txt', mode="r", encoding="utf-8") as file:
        codelist = file.readlines()

    id = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]  # 地区项
    id = id + str(y)
    id = id + str(m) + str(d)
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode ={'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5',
                '8': '5', '9': '3', '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
       count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count%11)]  # 算出校验码
    print (id)
    return id


def dingTalk(msg):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": "腾顺--%s" % msg
        },
        "at": {
            "atMobiles": [],
            "isAtAll": "false"
        }
    }
    json_data = json.dumps(data)
    requests.post(
        url='https://oapi.dingtalk.com/robot/send?access_token=0d4a6061efd77b130f6d28d5984ed55a4ac3e7b9357197d32c1001acff7054da',
        data=json_data, headers=headers)

def age(xAge,dAge,d,m,y):
    a = gmtime()
    # difference in day
    xd = int(d) +1
    xm = int(m)
    xy = int(y) - int(dAge) -1
    if xd==32 and xm==12:
        xm = 1
        xd = 1
        xy = int(y) - int(dAge) - 1

    # 最大出生日期
    dd = int(d)
    # difference in month
    dm = int(m)
    # difference in year
    dy = int(y) - int(xAge)
    xd_1=d
    dd_1=int(d)+1

    if len(str(dd_1))==1:
        dd_1=str(0)+str(dd_1)
    if len(str(xd_1))==1:
        xd_1=str(0)+str(xd_1)

    if len(str(dm))==1:
        dm=str(0)+str(dm)
    if len(str(dd))==1:
        dd=str(0)+str(dd)
    if len(str(xm))==1:
        xm=str(0)+str(xm)
    if len(str(xd))==1:
        xd=str(0)+str(xd)



    minIdNo=generator(str(xy),xm,xd)
    minIdNo_1=generator(str(xy),str(xm),str(xd_1))
    maxIdNo=generator(str(dy),str(dm),str(dd))
    maxIdNo_1=generator(str(dy),str(dm),str(dd_1))
    result=u"保险符合要求的年龄区间：%s岁-%s岁,今天是 %s-%s-%s ,\r\n符合要求的出生日期： %d-%s-%s 至 %d-%s-%s"%(xAge,dAge,y,m,d,xy, xm, xd, dy, dm, dd)+"\r\n符合条件的身份证号：\r\n%s\r\n%s\r\n不符合条件的身份证号：\r\n%s\r\n%s"%(minIdNo,maxIdNo,minIdNo_1,maxIdNo_1)

    # print(result+"符合条件的身份证号为：%s;%s,\r\n不符合条件的为：%s;%s"%(minIdNo,maxIdNo,minIdNo_1,maxIdNo_1))
    print(result)
    # print(u"保险允许的年龄区间：%s--%s,今天是 %s-%s-%s"%(xAge,dAge,y,m,d))
    # print(u"允许的出生日期: %d-%s-%s 至 %d-%s-%s" % (xy, xm, xd, dy, dm, dd))

    dingTalk(result)




if __name__ == '__main__':
    age(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])





