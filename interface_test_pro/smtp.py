from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def send_email(subject, content):
    email_client = SMTP("smtp.163.com")  # smtp的邮箱
    email_client.login("rzm_boy@163.com", "rzm741")  # 网易邮箱的账号  状态码
    # create msg
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # 标题
    msg['From'] = "rzm_boy@163.com"  # 发送人
    msg['To'] = "1666323633@qq.com"  # 接收人
    email_client.sendmail("rzm_boy@163.com", "1666323633@qq.com", msg.as_string())

    email_client.quit()
    print('发送成功')


send_email("增删改查", open('./report/report.html', 'rb').read())
