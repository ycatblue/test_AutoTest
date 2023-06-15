# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : yaml_util.py
import random

from faker import Faker
fake = Faker(locale="zh-CN")


def func_yaml(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if '${' and '}' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                func_name = str(value)[start+2:end]
                data[key] = str(value)[0:start]+str(eval(func_name))+str(value)[end+1:len(str(value))]
    return data


def random_name():
    return fake.name()


def age():
    return random.randint(20, 50)


if __name__ == '__main__':
    data = {"name": "上海-${random_name()}", "age": "${age()}", "sex": "woman"}
    print(func_yaml(data))