import pytest
from two_sum import sum_two_num

def test_case_1():
    nums = [2,7,11,15]
    target = 9
    result = sum_two_num(nums, target)
    expected = [0, 1]
    assert result == expected

def test_case_2():
    nums = [3,2,4]
    target = 6
    result = sum_two_num(nums, target)
    expected = [1,2]
    assert result == expected

def test_case_3():
    nums = [3,3]
    target = 6
    result = sum_two_num(nums, target)
    expected = [0,1]
    assert result == expected