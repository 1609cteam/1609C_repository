import logging
from datetime import datetime
import os


class CaseLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        base_path = os.path.abspath('../') + '\\'
        log_name = base_path + datetime.now().strftime('%Y-%m-%d') + '.log'
        file_handle = logging.FileHandler(log_name)
        style = logging.Formatter('%(name)s-%(levelname)s-%(filename)s-%(pathname)s-%(message)s')
        file_handle.setFormatter(style)
        self.logger.addHandler(file_handle)

    def get_log(self):
        return self.logger

# if __name__ == '__main__':
#     CaseLog()
# class MyLog(object):
#     def __init__(self):
#         self.base_path = os.path.abspath('.')
#         print(self.base_path)
#         # 生成文件名
#         log_file = datetime.now().strftime('%Y-%m-%d') + '.log'
#         log_name = self.base_path + '/logs/' + log_file
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#
#         # 在绝对路径下创建文件
#         self.file_handle = logging.FileHandler(log_name)
#
#         # 生成日志
#         self.ff = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s ')
#         self.file_handle.setFormatter(self.ff)
#
#         self.logger.addHandler(self.file_handle)
#         self.logger.debug('用类写的debug')
#
#     def get_log(self):
#         return self.logger
