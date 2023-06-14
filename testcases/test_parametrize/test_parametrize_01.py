# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : test_parametrize_01.py
import pytest


# 单参数单次循环
# @pytest.mark.parametrize("name", ["ycat"])
# def test_parametrize(name):
#     print("我是"+name)

# 单参数多次循环
# 运行时，将数组里的值分别赋值给变量，每赋值一次，运行一次
@pytest.mark.parametrize("name", ["安琪拉", "廉颇", "鲁班七号"])
def test_parametrize(name):
    assert name == "安琪拉"


