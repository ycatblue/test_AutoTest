# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : test.py
import os
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml"))