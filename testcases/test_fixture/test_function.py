# -*- coding: utf-8 -*-
# @Time     : 2023/6/13
# @Author   : ycat
# @File     : test_function.py
import requests
import pytest


# 默认scope是function
# @pytest.fixture(autouse=True)
# def func():
#     print("我是前置步骤")


def test_mobile(test_func1, test_func2):
    print("测试手机号归属地get请求")
    r = requests.get("http://api.binstd.com/shouji/query",
                     params={"shouji": "13456755448", "appkey": "0c818521d38759e1"})
    # print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "浙江"
    assert result['result']["city"] == "杭州"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


def test_mobile_post(test_func2):
    print("测试手机号归属地post请求")
    params = {
        "shouji": "13456755448",
        "appkey": "0c818521d38759e1"
    }
    r = requests.post('http://api.binstd.com/shouji/query', params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13456755448"
    assert result['result']["province"] == "浙江"
    assert result['result']["city"] == "杭州"
    assert result['result']["company"] == "中国移动"
    assert result['result']["cardtype"] is None
    assert result['result']["areacode"] == "0571"


if __name__ == '__main__':
    pytest.main()