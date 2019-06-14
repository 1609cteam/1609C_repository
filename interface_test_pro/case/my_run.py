import unittest
import time
# 引入测试用例
from interface_test_pro.case.python_cases import SELECT, POST, UPDATE, DELETE
# 测试数据库清空操作
from interface_test_pro.case import mysql
# 引入日志
from interface_test_pro.case.report_log import Log


class API(unittest.TestCase):
    def setUp(self):
        print('开始了....')
        log = Log()
        self.logger = log.get_log()
        self.logger.debug('----开始---->')

    def test_zhuyangyang(self):
        print('增...')
        status_post = POST
        time.sleep(3)
        self.assertEqual(201, status_post, msg='增加错误')
        self.logger.debug('----增加---->')
        print('改 ...')
        status_put = UPDATE
        time.sleep(3)
        self.assertEqual(200, status_put, msg='修改错误')
        self.logger.debug('----修改---->')
        print('查..')
        status_select = SELECT
        time.sleep(3)
        self.assertEqual(200, status_select, msg='查询错误')
        self.logger.debug('----查询---->')

        print('删 ...')
        status_delete = DELETE
        time.sleep(3)
        self.assertEqual(204, status_delete, msg='删除错误')
        self.logger.debug('----删除---->')

    def tearDown(self):
        print('结束了.....')
        self.logger.debug('----结束---->')
        # 数据库清空操作
        mysql.mysql()


if __name__ == '__main__':
    unittest.main()


