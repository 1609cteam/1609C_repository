
"""


import time
import unittest
import pymysql
from interface_test_pro.case.api_ceshi import Test_Interface, SELECT, POST, UPDATE, DELETE
from interface_test_pro.log_file.log import CaseLog

def mysql():
    con = pymysql.connect(
                port=3306,
                host='localhost',
                user='root',
                password='lsj',
                db='api_ceshi'
            )
    cur = con.cursor()
    cur.execute('truncate demo_bookinfo')
    con.commit()





class MyTest(unittest.TestCase):  # 继承unittest.TestCase

    def setUp(self):
        # 每个测试用例执行之前做操作
        log = CaseLog()
        self.logger = log.get_log()
        self.logger.debug('=====开始了=====')
        # self.yy = Test_Interface()
    def tearDown(self):
        # 每个测试用例执行之后做操作
        self.logger.debug('=====结束了=====')


    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('4444444')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('33333')



    #调用查询
    def test_01(self):
    # def test_Get(self):
        self.logger.debug('=====正在查询=====')
        status_code = SELECT
        self.assertEqual(status_code,200,msg='查询失败')  # 测试用例
        self.logger.debug('=====查询结束=====')
        time.sleep(2)

    #    调用添加
    def test_02(self):
    # def test_Post(self):
        self.logger.debug('=====正在添加=====')
        status_code = POST
        self.assertEqual(status_code, 201, msg='添加失败')  # 测试用例
        self.logger.debug('=====添加结束=====')
        time.sleep(2)

    #调用修改
    # def test_Put(self):
    def test_03(self):
        self.logger.debug('=====正在修改=====')
        status_code = UPDATE
        self.assertEqual(status_code, 200,msg='修改失败')  # 测试用例
        self.logger.debug('=====修改结束=====')
        time.sleep(2)

    # 调用删除
    def test_04(self):
    # def test_Delete(self):
        self.logger.debug('=====正在删除=====')
        status_code = DELETE
        self.assertEqual(status_code, 204, msg='删除失败')  # 测试用例
        self.logger.debug('=====删除结束=====')
        time.sleep(2)



# 主函数234
if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
    mysql()
"""