# 生成log日志
from datetime import datetime
import logging,os


# 定义生成日志类
class Create_log(object):

    # 定义析构方法--用于每一次调用都自动执行
    def __init__(self):
        # 上一级路径                        D:\python-lj\ce_shi\k_j
        base_path=os.path.abspath(".")  # D:\python-lj\1609C_repository01\interface_test_pro
        print('上一级路径',base_path)

        # 给新生log日志起名,当前时间+后缀名.log---.strftime('Y%-%m-%d')只要年月日
        log_name=datetime.now().strftime('%Y-%m-%d')+'.log'  # 2019-05-14.log
        # print(log_name)

        # 日志log文件-存储路径  文件夹名  日志名
        # D:\python-lj\1609C_repository01\interface_test_pro\data/2019-05-14.log
        log_file=base_path+'/report/'+log_name
        # print(log_file,'/////')

        self.log=logging.getLogger()
        self.log.setLevel(logging.DEBUG)  # 设置等级  debug

        file_add=logging.FileHandler(log_file)  # 创建文件的一个流 FileHandler(log_file)+路径log_file
        # 设置显示字段
        ff=logging.Formatter('%(asctime)s %(filename)s %(module)s %(lineno)d %(funcName)s %(message)s ')
        # 把显示字段添加file_add日志流里面
        file_add.setFormatter(ff)
        # 把流添加到debug日志显示
        self.log.addHandler(file_add)

    # 自定义方法
    def get_log(self):
        return self.log  # 返回