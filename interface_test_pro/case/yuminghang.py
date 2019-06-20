#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 11:38
# @Author  : 蔚明杭
# @Site    :
# @File    : yuminghang.py
# @Software: PyCharm

import requests
import time

updatetime = time.strftime('%Y-%M-%d')
class RunMain():
    # 增加
    def send_post(self, url, data):
        result_post = requests.post(url=url, data=data)
        # print(result_post.status_code)
        # print(result_post.text)
        return result_post

    # 查询
    def send_get(self, url, data):
        result_get = requests.get(url=url, data=data)
        # print(result_get.text)
        # print(result_get.status_code)
        return result_get

    # 修改
    def send_put(self,url,data):
        result_put = requests.put(url=url,data=data)
        # print(result_put.status_code)
        # print(result_put.text)
        return result_put
