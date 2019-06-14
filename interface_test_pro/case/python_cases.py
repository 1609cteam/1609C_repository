# 1.测试用例类
import requests


# 测试数据库清空操作
# from interface_test_pro.case import mysql


class Port_test():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/ban/'

    # 添加
    def port_post(self):
        data = {
            'id': 1,
            'name': '世界班2'
        }
        response = requests.post(self.url, data=data)
        print('增', response.text)
        return response.status_code

    # 修改
    def port_put(self):
        data = {
            'name': '中国班'
        }
        response = requests.put(self.url + '1/', data=data)
        print('改', response.text)
        return response.status_code

    # 查询
    def port_get(self):
        response = requests.get(self.url)
        print('查', response.text)
        return response.status_code

    # 删除
    def port_delete(self):
        response = requests.delete(self.url + '1/')
        print('删', response.text)
        return response.status_code


port = Port_test()
POST = port.port_post()
UPDATE = port.port_put()
SELECT = port.port_get()
DELETE = port.port_delete()
# 数据库清空操作
# mysql.mysql()
