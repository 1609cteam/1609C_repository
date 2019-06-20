import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


# 收件人地址列表，支持多个收件人，最多30个
# rcptlist = ['1666323633@qq.com']
# receivers = ','.join(rcptlist)
# 构建 multipart 的邮件消息
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Test Email'
msg['From'] = 'rzm_boy@163.com'
msg['To'] = '1666323633@qq.com'
# 构建 multipart/alternative 的 text/plain 部分
alternative = MIMEMultipart('alternative')
textplain = MIMEText('liu-shu-jie', _subtype='plain', _charset='UTF-8')
alternative.attach(textplain)
# 构建 multipart/alternative 的 text/html 部分
texthtml = MIMEText('report.html', _subtype='html', _charset='UTF-8')
alternative.attach(texthtml)
# 将 alternative 加入 mixed 的内部
msg.attach(alternative)
# 附件类型

"""
# xlsx 类型的附件
xlsxpart = MIMEApplication(open('测试文件1.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename=Header("测试文件1.xlsx","utf-8").encode())
msg.attach(xlsxpart)

"""

"""
# jpg 类型的附件
jpgpart = MIMEApplication(open('2.jpg', 'rb').read())
jpgpart.add_header('Content-Disposition', 'attachment', filename=Header("2.jpg","utf-8").encode())
msg.attach(jpgpart)
"""

"""
# mp3 类型的附件
mp3part = MIMEApplication(open('3.mp3', 'rb').read())
mp3part.add_header('Content-Disposition', 'attachment', filename=Header("3.mp3","utf-8").encode())
msg.attach(mp3part)
"""
# HTML报告类型
part = MIMEApplication(open('./report/report.html', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=Header("index.html", "utf-8").encode())
msg.attach(part)

# 发送邮件
try:
    client = smtplib.SMTP()
    # python 2.7以上版本，若需要使用SSL，可以这样创建client
    # client = smtplib.SMTP_SSL()
    client.connect('smtp.163.com')
    client.login('rzm_boy@163.com', 'rzm741')
    # 发件人和认证地址必须一致
    client.sendmail('rzm_boy@163.com', '1666323633@qq.com', msg.as_string())
    client.quit()
    print('发送成功')
except smtplib.SMTPRecipientsRefused:
    print('发送失败,收件人拒绝')
except smtplib.SMTPAuthenticationError:
    print('发送失败,认证错误')
except smtplib.SMTPSenderRefused:
    print('发送失败,发件人被拒接')
except smtplib.SMTPException as e:
    print('发送失败:', e.errno)
