import requests

class Test_Interface():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/book/'
    #查询
    def Get_Api(self):
        response = requests.get(self.url)

        return response.status_code
    #修改
    def Put_Api(self):
        query = {
            "id": 1,
            "name": "朱阳阳",
            "price": 1.0
        }
        response = requests.put(self.url+'1/',data=query)
        return response.status_code
    #删除
    def delete_api(self):

        response = requests.delete(self.url+'1/')
        #204
        return response.status_code

    #添加
    def Post_Api(self):
        query = {
            "name":'刘书杰',
            'price':600
        }
        response = requests.post(self.url,data=query)
        return response.status_code

yy = Test_Interface()
SELECT = yy.Get_Api()
POST = yy.Post_Api()
UPDATE = yy.Put_Api()
DELETE = yy.delete_api()


