import requests


class Test_yl():


    def send_put(self,url,data):

        res = requests.post(url=url,data=data)

        return res


    def send_get(self,url,data):

        res = requests.get(url=url,data=data)

        return res.status_code


    def send_post(self,url,ress):

        # ress = {
        #
        #     "name": "ggg"
        # }

        res = requests.post(url=url,data=ress)

        return res.status_code

    def send_put(self,url,ress):


        res = requests.put(url=url,data=ress)
        print(res.status_code)
        return res.status_code


    def send_delete(self,url):

        res = requests.delete(url=url)

        print(res.status_code)

        return res.status_code

# test = Test_yl()
#
# test.send_get("http://127.0.0.1:8000/book_type/1/",'1')
#
# test.send_post("http://127.0.0.1:8000/goodstype/")
#
# test.send_put("http://127.0.0.1:8000/book_type/1/")
#
# test.send_delete('http://127.0.0.1:8000/book_type/5/')