import requests


# from interface_test_pro.run import MyTest


class Rzm():
    def __init__(self):
        self.url = 'http://10.30.29.53:9000/book_type/'

    # 查询
    def Get_Api(self):
        response = requests.get(self.url)

        return response.status_code

    # 添加
    def Post_Api(self, data):
        response = requests.post(self.url, data=data)

        return response.status_code

    # 删除
    def Delete_Api(self, url):
        response = requests.delete(url)

        return response.status_code

    # 修改
    def Put_Api(self, data, number):
        response = requests.put(self.url + str(number) + "/", data=data)

        return response.status_code

    # 另一种修改
    # def Put_Api(self, data, number):
    #     response = requests.patch(self.url+str(number)+"/", data=data)
    #
    #     return response.status_code
