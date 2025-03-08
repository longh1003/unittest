import pytest
from divide import divide


def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(100, 1) == 100


def test_divide_to_zero():
    # with pytest.raises(ZeroDivisionError, match="Loi chia cho 0"): #ValueError in divide.py
    with pytest.raises(ValueError, match="Loi chia cho 0"):
        divide(1, 0)


def test_neg_divide_to_pos():
    assert divide(-3, 2) == -1.5
