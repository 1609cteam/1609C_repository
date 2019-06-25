import logging

from datetime import datetime

import os

class CaseLog(object):

    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        base_path = os.path.abspath('../') +'\\'
        print(base_path)
        log_name = base_path + datetime.now().strftime('%y-%m-%d') + '.log'
        file_handle = logging.FileHandler(log_name)
        style = logging.Formatter('%(name)-%(levelname)s-%(filename)s-%(pathname)s-%(message)s')
        file_handle.setFormatter(style)
        self.logger.addHandler(file_handle)

    def get_log(self):

        return self.logger

CaseLog()