import requests
import json
class Book():
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/books/'
    def ge_t(self):
        a = requests.get(self.url)
        a_text = a.text[1:-1]
        id = json.loads(a_text)['id']
        # print(id)
        # print(a_text)
        print(a.status_code)
        return  a.status_code
    def pos_t(self):

        data = {
            'name':'水浒传'
        }
        a = requests.post(self.url,data=data)
        print(a.status_code)
        return a.status_code
    def pu_t(self):
        a = requests.get(self.url)
        a_text = a.text[1:-1]
        id = json.loads(a_text)['id']
        data = {
            'id':id,
            'name':'水浒'
        }
        a = requests.put(self.url+str(id)+'/',data=data)
        print(a.status_code)
        return a.status_code
    def delet_e(self):
        a = requests.get(self.url)
        a_text = a.text[1:-1]
        id = json.loads(a_text)['id']
        a = requests.delete(self.url+str(id)+'/')
        print(a.status_code)
        return a.status_code
if __name__ == '__main__':
    bo = Book()
    bo.ge_t()
    # bo.pos_t()
    # bo.pu_t()
    # bo.delet_e()
