# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : test_parametrize_02.py
import pytest

from utils.read_data import get_data

# 单参数
# @pytest.mark.parametrize("name", get_data['heroes_name'])
# def test_parametrize_02(name):
#     print(name)


# 多参数
@pytest.mark.parametrize("name, attribute", get_data['heroes_name_attribute'])
def test_parametrize_02(name, attribute):
    print(f'{name}的属性是{attribute}')