# -*- coding: utf-8 -*-
# @Time     : 2023/6/8
# @Author   : ycat
# @File     : http_request.py
# @Remrk    : 写一个requests类方法
import requests


class HttpRequests:
    def get_requests(self, url, method, data, cookie=None):
        if method == 'get':
            http_request = requests.get(url=url, data=data, cookies=cookie)
            return http_request

        elif method == 'post':
            http_request = requests.post(url=url, data=data, cookies=cookie)
            return http_request

        else:
            print("输入的请求方法有误")


if __name__ == '__main__':
    data = {"shouji": "131", "appkey": "0c818521d38759e1"}
    r = requests.post("http://api.binstd.com/shouji/query", data)
    print(r.json())