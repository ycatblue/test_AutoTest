# -*- coding: utf-8 -*-
# @Time     : 2023/6/15
# @Author   : ycat
# @File     : test_post.py
import pytest

from api.api import test_json
from utils.read import base_data


def test_post():
    json_data = base_data.read_data()['json_data']
    result = test_json(json_data)
    assert result['id'] == 101


if __name__ == '__main__':
    pytest.main()
