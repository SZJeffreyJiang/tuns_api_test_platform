#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author tom
import requests
import json

def dingTalk():
    headers={
        "Content-Type": "application/json"
            }
    data={
    "actionCard": {
        "title": "jenkins构建", 
        "text": "![screenshot](@lADOpwk3K80C0M0FoA) ### 乔布斯 20 年前想打造的苹果咖啡厅 Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划jenkins", 
        "hideAvatar": "0", 
        "btnOrientation": "0", 
        "singleTitle" : "阅读全文",
        "singleURL" : "https://www.dingtalk.com/"
    }, 
    "msgtype": "actionCard"
}
          
    json_data=json.dumps(data)
    requests.post(url='https://oapi.dingtalk.com/robot/send?access_token=fc190bc0fd1d0030ffac5d1cf66b476216543a51228281d7151991c0dca76ca8',data=json_data,headers=headers)
