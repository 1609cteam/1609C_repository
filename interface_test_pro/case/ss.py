import requests
import json
class Cs():
    def __init__(self):
        self.url='http://127.0.0.1:8000/use/'
    def ge_t(self):
        req = requests.get(self.url)
        print(req.text)
        a = req.text[1:-1]
        c = json.loads(a)['id']
        c = str(c)
        print(req.status_code)
        #200
        return req.status_code
    def pos_t(self):
        sj={
            'name':'abc',
            'pwd':'abc'
        }
        req=requests.post(self.url,data=sj)
        print(req.status_code)
        #201
        return req.status_code
    def de_l(self):
        req = requests.get(self.url)
        a = req.text[1:-1]
        c = json.loads(a)['id']
        c = str(c)
        w=requests.delete(self.url+c)
        #204
        print(w.status_code)
        return w.status_code
    def pu_t(self):
        req = requests.get(self.url)
        a = req.text[1:-1]
        c = json.loads(a)['id']
        c = str(c)
        sj={
            'id':c,
            'name':'aaa',
            'pwd':'eeee'
        }
        w=requests.put(self.url+c+'/',data=sj)
        #200
        print(req.status_code)
        return w.status_code

if __name__ == '__main__':
    a=Cs()
    # a.ge_t()
    # a.pos_t()
    a.de_l()
    # a.pu_t()