# -*- coding: utf-8 -*-
# @Time     : 2023/6/22
# @Author   : ycat
# @File     : goods_api.py
from core.api_util import api_util
from utils.response_util import process_response


def get_banner():
    """
    获取banner接口
    :return:
    """
    response = api_util.banner()
    return process_response(response)