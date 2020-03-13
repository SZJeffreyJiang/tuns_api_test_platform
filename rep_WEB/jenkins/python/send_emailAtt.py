import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

PROJECT_NAME=sys.argv[1]
BUILD_NUMBER=sys.argv[2]
BUILD_URL=sys.argv[3]

smtpserver='smtp.mxhichina.com'

user='15914116527'
password='mkjiangle1'

sender='jiangrongle6527@dingtalk.com'
receives=['29548750@qq.com']
# receives=['jiangrongle@honhesns.com']

subject = PROJECT_NAME+'第'+BUILD_NUMBER+'次api测试报告'
content='<html><h1 style="color:red">ERP API TestReport</h1></html><span>\n测试报告请见附件 \n本邮件为自动发送请勿回复\n 构建地址:"'+BUILD_URL+"</span>"


send_file=open(r'D:\TS_apiTest\APP\jenkins\html\APP_api_testreport.html' ,'rb').read()



att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="APP_api_testreport.html"'


msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)


smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("Start send email...")
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print("Send email end!")



