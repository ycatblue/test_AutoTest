# -*- coding: utf-8 -*-
# @Time     : 2023/6/15
# @Author   : ycat
# @File     : read_ini.py
import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")


def read_ini():
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8")
    return config


get_ini = read_ini()

# print(read_ini()['host']['api_sit_url'])
