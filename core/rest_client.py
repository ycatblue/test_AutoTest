# -*- coding: utf-8 -*-
# @Time     : 2023/6/15
# @Author   : ycat
# @File     : rest_client.py
import requests

from utils.read import base_data

api_root_url = base_data.read_ini()['host']['api_sit_url']
post_url = base_data.read_ini()['host']['post_url']


class RestClient:
    def __init__(self):
        self.api_root_url = api_root_url

    def get(self, url, **kwargs):
        return requests.get(api_root_url+url, **kwargs)

    def post(self, url, **kwargs):
        return requests.post(post_url+url, **kwargs)
