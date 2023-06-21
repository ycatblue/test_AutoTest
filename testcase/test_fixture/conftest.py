# -*- coding: utf-8 -*-
# @Time     : 2023/6/13
# @Author   : ycat
# @File     : conftest.py
import pytest


@pytest.fixture(scope="session", autouse=True)
def test_session():
    print("我是session级的fixture")


@pytest.fixture(scope="function")
def test_func1():
    print("我是func1级别的fixture")


@pytest.fixture(scope="function")
def test_func2():
    print("我是func2级别的fixture")


@pytest.fixture(scope="function")
def get_params():
    params = {"shouji": "13456755448", "appkey": "0c818521d38759e1"}
    return params


@pytest.fixture(scope='function', autouse=True)
def func():
    print('我是前置步骤')
    yield
    print('我是后置步骤')


@pytest.fixture(scope='function')
def use_fixture1():
    fixtures = 2
    print("我现在使用use_fixtures1")
    return fixtures


@pytest.fixture(scope='function')
def use_fixture2():
    fixtures = 2
    print("我现在使用use_fixtures2")
    return fixtures
