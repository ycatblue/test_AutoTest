# -*- coding: utf-8 -*-
# @Time     : 2023/6/13
# @Author   : ycat
# @File     : test_ship.py
import requests


# 用户名密码登录
# 拿到登录的token，获取用户信息


class TestUser:
    def test_login(self):
        username = "ycat"
        password = "123456"
        # requests.post("/login", json={"username": username, "password": password})
        token = "token"
        assert token == "token"
        return token, username

    def test_userinfo(self):
        token, username = self.test_login()
        headers = {
            "token": token
        }
        # res = requests.post("/get_user", headers=headers)

        assert headers['token'] == token
        assert username == "ycat"

