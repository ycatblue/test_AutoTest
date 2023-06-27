# -*- coding: utf-8 -*-
# @Time     : 2023/6/26
# @Author   : ycat
# @File     : test_user_new.py
import allure
import pytest

from api.user_api_new import login_new
from testcases.conftest import get_data


@allure.feature("用户中心模块")
class TestUser:
    @pytest.mark.parametrize("data", get_data()['user_login_new'])
    @allure.story("用户登录")
    @allure.title("用户手机号登录测试用例")
    def test_login(self, data):
        print(data)
        # print(username, password)
        login_result = login_new(data)
        assert login_result.success is True
        # assert len(login_result.body['token']) != 0
