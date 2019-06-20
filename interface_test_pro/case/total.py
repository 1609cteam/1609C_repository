# import unittest
#
# from interface_test_pro.case.log_code import MyLog
#
# from interface_test_pro.case.yuminghang import RunMain
# # from interface_test_pro.case.html_code import Html
# log = MyLog()
# logger = log.get_log()
#
# class Total(unittest.TestCase):  # 继承unittest.TestCase
#     def tearDown(self):
#         # 每个测试用例执行之后做操作
#         print('111')
#
#     def setUp(self):
#         # 每个测试用例执行之前做操作
#         self.run_main = RunMain()
#         print('22222')
#
#     def test_a(self):
#         # html = Html()
#         logger.debug('查看')
#         run_get = self.run_main.send_get('http://127.0.0.1:8000/goods/1', '')
#         return run_get
#
#     def test_b(self):
#         logger.debug('增加')
#         run_post = self.run_main.send_post('http://127.0.0.1:8000/goods/',
#                       {
#                           "name": "桃子18",
#                           "price": 5.67,
#                           "goods_type": 1
#                       })
#         return run_post
#
#     def test_c(self):
#         logger.debug('修改')
#         run_put = self.run_main.send_put('http://127.0.0.1:8000/goods/1/',
#                       {
#                           "id": 1,
#                           "name": "桃子1",
#                           "price": 1.1,
#                           "goods_type": 1
#                       })
#         return run_put
#
# # 主函数234
# if __name__ == '__main__':
#     unittest.main()  # 运行所有的测试用例