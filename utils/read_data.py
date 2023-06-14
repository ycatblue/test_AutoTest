# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : read_data_test.py
import os
import yaml

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")


def read_data():
    f = open(path, encoding="utf-8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()