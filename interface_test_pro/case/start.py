import unittest,os,yagmail
import smtplib
from interface_test_pro.util.HTMLTestRunner import *
from interface_test_pro.case.luxuanming import *
# from interface_test_pro.case.lxm import *

import smtplib
from email.header import Header
from email.mime.text import MIMEText
import os,yagmail  # 附件用


# 测试生成html报告!

# 发送遍历html内容的邮件函数
def email():
    # 发件人和收件人
    sender = 'lxm_331131808@163.com'
    # 发送单人
    # receiver = '331131808@qq.com'
    # 多人发送
    receiver = '331131808@qq.com,1370530477@qq.com'

    # 所使用的用来发送邮件的SMTP服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = 'lxm_331131808@163.com'
    password = 'lxm163'

    # 邮件主题
    mail_title = '主题：商品测试报告'
    # 读取html文件的绝对路径
    report = r"D:\python-lj\1609C_repository\interface_test_pro/report/report.html"
    # 读取html文件内容
    f = open(report, 'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
    mail_body = f.read()
    f.close()

    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        # print("发送邮件成功！！！")
        smtp.quit()
        return "发送邮件成功01！！！"
    except smtplib.SMTPException:
        return "发送邮件失败01！！！"


# 发送附件的html邮件函数
def email01():
    # print('上传附件路径:',file)
    #  指定最新的测试报告路径report/report.html--D:\python-lj\1609C_repository\interface_test_pro/report/report.html
    file=r'D:\python-lj\1609C_repository\interface_test_pro/report/report.html'
    print('测试报告html文件:', file)

    # 填写登录信息--通过网易163邮箱进行发送给QQ邮箱           网易ip地址
    yag = yagmail.SMTP("lxm_331131808@163.com", "lxm163", "smtp.163.com")

    # 邮件正文---副标题
    content = "<<商品接口测试试报告>>__下载附件"
    # 将测试报告作为附件发送--进行发送--主标题--副标题-文件路径
    # --发送两个人
    yag.send("331131808@qq.com", "商品测试报告", content, file)
    yag.send("1370530477@qq.com", "商品测试报告", content, file)
    return '发送邮件成功02!'


# 运行--方法01-------------------------------------------
if __name__ == '__main__':
    cs=unittest.TestLoader().loadTestsFromTestCase(Shop)  # 类
    zx=unittest.TestSuite([cs])

    bas_path=os.path.abspath('..')
    print(bas_path)
    # 编辑html文件生成报告
    with open(bas_path+'/report/report.html','wb') as f:
        runner=HTMLTestRunner(
            stream=f,
            title='增删改查商品',
            description='自动化测试商品接口',
            verbosity=2
        )
        runner.run(zx)
        # 调用发送邮件函数
        print(email())
        time.sleep(2)
        print(email01())




# 方法02------------------------------------
# if __name__ == '__main__':
#     # 1. 构建测试套件
#     tjs=unittest.TestSuite()
#     # 把列表添加到测试套件
#     # test_list=[Shop('test_sptj'),Shop('test_spxg'),Shop('test_spsc'),Shop('test_spck')]
#     test_list=[Shop('test_spxg'),Shop('test_spck')]
#     # 把列表添加到套件运行--单独一个用addTest  多个加s  addTests
#     tjs.addTests(test_list)
#
#
#     base_path = os.path.abspath('..')
#     print(base_path)
#     # 编辑html文件生成报告
#     with open(base_path+'/report/report.html','wb') as f:
#         runner=HTMLTestRunner(
#             stream=f,
#             title='增删改查商品',
#             description='自动化测试商品接口',
#             verbosity=2
#         )
#         runner.run(tjs)







