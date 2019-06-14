import os,yagmail

#测试报告存储路径01
wj=os.path.abspath('..')

report_dir = wj+'/report/'
#测试报告存储路径02
# report_dir = "../report/"

#将测试报告文件夹下的所有文件名作为一个列表返回
lists = os.listdir(report_dir)
#对所有测试报告按照生成时间进行排序
lists.sort(key = lambda filename : os.path.getmtime(report_dir+filename))
#获取最新的测试报告
recent=lists[1]
print('测试报告html文件:',recent)

# 指定最新的测试报告路径report/report.html--D:\python-lj\1609C_repository\interface_test_pro/report/report.html
file=os.path.join(report_dir,recent)
# print('上传附件路径:',file)

#填写登录信息--通过网易163邮箱进行发送给QQ邮箱
yag = yagmail.SMTP("wu1994109253@163.com","cao130126","smtp.163.com")

#邮件正文---副标题
content="商品试报告"

#将测试报告作为附件发送--进行发送--主标题--副标题-文件路径
yag.send("1370530477@qq.com","测试报告",content,file)
print('发送成功!')







# import os,yagmail
#
# #测试报告存储路径01
# report_dir = r"D:\python-lj\1609C_repository\interface_test_pro/report/"
# #测试报告存储路径02
# # report_dir = "../report/"
#
# #将测试报告文件夹下的所有文件名作为一个列表返回
# lists = os.listdir(report_dir)
# #对所有测试报告按照生成时间进行排序
# lists.sort(key = lambda filename : os.path.getmtime(report_dir+filename))
# #获取最新的测试报告
# recent=lists[1]
# print('测试报告html文件:',recent)
#
# # 指定最新的测试报告路径report/report.html--D:\python-lj\1609C_repository\interface_test_pro/report/report.html
# file=os.path.join(report_dir,recent)
# # print('上传附件路径:',file)
#
# #填写登录信息--通过网易163邮箱进行发送给QQ邮箱
# yag = yagmail.SMTP("lxm_331131808@163.com","lxm163","smtp.163.com")
#
# #邮件正文---副标题
# content="商品试报告"
#
# #将测试报告作为附件发送--进行发送--主标题--副标题-文件路径
# yag.send("331131808@qq.com","测试报告",content,file)
# print('发送成功!')