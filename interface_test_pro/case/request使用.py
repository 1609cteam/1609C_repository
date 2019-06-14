# import requests
#
# url = 'http://127.0.0.1:8000/ban/'
# query = {'id': '1'}
# r = requests.get(url, params=query)
# print(r.text)
# print(r.status_code)
# print('***************************')
# r2 = requests.get(url+'1/')
# print(r2.text)
# print(r.status_code)

import smtplib
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('Hello Boy!')  # 邮件内容
message['From'] = Header('小爱')  # 邮件发送者名字
message['To'] = Header('小蓝枣')  # 邮件接收者名字
message['Subject'] = Header('来自异世界的一封信!')  # 邮件主题

mail = smtplib.SMTP()
mail.connect("smtp.163.com")  # 连接 qq 邮箱
mail.login("zhuyangyang5969@163.com", "zyy1248050365")  # 账号和授权码
mail.sendmail("zhuyangyang5969@163.com", ["1248050365@qq.com"], message.as_string())  # 发送账号、接收账号和邮件信息
mail.quit()
