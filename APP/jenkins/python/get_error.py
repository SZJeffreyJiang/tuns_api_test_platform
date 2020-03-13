import json
import requests

path = r'D:\TS_apiTest\APP\jenkins\errorLog\APP_api_testreport_error.txt'
error=[]
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        value = line[:-1] #去掉换行符
        error.append(value)
print(len(error))
print(error)
f.close()




def sendmessage(errorName,message):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=f289df0f42041ef96006c1f59196ac0945fb6cf1b6f3be42f7f409f8f31d73df'  # TS
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=fc190bc0fd1d0030ffac5d1cf66b476216543a51228281d7151991c0dca76ca8'  # 测试
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=e54fca8930f64e3ac7a01b564e68351938984f04be38d1bcf843c93ab340b9a6'  # 卢瑟测试
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    message = message
    if message == "0":
        msg='nice！生产环境APP接口测试构建完成，本次自动化测试没有发现异常！'
        phone=''
    else:
        msg='后台异常！！！生产环境APP接口测试构建完成，本次自动化测试有'+errorName+'共计'+message+'条用例异常，请下载报告分析'
        phone='+86-15096003642'
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": msg},
        "at": {
            "atMobiles": [phone]  # 如果需要@某人，这里写他的手机号
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)



if __name__ == '__main__':
    sendmessage(str(error),str(len(error)))

