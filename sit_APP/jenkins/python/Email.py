# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import sys

PROJECT_NAME=sys.argv[1]
BUILD_NUMBER=sys.argv[2]
BUILD_URL=sys.argv[3]


# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.263.net'
username = 'jiangrongle@honhesns.com'
password = 'mkjiangle1'
sender = 'jiangrongle@honhesns.com'
# receiver='XXX@126.com'
# 收件人为多个收件人
to_receiver = ['jiangrongle@honhesns.com','huangminling@honhesns.com']
cc_receiver =[ '29548750@qq.com']
receiver= to_receiver + cc_receiver

subject = PROJECT_NAME+'第'+BUILD_NUMBER+'次api测试报告'
# 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
# subject = '中文标题'
# subject=Header(subject, 'utf-8').encode()

# 构造邮件对象MIMEMultipart对象
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '秒台车自动化测试平台'
# msg['To'] = 'XXX@126.com'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ",".join(to_receiver)
msg['Cc'] = ",".join(cc_receiver)
# msg['Date']='2012-3-16'

 # 构造文字内容
text = "测试报告请见附件 \n本邮件为自动发送请勿回复\n 构建地址:"+BUILD_URL
text_plain = MIMEText(text , 'plain' , 'utf-8')
msg.attach(text_plain)

# # 构造图片链接
# sendimagefile = open(r'E:\apitest\appCenter\jenkins\html\expand.png' , 'rb').read()
# image = MIMEImage(sendimagefile)
# image.add_header('Content-ID' , '<image1>')
# image["Content-Disposition"] = 'attachment; filename="expand.png"'
# msg.attach(image)

# # 构造html
# html = """"""
#
# text_html = MIMEText(html , 'html' , 'utf-8')
# text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
# # msg.attach(text_html)

# 构造附件
sendfile = open(r'D:\mtcApiTest\QDS\jenkins\html\QDSAPP_api_testreport.html' , 'rb').read()
text_att = MIMEText(sendfile , 'base64' , 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 以下附件可以重命名成aaa.txt
# text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
# 另一种实现方式
text_att.add_header('Content-Disposition' , 'attachment' , filename='QDSAPP_api_testreport.html')
# 以下中文测试不ok
# text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
msg.attach(text_att)

# 发送邮件

smtp = smtplib.SMTP()
smtp.connect(smtpserver,port=25)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
smtp.ehlo()
smtp.starttls()
smtp.login(username , password)
smtp.sendmail(sender , receiver , msg.as_string())
smtp.quit()

