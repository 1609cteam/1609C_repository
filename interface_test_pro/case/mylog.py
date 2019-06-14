import logging
import  os
import datetime
import time
class CaseLog(object):
    def __init__(self):
        base_url = os.path.dirname(os.path.abspath(__file__))
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        if not os.path.exists('logs'):
            os.mkdir('logs')
        log_name = base_url+'/logs/'+log_file
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        file_handle = logging.FileHandler(log_name)
        ff = logging.Formatter('%(asctime)s %(filename)s %(module)s %(lineno)d %(funcName)s %(message)s ')
        file_handle.setFormatter(ff)
        self.logger.addHandler(file_handle)
    def get_log(self):
        return self.logger
if __name__ == '__main__':
    CaseLog()

