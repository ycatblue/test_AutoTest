# -*- coding: utf-8 -*-
# @Time     : 2023/6/13
# @Author   : ycat
# @File     : test_fixture_order.py
import pytest


@pytest.fixture(scope="session")
def t_session():
    print("我是session fixture")


@pytest.fixture(scope="module")
def t_module():
    print("我是module fixture")


@pytest.fixture(scope="class")
def t_class():
    print("我是class fixture")


@pytest.fixture(scope="function")
def t_function():
    print("我是function fixture")


class TestOrder:
    def test_order(self, t_module, t_class, t_function, test_session):
        assert 1 == 1

