import unittest
from interface_test_pro.case.test_case import Bo
from interface_test_pro.util.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    #构建测试套件
    cases = unittest.TestLoader().loadTestsFromTestCase(Bo)
    suite = unittest.TestSuite(cases)

    # 执行测试,打印详细信息
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    # 执行HTML文件
    with open('report.html','wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title='测试接口',
            description='自动化接口测试',
            verbosity=2
        )
        runner.run(suite)