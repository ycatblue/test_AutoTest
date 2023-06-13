# -*- coding: utf-8 -*-
# @Time     : 2023/6/12
# @Author   : ycat
# @File     : test_get_param.py
import requests


def test_mobile():
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
 