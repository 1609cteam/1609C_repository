from selenium import webdriver
import unittest
from .gyz import Book
from interface_test_pro.case.loggingrizhi import Caselog
cas = Caselog()
log = cas.get_log()
book = Book()
class Bo(unittest.TestCase):
    def setUp(self):
        print('开始')
        log.debug('开始写入日志')
    def test_1(self):
        log.debug('开始增加')
        a = book.pos_t()
        self.assertEqual(201,a)
    def test_2(self):
        log.debug('开始查看')
        a = book.ge_t()
        self.assertEqual(200,a)
    def test_3(self):
        log.debug('开始修改')
        a = book.pu_t()
        self.assertEqual(200,a)
    def test_4(self):
        log.debug('开始删除')
        a = book.delet_e()
        self.assertEqual(204,a)

    def tearDown(self):
        print('结束')

if __name__ == '__main__':
    unittest.main()