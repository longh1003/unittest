import pytest
from sum_list import sum_list


def test_sum_list_equal_zero():
    assert sum_list([]) == 0


def test_sum_list_one_element():
    assert sum_list([1]) == 1


def test_sum_list_total():
    assert sum_list([1, 2, 3, 4]) == 10


def test_sum_list_total_neg():
    assert sum_list([-1, 2, -3, 4, -5]) == -3
