from interface_test_pro.case.ss import *
from interface_test_pro.case.mylog import *

import time
import unittest
a=Cs()
b=CaseLog()
log=b.get_log()
class Csyq(unittest.TestCase):
    def setUp(self):
        print('开始')

    def test_1(self):
        print('插入数据')
        log.debug('插入数据')
        ge_t = a.pos_t()
        self.assertEqual(ge_t, 201, '失败')

    def test_2(self):
        time.sleep(5)
        print('查看数据')
        log.debug('查看数据')
        ge_t=a.ge_t()
        self.assertEqual(ge_t,200,'失败')
    def test_3(self):
        print('修改数据')
        time.sleep(10)
        log.debug('修改数据')
        ge_t=a.pu_t()
        self.assertEqual(ge_t,200,'失败')
    def test_4(self):
        print('删除数据')
        time.sleep(15)
        log.debug('删除数据')
        ge_t=a.de_l()
        self.assertEqual(ge_t,204,'失败')
    def tearDown(self):
        print('结束')
if __name__ == '__main__':
    unittest.main()
