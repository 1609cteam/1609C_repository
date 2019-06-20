#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 14:52
# @Author  : 蔚明杭
# @Site    :
# @File    : html_code.py
# @Software: PyCharm

import unittest
import os

from interface_test_pro.run import MyTest
from interface_test_pro.util.HTMLTestRunner import HTMLTestRunner
from interface_test_pro.case.yuminghang import RunMain

from interface_test_pro.case.smtp_mult import SmtpMult

class Html():
    base_path = os.path.abspath('..')
    base_url = base_path+'/report/report.html'

    cases = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    suite = unittest.TestSuite([cases])
    with open(base_url,'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title='接口测试',
            description='查看，增加',
            verbosity=2
        )
        runner.run(suite)
Html()
SmtpMult()