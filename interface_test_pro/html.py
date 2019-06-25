import interface_test_pro
from interface_test_pro import run
from interface_test_pro.util.HTMLTestRunner import HTMLTestRunner
import unittest


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(MyTest('test_a_run'))
    # suite.addTest(MyTest('test_b_run'))
    # suite.addTest(MyTest('test_c_run'))
    # suite.addTest(MyTest('test_d_run'))

    cases = unittest.TestLoader().loadTestsFromTestCase(run.MyTest)
    suite = unittest.TestSuite(cases)

    with open(r'F:\1609C_repository\interface_test_pro\report\report.html','wb') as f:

        reunner = HTMLTestRunner(

            stream=f,
            title='book_type',
            description= 'book-type',
            verbosity=2

        )
        reunner.run(suite)
