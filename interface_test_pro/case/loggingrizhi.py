import logging
import os
import datetime
from logging import getLogger
class Caselog(object):
    def __init__(self):
        #文件夹绝对路劲
        base_path = os.path.abspath('..')
        # print(base_path)
        #当前文件父级路劲
        base_url = os.path.dirname(os.path.abspath(__file__))
        # print(base_url)
        #日期为name的log日志
        log_file = datetime.datetime.now().strftime("%y-%m-%d")+".log"
        # print(log_file)
        #设置log文件
        log_name = base_url+'/'+log_file
        # print(log_name)
        #生成日志
        self.logger = logging.getLogger()   #级别默认warning  数值30
        self.logger.setLevel(logging.DEBUG)    #设置级别为DEBUG   数值为10
        #把日志记录在log文件里,级别为DEBUG以上
        file_handle = logging.FileHandler(log_name)
        #设置日志格式
        '''
        % (name)s 记录器的名称        
        % (levelno)s 数字形式的日志记录级别
        % (levelname)s 日志记录级别的文本名称
        % (filename)s 执行日志记录调用的源文件的文件名称
        % (pathname)s 执行日志记录调用的源文件的路径名称
        % (funcName)s        执行日志记录调用的函数名称
        % (module)s        执行日志记录调用的模块名称
        % (lineno)s        执行日志记录调用的行号
        % (created)s        执行日志记录的时间
        % (asctime)s        日期和时间
        % (msecs)s        毫秒部分
        % (thread)d        线程ID
        % (threadName)s        线程名称
        % (process)d        进程ID
        % (message)s        记录的消息
        '''
        ff = logging.Formatter('%(asctime)s %(filename)s %(module)s %(lineno)d %(funcName)s %(message)s')
        file_handle.setFormatter(ff)    #格式化字符串

        #将相应的handler添加在logger对象中
        self.logger.addHandler(file_handle)
        self.logger.debug('aaa')

    def get_log(self):
        return self.logger

if __name__ == '__main__':
    a=Caselog()
