import logging
from datetime import datetime
import os
class CaseLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # base_path = os.path.abspath('..')+ '/' + 'log_file/'
        log_name = datetime.now().strftime('%Y-%m-%d') + '.txt'
        file_handle = logging.FileHandler(log_name)
        style = logging.Formatter('%(name)s-%(levelname)s-%(filename)s-%(pathname)s-%(message)s')
        file_handle.setFormatter(style)
        self.logger.addHandler(file_handle)

    def get_log(self):
        return self.logger

# yy = CaseLog()
# yy.get_log().debug('===============hello world============')
