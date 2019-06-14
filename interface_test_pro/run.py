import unittest

from interface_test_pro.case.renzhiming import Rzm
from interface_test_pro.log import CaseLog


class MyTest(unittest.TestCase):  # 继承unittest.TestCase

    def tearDown(self):
        # 每个测试用例执行之后做操作
        self.logger.debug('=====结束了=====')

    def setUp(self):
        # 每个测试用例执行之前做操作
        log = CaseLog()
        self.logger = log.get_log()
        self.logger.debug('=====开始了=====')

    # def tearDownClass(self):
    #     # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    #     print('4444444')
    #
    # def setUpClass(self):
    #     # 必须使用@classmethod 装饰器,所有test运行前运行一次
    #     print('33333')

    def test_Post(self):
        res = Rzm()
        data = {'type_name': '金庸武侠'}
        self.assertEqual(res.Post_Api(data), 201)  # 测试用例

    def test_del(self):
        res = Rzm()
        url = 'http://10.30.29.53:9000/book_type/17/'
        self.assertEqual(res.Delete_Api(url), 204)  # 测试用例

    def test_Put(self):
        res = Rzm()
        data = {'type_name': '金庸'}
        self.assertEqual(res.Put_Api(data, 18), 200)  # 测试用例

    # def test_Put(self):
    #     res = Rzm()
    #     data = {'type_name': '金庸asd武侠'}
    #     self.assertEqual(res.Put_Api(data, 16), 200)

    def test_Get(self):
        res = Rzm()

        self.assertEqual(res.Get_Api(), 200)  # 测试用例


# 主函数234
if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
