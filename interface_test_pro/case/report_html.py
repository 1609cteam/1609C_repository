import unittest
# from interface_test_pro.case import mysql
# mysql.mysql()
from interface_test_pro.case.my_run import API
from interface_test_pro.util import HTMLTestRunner

if __name__ == '__main__':
    n = unittest.TestSuite()
    n.addTest(API('test_zhuyangyang'))
    with open(r'D:\Program Files\1609C_repository\interface_test_pro\report\report_html.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='My unit test',
            description='This demonstrates the report output by The interface test.',
            verbosity=2
        )
        runner.run(n)
