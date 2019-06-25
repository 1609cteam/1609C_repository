from email.header import Header

from email.mime.text import MIMEText

from smtplib import SMTP


def send_email(subject,content):

    email_client = SMTP('smtp。163.com')
    email_client.login('tiantester@163.com','tmg666888')

    msg =   MIMEText(content,'html','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['Form'] = 'tiantester@163.com'
    msg['To'] = '250395029@qq.com'
    email_client.sendmail('tiantester@163.com','250395029@qq.com',msg.as_string())

    email_client.quit()
    print('发送成功')

send_email('增删改查',open('../report/report.html','rb').read())