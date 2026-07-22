import pytest

def test_addition():
    """测试加法"""
    assert 1 + 1 == 2

def test_subtraction():
    """测试减法"""
    assert 5 - 3 == 2

def test_with_fixture():
    """测试使用数据"""
    data = [1, 2, 3, 4, 5]
    assert len(data) == 5
    assert sum(data) == 15
