import pytest

@pytest.mark.skip(reason="skipping first method")
def test_sample1():
    a=2
    b=3
    assert a==b

def test_sample2():
    a=3
    b=3
    assert a==b
