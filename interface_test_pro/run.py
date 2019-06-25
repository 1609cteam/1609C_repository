# import unittest
#
# from interface_test_pro.case.tianmenggang import Test_yl
# class MyTest(unittest.TestCase):  # 继承unittest.TestCase
#
#
#
#     def tearDown(self):
#         # 每个测试用例执行之后做操作
#         print('4444444444')
#
#     def setUp(self):
#         # 每个测试用例执行之前做操作
#         self.test = Test_yl()
#         self.test1 = self.test.send_get("http://127.0.0.1:8000/goodstype/",'1')
#         self.test2 = self.test.send_post("http://127.0.0.1:8000/goodstype/")
#         # self.test3 = self.test.send_put("http://127.0.0.1:8000/goodstype/",'4')
#         # self.test4 = self.test.send_delete("http://127.0.0.1:8000/goodstype/3/")
#
#     def test_01(self):
#         self.assertEqual(self.test1,200)  # 测试用例
#     #
#     def test_02(self):
#         self.assertEqual(self.test2,201)  # 测试用例
#     #
#     # def test_c_run(self):
#     #     self.assertEqual(self.test3,200)
#     #
#     # def test_d_run(self):
#     #     self.assertEqual(self.test4,204)
#
# # 主函数234
# if __name__ == '__main__':
#     unittest.main()  # 运行所有的测试用例
import unittest

from interface_test_pro.case.tianmenggang import Test_yl

from interface_test_pro.rizhi import CaseLog

class MyTest(unittest.TestCase):  # 继承unittest.TestCase



    def setUp(self):
        log = CaseLog()
        self.logger = log.get_log()
        self.logger.debug('开始')


    def test_a_run(self):
        self.test = Test_yl()
        self.test1 = self.test.send_get("http://127.0.0.1:8000/goodstype/", '1')
        self.assertEqual(self.test1,200)
        self.logger.debug('查看')
        print('查看')

    def test_b_run(self):
        self.test = Test_yl()
        ress = {"name": "飘忽不定呀"}
        self.test2 = self.test.send_post("http://127.0.0.1:8000/goodstype/", ress)
        self.assertEqual(self.test2, 201)  # 测试用例
        self.logger.debug('增加')
        print('添加')

    def test_c_run(self):
        self.test = Test_yl()
        self.test3 = self.test.send_put("http://127.0.0.1:8000/goodstype/39/", {'id': 39, "name": '红人馆'})
        self.assertEqual(self.test3, 200)  # 测试用例
        self.logger.debug('修改')
        print('修改')

    def test_d_run(self):
        self.test = Test_yl()
        self.test4 = self.test.send_delete("http://127.0.0.1:8000/goodstype/4/")
        self.assertEqual(self.test4, 204)  # 测试用例
        self.logger.debug('删除')
        print('删除')

    def tearDown(self):
        # 每个测试用例执行之后做操作
        self.logger.debug('结束')

# 主函数234
if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
