# -*- coding: utf-8 -*-
# @Time     : 2023/6/15
# @Author   : ycat
# @File     : api_util.py
from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get("/shouji/query", **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)


api_util = Api()
