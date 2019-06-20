#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 10:59
# @Author  : 蔚明杭
# @Site    : 
# @File    : smtp_html.py
# @Software: PyCharm

from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 发送人和接收人
sender = '13306517079@163.com'
receiver = '2394686994@qq.com'

# 发送邮箱人的用户名和密码
username = '13306517079@163.com'
password = 'ymh13306517079'

#邮箱服务
email_server = 'smtp.163.com'
# 邮箱主题
email_title = '测试报告'
# 读取html中的内容
f = open('../report/report.html','rb')
email_content = f.read()
f.close()

# 邮件的内容，格式，编码
message = MIMEText(email_content,'html','utf-8')
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(email_title,'utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect(email_server)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,message.as_string())
    smtp.quit()
    print('发送成功！')
except smtplib.SMTPException:
    print('发送失败！')