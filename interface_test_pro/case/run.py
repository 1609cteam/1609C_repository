from interface_test_pro.case.cs import *
from interface_test_pro.util.HTMLTestRunner import *
import unittest
import os
if __name__ == '__main__':
    un=unittest.TestLoader().loadTestsFromTestCase(Csyq)
    fh=unittest.TestSuite(un)
    wj=os.path.abspath('..')
    with open(wj+'/report/'+'report.html','wb')as f:
        th=HTMLTestRunner(stream=f, verbosity=2, title='接口测试', description='测试')
        th.run(fh)


