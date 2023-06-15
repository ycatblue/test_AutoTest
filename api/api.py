# -*- coding: utf-8 -*-
# @Time     : 2023/6/15
# @Author   : ycat
# @File     : api.py
from core.api_util import api_util


def mobile_query(params):
    respond = api_util.get_mobile_belong(params=params)
    return respond.json()


def test_json(json_data):
    """
    这个方法测试json传参
    :param json_data:
    :return:
    """
    respond = api_util.post_data(json=json_data)
    return respond.json()