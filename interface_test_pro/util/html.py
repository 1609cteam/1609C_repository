from HTMLTestRunner import HTMLTestRunner
import unittest
from interface_test_pro.run import MyTest

if __name__ == '__main__':
    cases = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    suite = unittest.TestSuite(cases)

    # a = os.path.abspath(".." + "/report/report.html")

    with open("../report/report.html", 'wb') as f:
        renner = HTMLTestRunner(
            stream=f,
            title='book_type',
            description='book_type',
            verbosity=2
        )
        renner.run(suite)
