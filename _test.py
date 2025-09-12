import pytest
from app import calculate_power

def test_positive_power():
    assert calculate_power(2,3) == 8, "test failed : ❌ 2^3 should be 8"
    assert calculate_power(5,2) == 25, "test failed : ❌ 5^2 should be 25"

def test_zero_power():
    assert calculate_power(10,0) == 1, "test failed : ❌ power raised to 0 should always be 1"
    assert calculate_power(102,0) == 1, "test failed : ❌ power raised to 0 should always be 1"

def test_negative_power():
    assert calculate_power(2, -2) == 0.25, "test failed : ❌ 2^-2 should be 0.25"
    assert calculate_power(5, -1) == 0.2, "test failed : ❌ 5^-1 should be 0.2"

def test_one_power():
    assert calculate_power(7, 1) == 7, "test failed : ❌ 7^1 should be 7"
    assert calculate_power(1, 100) == 1, "test failed : ❌ 1^100 should be 1"

def test_large_power():
    assert calculate_power(2, 10) == 1024, "test failed : ❌ 2^10 should be 1024"
