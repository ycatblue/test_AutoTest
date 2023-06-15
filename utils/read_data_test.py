# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : read_data_test.py
import yaml

f = open("../data/data.yaml", encoding="utf-8")
data = yaml.safe_load(f)
# print(data['hero'])
# print(data['heroes'])
# print(data['heroes_name'])
# print(data['heroes_name_list'])
# print(data['test'])
# print(data['test']['name'])
print(data['mobile_belong_get'])
