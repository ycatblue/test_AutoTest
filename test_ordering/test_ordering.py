# -*- coding: utf-8 -*-
# @Time     : 2023/6/12
# @Author   : ycat
# @File     : test_ordering.py
import pytest


def test_search():
    print("search...")


def test_order():
    print("order...")


def test_pay():
    print("pay...")


@pytest.mark.run(order=1)
def test_login():
    print("login...")
