import pytest

@pytest.mark.xfail(reason="expected to fail until we fix the bug")
def test_sample_one():
    a=5
    b=10
    assert a==b

@pytest.mark.xfail(reason="expected to pass")
def test_sample_two():
    a=5
    b=5
    assert a==b

def test_sample_three():
    a="saran"
    b="saran"
    assert a.__eq__(b)