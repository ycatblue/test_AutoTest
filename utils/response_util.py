# -*- coding: utf-8 -*-
# @Time     : 2023/6/16
# @Author   : ycat
# @File     : response_util.py
import json

from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code == 200 or response.status_code == 201:
        ResultResponse.success = True
        ResultResponse.body = response.json()
        logger.info("接口的返回内容>>>:" + json.dumps(response.json(), ensure_ascii=False))
    else:
        ResultResponse.success = False
        logger.info("接口状态码不是2开头，请检查" + json.dumps(response.json(), ensure_ascii=False))
    return ResultResponse