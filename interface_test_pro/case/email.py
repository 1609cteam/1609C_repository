# 发送附件的html邮件函数
import smtplib, yagmail
from email.mime.text import MIMEText
from email.header import Header


# ====生成文档===============
# from interface_test_pro.case.report_html import *
# from interface_test_pro.util.HTMLTestRunner import *


def email():
    # 发件邮箱
    sender = 'zhuyangyang5969@163.com'
    # 单人接收邮箱
    receiver = ['1248050365@qq.com']
    # 多人接收邮箱
    # receiver = ['1370530477@qq.com','1248050365@qq.com']

    # 连接网易邮箱
    smtpserner = 'smtp.163.com'
    # 发件邮箱 的用户名 与授权码
    username = 'zhuyangyang5969@163.com'
    password = 'zyy1248050365'
    # 邮件标题
    title = '测试报告'
    # 读取html文件内容的路径
    report = r'D:\Program Files\1609C_repository\interface_test_pro\report\report_html.html'
    # 读取HTML文件内容
    f = open(report, 'rb')
    email_body = f.read()
    f.close()
    # ========================封装参数===============================================================================
    # ========================邮件主体===============================================================================
    message = MIMEText(email_body, 'html', 'utf-8')
    message['From'] = Header('小爱')
    message['To'] = report
    message['Subject'] = Header(title, 'utf-8')
    try:
        smt = smtplib.SMTP()
        smt.connect(smtpserner)
        smt.login(username, password)
        smt.sendmail(sender, receiver, message.as_string())
        smt.quit()
        print('进来了....')
        return '发送邮件成功--1'
    except smtplib.SMTPException:
        return '发送邮件失败--1'
    # =================附件=====================================


import yagmail


def email_affix():
    file = r'D:\Program Files\1609C_repository\interface_test_pro\report\report_html.html'
    print('测试报告HTML文件:', file)
    yag = yagmail.SMTP('zhuyangyang5969@163.com', 'zyy1248050365', 'smtp.163.com')
    # 邮件正文
    content = '<商品接口测试报告>_下载附件'
    # 将测试报告作为附件发送-进行发送-主标题-副标题-文件路径
    yag.send('1248050365@qq.com', '商品测试报告', content, file)
    # 老师邮箱地址
    # yag.send('1370530477@qq.com', '商品测试报告', content, file)
    return '发送邮件附件成功....'


if __name__ == '__main__':
    email()
    email_affix()
