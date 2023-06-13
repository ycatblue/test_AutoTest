# -*- coding: utf-8 -*-
# @Time     : 2023/6/12
# @Author   : ycat
# @File     : test_two.py
import pytest


@pytest.mark.pro
class TestThree:

    def test_one(self):
        expect = 1
        actual = 1
        assert expect == actual

    def test_two(self):
        expect = 1
        actual = 2
        assert expect == actual