# -*- coding: utf-8 -*-
# @Time     : 2023/6/13
# @Author   : ycat
# @File     : test_mobile.py
import pytest
import requests
from utils.read_data import get_data
from utils.read_ini import read_ini
url = read_ini()['host']['api_sit_url']


@pytest.mark.parametrize('mobile, appkey', get_data['mobile_belong_get'])
def test_mobile(mobile, appkey):
    print("测试手机号归属地get请求")
    r = requests.get(url+"/shouji/query",
                     params={"shouji": mobile, "appkey": appkey})
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


@pytest.mark.parametrize('mobile, appkey', get_data['mobile_belong_post'])
def test_mobile_post(mobile, appkey):
    print("测试手机号归属地post请求")
    params = {
        "shouji": mobile,
        "appkey": appkey
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