#coding=utf8
import time

from interface_test_pro.case import mysql
from interface_test_pro.case.api_ceshi import SELECT, POST, UPDATE, DELETE
import unittest

from interface_test_pro.case.log_file.log import CaseLog




class API(unittest.TestCase):

    def setUp(self):
        log = CaseLog()
        self.logger = log.get_log()
        self.logger.debug('开始')

    def tearDown(self):
        self.logger.debug('结束')

    def test_liushujie(self):
        status_select = SELECT
        time.sleep(1)
        status_post = POST
        time.sleep(1)
        status_update = UPDATE
        time.sleep(1)
        status_delete = DELETE
        time.sleep(1)
        self.logger.debug('查询')
        self.assertEqual(200,status_select,msg='查询失败')
        self.logger.debug('查询结束')
        self.logger.debug('添加')
        self.assertEqual(201,status_post,msg='提交失败')
        self.logger.debug('添加结束')
        self.logger.debug('修改')
        self.assertEqual(200,status_update,msg='修改失败')
        self.logger.debug('修改结束')
        self.logger.debug('删除')
        self.assertEqual(204,status_delete,msg='删除失败')
        self.logger.debug('删除结束')


if __name__ == '__main__':
    unittest.main()
    mysql.mysql()


