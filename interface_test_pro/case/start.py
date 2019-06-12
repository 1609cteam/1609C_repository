#coding=utf8
import unittest

from interface_test_pro.case.run import API
from interface_test_pro.util.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(API('test_liushujie'))
    with open(r'C:\Users\dell\Desktop\1609C_repository\interface_test_pro\report\report.html','wb') as fp:
        runner = HTMLTestRunner(
            verbosity=2,
            stream=fp,
            title='API',
            description='增删改查'
        )
        runner.run(suite)