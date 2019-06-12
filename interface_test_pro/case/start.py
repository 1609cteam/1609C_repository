import unittest,os
from interface_test_pro.util.HTMLTestRunner import *
from interface_test_pro.case.luxuanming import *

# 测试生成html报告!
if __name__ == '__main__':
    cs=unittest.TestLoader().loadTestsFromTestCase(Shop)  # 类
    zx=unittest.TestSuite([cs])

    base_path=os.path.abspath('..')
    # 编辑html文件生成报告
    with open(base_path+'/report/report.html','wb') as f:
        runner=HTMLTestRunner(
            stream=f,
            title='增删改查商品',
            description='自动化测试商品接口',
            verbosity=2
        )
        runner.run(zx)