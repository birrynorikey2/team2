import pytest
import retirement
from FullRetirementAge import *


# These next test are for checking it correctly calculates retirement age

def test_retirement_age1():
    a = get_retirement_age(1937, 2)
    assert a == (65, 0)


def test_retirement_age2():
    a = get_retirement_age(1938, 2)
    assert a == (65, 2)


def test_retirement_age3():
    a = get_retirement_age(1939, 2)
    assert a == (65, 4)


def test_retirement_age4():
    a = get_retirement_age(1940, 2)
    assert a == (65, 6)


def test_retirement_age5():
    a = get_retirement_age(1941, 2)
    assert a == (65, 8)


def test_retirement_age6():
    a = get_retirement_age(1942, 2)
    assert a == (65, 10)


def test_retirement_age7():
    a = get_retirement_age(1943, 2)
    assert a == (66, 0)


def test_retirement_age8():
    a = get_retirement_age(1954, 2)
    assert a == (66, 0)


def test_retirement_age9():
    a = get_retirement_age(1955, 2)
    assert a == (66, 2)


def test_retirement_age10():
    a = get_retirement_age(1956, 3)
    assert a == (66, 4)


def test_retirement_age11():
    a = get_retirement_age(1957, 5)
    assert a == (66, 6)


def test_retirement_age12():
    a = get_retirement_age(1958, 10)
    assert a == (66, 8)


def test_retirement_age13():
    a = get_retirement_age(1959, 11)
    assert a == (66, 10)


def test_retirement_age14():
    a = get_retirement_age(1967, 12)
    assert a == (67, 0)


def test_retirement_age_year_is_not_int():
    with pytest.raises(Exception):
        get_retirement_age("Invalid year", 1);

def test_retirement_age_month_is_not_int():
    with pytest.raises(Exception):
        get_retirement_age(2000, "Invalid month");

def test_retirement_age_invalid_year():
    with pytest.raises(Exception):
        get_retirement_age(-1, 1);

def test_retirement_age_invalid_year():
    with pytest.raises(Exception):
        get_retirement_age(2000, -1);
