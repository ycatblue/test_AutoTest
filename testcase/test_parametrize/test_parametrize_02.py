# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : test_parametrize_02.py
import pytest

# 元组的形式
# @pytest.mark.parametrize("name, attribute", [("安琪拉", "法师"), ("廉颇", "战士"), ("射手", "鲁班七号")])
# def test_parametrize_02(name, attribute):
#     print("英雄"+name+"属性是"+attribute)


# 数组的形式
# @pytest.mark.parametrize("name, attribute", [["安琪拉", "法师"], ["廉颇", "战士"], ["射手", "鲁班七号"]])
# def test_parametrize_02(name, attribute):
#     print("英雄"+name+"属性是"+attribute)

# @pytest.mark.parametrize("name, attribute", [["安琪拉", "法师"]])
# def test_parametrize_02(name, attribute):
#     print("英雄"+name+"属性是"+attribute)


@pytest.mark.parametrize("hero", [{"name": "安琪拉", "attribute": "法师"}, {"name": "廉颇", "attribute": "战士"},
                                  {"name": "鲁班七号", "attribute": "射手"}])
def test_parametrize_02(hero):
    print("英雄"+hero['name']+",属性是"+hero['attribute'])


