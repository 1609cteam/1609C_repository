from selenium import webdriver
import unittest,time,requests
from ddt import ddt,data
# 引入日志类
from interface_test_pro.case.my_log import *

rz=Create_log() # 实例化
log01=rz.get_log() # 使用方法

# 获取状态码函数
def get_code(url):
    code=requests.get(url)
    # print(code.status_code,'***')
    return code.status_code

class Shop(unittest.TestCase):  # 继承
    def setUp(self):
        print('开始测试...')
        # log
        log01.debug('开始测试...')
        self.drv=webdriver.Chrome()
        # 请求本地路由-查询/修改id为1的类型
        # self.drv.get('http://127.0.0.1:8000/sps/')

    def tearDown(self):
        print('测试结束!')

    # 添加商品
    def test_sptj(self):
        self.drv.get('http://127.0.0.1:8000/sps/')
        print('正在测试添加商品...')
        # log
        # log.debug('正在测试添加...')
        time.sleep(1)
        name=self.drv.find_element_by_name('name').send_keys('山羊肉')
        time.sleep(1)
        price=self.drv.find_element_by_name('price').send_keys(22)
        time.sleep(1)
        jj=self.drv.find_element_by_name('jj').send_keys('补充营养')
        # time.sleep(1)
        lx=self.drv.find_element_by_name('lx').find_elements_by_xpath('./option')
        # 点击蔬菜类--输入类型
        lx[0].click()
        # 点击添加
        dj = self.drv.find_element_by_class_name('form-actions').find_element_by_tag_name('button').click()
        time.sleep(3)
        # 获取提交添加后的状态码
        codes=self.drv.find_element_by_xpath('//*[@id="content"]/div[2]/div[4]/pre/span[1]/b[1]').text
        code=int(codes[5:8])
        print('状态码为:',code)
        time.sleep(1)

        #-----requests获取状态码----------
        # # 获取当前路由
        # url=self.drv.current_url
        # # 调用获取状态码函数
        # code=get_code(url)
        # print('状态码为:',code)
        #---------------------------------

        # 断言--和返回的状态码进行匹配是否修改成功.
        self.assertEqual(code, 201, msg='添加失败!!!')
        time.sleep(6)


    # 修改商品----------------------------------------
    def test_spxg(self):
        self.drv.get('http://127.0.0.1:8000/sps/10')
        print('正在测试修改商品...')
        # log
        log01.debug('正在测试修改...')
        time.sleep(1)
        inp1=self.drv.find_element_by_class_name('form-control')
        time.sleep(1)
        inp1.clear()
        inp1.send_keys('圣女果')
        # 点击put按钮进行修改
        dj=self.drv.find_element_by_class_name('form-actions').find_element_by_tag_name('button').click()
        time.sleep(3)
        # 获取当前路由
        url=self.drv.current_url
        # 调用获取状态码函数
        code=get_code(url)
        print('状态码为:',code)
        # 断言--和返回的状态码进行匹配是否修改成功.
        self.assertEqual(code, 200, msg='修改失败!!!')
        time.sleep(6)



    # 删除操作----------------------------------------
    def test_spsc(self):
        self.drv.get('http://127.0.0.1:8000/sps/15')
        # 点击删除
        dj = self.drv.find_element_by_xpath('//*[@id="content"]/div[1]/button').click()
        time.sleep(3)
        dj1=self.drv.find_element_by_xpath('//*[@id="deleteModal"]/div/div/div[2]/form/button').click()
        # 获取当前路由
        url=self.drv.current_url
        # 调用获取状态码函数
        code=get_code(url)
        print('状态码为:',code)
        # 断言--和返回的状态码进行匹配是否修改成功.
        self.assertEqual(code, 404, msg='删除失败!!!')
        time.sleep(6)


    # 查询所有商品-------------------------------------
    def test_spck(self):
        self.drv.get('http://127.0.0.1:8000/sps/')
        # 获取当前路由
        url = self.drv.current_url
        # 调用获取状态码函数
        code = get_code(url)
        print('状态码为:', code)
        # 断言--和返回的状态码进行匹配是否修改成功.
        self.assertEqual(code, 200, msg='查询失败!!!')
        time.sleep(6)


if __name__ == '__main__':
    unittest.main()






