# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : test_fixture_params.py
import pytest


@pytest.fixture(params=["数据1", "数据2"], ids=["case1", "case2"])
def params_fixture(request):
    return request.param


def test_params(params_fixture):
    print(params_fixture)