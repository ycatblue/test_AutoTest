# -*- coding: utf-8 -*-
# @Time     : 2023/6/26
# @Author   : ycat
# @File     : user_api_new.py
from core.rest_client_new import api_util_new
from utils.response_util import process_response


def login_new(data):
    response = api_util_new.do_request(url=data['url'], method=data['method'], json=data['data'])
    return process_response(response)