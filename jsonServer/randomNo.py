#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

def write_file(no):
    """ 文件写入"""
    file_name = "db-1.json"
    # 以写入的方式打开
    f = open(file_name,'w')
    no=no
    # 写入内容
    # f.write('{"dd": {"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "%s"}}}'%(no))
    f.write('{"dd": {"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "DD%s"}},"pa": {"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "PA%s"}},"ta": {"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "TA%s"}},"ca": {"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "CA%s"}},"zh": {"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "ZH%s"}}}'%(no,no,no,no,no))
    # 关闭文件
    f.close()

if __name__ == '__main__':
    while 1 < 2:
        aa = time.strftime("%Y%m%d%H%M%S", time.localtime())
        write_file(aa)
        print(aa)
        time.sleep(30)
