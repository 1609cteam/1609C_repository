import itchat
import os
import cv2
import time

sendMsg = u'{消息助手}:暂时无法回复'
usageMsg = u'使用方法:\n1.运行cmd命令:cmd xxx(xxx为命令)\n例如关机命令:\ncmd shutdown -s -t 60\n例如取消关机命令:\ncmd shutdown -a\n2.获取当前电脑用户:cap\n3.启用消息助手(默认关闭):ast\n4.关闭消息助手astc'
flag = 0
nowTime = time.localtime()
filename = str(nowTime.tm_mday) + str(nowTime.tm_hour) + str(nowTime.tm_min) + str(nowTime.tm_sec) + '.txt'


# myfile=open(filename,'w')
@itchat.msg_register('Text')
def reply_msg(msg):
    global flag
    message = msg['Text']
    message = message.lower()
    fromName = msg['FromUserName']
    toName = msg['ToUserName']
    if toName == 'filehelper':

        if message == 'cap':
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            cv2.imwrite('weixinTemp.jpg', img)
            itchat.send('@img@%s' % 'weixinTemp.jpg', 'filehelper')
            cap.release()
        if message[0:3] == 'cmd':
            os.system(message.strip(message[0:4]))
        if message == 'ast':
            flag = 1
            itchat.send('消息助手已开启', 'filehelper')
        if message == 'astc':
            flag = 0
            itchat.send('消息助手已关闭', 'filehelper')
    # elif flag==1:
    #     itchat.send(sendMsg,fromName)
    #     myfile.write(message)
    #     myfile.write('\n')
    #     myfile.flush()


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.send(usageMsg, 'filehelper')
    itchat.run()
