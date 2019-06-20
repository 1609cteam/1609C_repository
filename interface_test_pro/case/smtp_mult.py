#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 11:51
# @Author  : 蔚明杭
# @Site    : 
# @File    : smtp_mult.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication

class SmtpMult():
    # 发送人邮箱名和密码
    email_name = '13306517079@163.com'
    password = 'ymh13306517079'
    # 收件人邮箱列表
    receiver_list = ['2394686994@qq.com']
    receivers = ','.join(receiver_list)
    # 构建附件消息
    message = MIMEMultipart('mixed')
    # 标题
    message['Subject'] = '测试报告'
    message['From'] = email_name
    message['To'] = receivers

    # 构建multipart/alternative的text/plain部分
    alternative = MIMEMultipart('alternative')
    textplain = MIMEText('ymh',_subtype='plain',_charset='utf-8')
    alternative.attach(textplain)

    # 构建multipart/alternative的text/html部分
    texthtml = MIMEText('report.html',_subtype='html',_charset='utf-8')
    alternative.attach(texthtml)

    # 将alternative加入mixed的内部
    message.attach(alternative)


    # 附件类型
    """
    # xlsx 类型的附件
    xlsxpart = MIMEApplication(open('测试文件1.xlsx','rb').read())
    xlsxpart.add_header('Content-Disposition','attachment',filename=Header('测试文件.xlsx','utf-8').encode())
    message.attach(xlsxpart)
    """

    # jpg类型的附件
    """
    jpgpart = MIMEApplication(open('1.jpg','rb').read())
    jpgpart.add_header('Content-Disposition','attachment',filename=Header('1.jpg','utf-8').encode())
    message.attach(jpgpart)
    """

    """
    # MP3类型的附件
    mp3part = MIMEApplication(open('1.mp3','rb').read())
    mp3part.add_header('Content-Disposition','attachment',filename=Header('1.mp3','utf-8').encode())
    message.attach(mp3part)
    """
    # HTML报告类型
    part = MIMEApplication(open('../report/report.html','rb').read())
    part.add_header('Content-Disposition','attachment',filename=Header('index.html','utf-8').encode())
    message.attach(part)

    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(email_name,password)
        smtp.sendmail(email_name,receiver_list,message.as_string())
        smtp.quit()
        print('发送成功！')
    except smtplib.SMTPRecipientsRefused:
        print('发送失败，收件人拒绝！')
    except smtplib.SMTPAuthenticationError:
        print('发送失败，认证错误！')
    except smtplib.SMTPSenderRefused:
        print('发送失败，发送人拒绝发送')
    except smtplib.SMTPException:
        print('发送失败，其他错误')