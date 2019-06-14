from HTMLTestRunner import HTMLTestRunner
import unittest
import interface_test_pro.run
from interface_test_pro.smtp import send_email

if __name__ == '__main__':
    cases = unittest.TestLoader().loadTestsFromTestCase(interface_test_pro.run.MyTest)
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
    with open("../report/report.html", 'r') as f:
        send_email("增删改查", f.read())
