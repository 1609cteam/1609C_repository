from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains


class Lol(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = 'https://lol.qq.com/'

    def test_ying(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(5)
        you = driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a/span[1]')
        ActionChains(driver).move_to_element(you).perform()
        time.sleep(5)
        driver.find_element_by_link_text('攻略中心').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])

        print(driver.current_url, '*' * 20)
        input_ku = driver.find_element_by_id('search_content')
        input_ku.clear()
        time.sleep(2)
        input_ku.send_keys('之怒风暴迦娜')
        time.sleep(2)

        driver.find_element_by_class_name('r-spr').click()


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
