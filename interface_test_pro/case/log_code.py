#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 14:26
# @Author  : 蔚明杭
# @Site    :
# @File    : log_code.py
# @Software: PyCharm

import logging
import os
from datetime import datetime

class MyLog(object):
    # 获取到当前目录的上上一级目录interface_test_pro
    def __init__(self):
        base_path = os.path.abspath('..')
        print('base_path：',base_path)
        # 生成日志名
        log_name = datetime.now().strftime('%Y-%M-%d')+'.log'
        print('log_name：',log_name)

        # 生成路径加文件
        log_file = base_path+'/report/'+log_name
        print('log_file：',log_file)

        self.logger = logging.getLogger()
        print('self.logger：',self.logger)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        print('self.logger：',self.logger)
        file_handle = logging.FileHandler(log_file)
        print('file_handle：',file_handle)
        ff = logging.Formatter('%(name)s %(levelname)s %(filename)s %(lineno)d %(message)s')
        file_handle.setFormatter(ff)
        self.logger.addHandler(file_handle)
        self.logger.debug('111')
    def get_log(self):
        return self.logger