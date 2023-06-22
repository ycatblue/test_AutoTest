# -*- coding: utf-8 -*-
# @Time     : 2023/6/21
# @Author   : ycat
# @File     : test_user.py
import allure
import pytest

from api.user_api import send_code, register, login
from testcases.conftest import get_data
from testcases.usercenter.conftest import get_code, delete_user, delete_code
from utils.read import base_data


@allure.feature("用户中心模块")
class TestUser:
    @allure.story("用户注册后登录")
    @allure.title("注册手机号测试用例")
    def test_register(self):
        json_data = get_data()['test_register']
        # 删除验证码
        delete_code(json_data['mobile'])
        # 发送验证码
        result = send_code(json_data)
        assert result.success is True
        mobile = result.body['mobile']
        # 获取短信验证码
        code = get_code(mobile)
        # 注册
        register_result = register(code, mobile)
        assert register_result.success is True
        # 删除用户
        delete_user(mobile)

    @pytest.mark.parametrize("username, password", get_data()['user_login'])
    @allure.story("用户登录")
    @allure.title("用户手机号登录测试用例")
    def test_login(self, username, password):
        print(username, password)
        login_result = login(username, password)
        assert login_result.success is True
        assert len(login_result.body['token']) != 0
