# -*- coding: utf-8 -*-
# @Time     : 2023/6/15
# @Author   : ycat
# @File     : api.py
import json

from core.api_util import api_util
from utils.log_util import logger
from utils.response_util import process_response


def mobile_query(params):
    response = api_util.get_mobile_belong(params=params)
    result = process_response(response)
    return result


def test_json(json_data):
    """
    这个方法测试json传参
    :param json_data:
    :return:
    """
    respond = api_util.post_data(json=json_data)
    return respond.json()