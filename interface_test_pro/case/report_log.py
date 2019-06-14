# 日志页

import logging
from datetime import datetime
import os


class Log(object):
    def __init__(self):
        base_path = os.path.abspath('.')
        # print('地址:', base_path)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        log_f = datetime.now().strftime('%Y-%M-%d') + '.log'
        log_name = base_path + '/logs/' + log_f
        file_handel = logging.FileHandler(log_name)
        style = logging.Formatter('%(asctime)s %(filename)s %(module)s  %(funcName)s %(lineno)d %(msecs)d')
        file_handel.setFormatter(style)
        self.logger.addHandler(file_handel)

    def get_log(self):
        return self.logger


# yy = Log()
# yy.get_log().debug('-----------')
