import pytest

@pytest.mark.smoke
def test_a():
    print("hai")

@pytest.mark.regression
def test_b():
    a=5
    b=3
    assert a!=b

@pytest.mark.smoke
def test_c():
    s="hello"
    s2="hello"
    assert s.__eq__(s2)
