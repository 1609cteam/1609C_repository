
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SmtpText():
    smtp_server = 'smtp.163.com'
    receivers = 'wshminghang@aliyun.com'# 接受邮件的邮箱

    # 用户名和密码
    username = '13306517079@163.com'
    password = 'ymh13306517079'

    message = MIMEText('python 邮件发送测试','plain','utf-8')
    message['Form'] = username# 发送者
    message['To'] = receivers # 接受者

    # 发送内容
    subject = '用python进行SMTP邮件测试'
    message['Subject'] = Header(subject,'utf-8')
    try:
        smypobj = smtplib.SMTP()
        smypobj.connect(smtp_server)
        smypobj.login(username,password)
        # smypobj.send(sender,receivers,message.as_string())
        smypobj.sendmail(username,receivers,message.as_string())

        print('邮件发送成功')
    except smtplib.SMTPException:
        print('Error 无法发送邮件')