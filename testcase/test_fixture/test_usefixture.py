# -*- coding: utf-8 -*-
# @Time     : 2023/6/14
# @Author   : ycat
# @File     : test_usefixture.py
import pytest


@pytest.mark.usefixtures("use_fixture1", "use_fixture2")
# @pytest.mark.usefixtures("use_fixture2")
def test_usefixture():
    print("userfixtures")