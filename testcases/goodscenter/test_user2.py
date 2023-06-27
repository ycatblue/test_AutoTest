# -*- coding: utf-8 -*-
# @Time     : 2023/6/21
# @Author   : ycat
# @File     : test_user.py
import allure
import pytest

from api.user_api import send_code, register, login, add_shopping_cart
from testcases.conftest import get_data
from testcases.usercenter.conftest import get_code, delete_user, delete_code, get_shop_cart_num
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("购物车")
    @allure.title("加购物车测试用例")
    def test_shopping_cart2(self, login_fixture):
        token = login_fixture[0]
        username = login_fixture[1]
        param = get_data()['shopping_cart']
        result = add_shopping_cart(param, token)
        # 查询购物车数量
        num = get_shop_cart_num(username, param['goods'])
        assert result.success is True
        assert result.body['nums'] == num

