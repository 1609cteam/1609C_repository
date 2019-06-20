import unittest

from interface_test_pro.case.log_code import MyLog

from interface_test_pro.case.yuminghang import RunMain
# from interface_test_pro.case.html_code import Html
log = MyLog()
logger = log.get_log()

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        self.run_main = RunMain()
        print('22222')

    # @classmethod
    # def tearDownClass(self):
    #     # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    #     print('4444444')
    #
    # @classmethod
    # def setUpClass(self):
    #     # 必须使用@classmethod 装饰器,所有test运行前运行一次
    #     print('33333')
    def test_a_run(self):
        # html = Html()
        logger.debug('查看')
        print('test_aaaaaaaaaaaaaaaaaaaaaaaaa')
        run_get = self.run_main.send_get('http://127.0.0.1:8000/goods/1', '')
        self.assertEqual(run_get.status_code, 200,msg='查询失败')  # 测试用例

    def test_b_run(self):
        logger.debug('增加')
        print('test_bbbbbbbbbbbbbbbbbbbb')
        run_post = self.run_main.send_post('http://127.0.0.1:8000/goods/',
                      {
                          "name": "桃子18",
                          "price": 5.67,
                          "goods_type": 1
                      })
        self.assertEqual(run_post.status_code, 201,msg='增加失败')  # 测试用例

    def test_c_run(self):
        logger.debug('修改')
        print('test_ccccccccccccccccccccccc')
        run_put = self.run_main.send_put('http://127.0.0.1:8000/goods/1/',
                      {
                          "id": 1,
                          "name": "桃子1",
                          "price": 1.1,
                          "goods_type": 1
                      })
        self.assertEqual(run_put.status_code, 200,msg='修改失败')  # 测试用例

# 主函数234
if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例