# -*- coding: utf-8 -*-
# @Time     : 2023/6/22
# @Author   : ycat
# @File     : conftest.py
from utils.read import base_data


def get_data():
    return base_data.read_data()