#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

import jpbizday

from . import common as c

YEAR = 2027
DAYS = 245
DAYS_OK = [[1, 4], [1, 5]]
DAYS_NG = [[1, 1], [1, 2], [1, 3]]
DAYS_PER_MONTH = [19, 18, 22, 21, 18, 22, 21, 21, 20, 20, 20, 23]
FIRST_BIZ_DAYS = [
    [1, 4],
    [2, 1],
    [3, 1],
    [4, 1],
    [5, 6],
    [6, 1],
    [7, 1],
    [8, 2],
    [9, 1],
    [10, 1],
    [11, 1],
    [12, 1],
]
LAST_BIZ_DAYS = [
    [1, 29],
    [2, 26],
    [3, 31],
    [4, 30],
    [5, 31],
    [6, 30],
    [7, 30],
    [8, 31],
    [9, 30],
    [10, 29],
    [11, 30],
    [12, 31],
]


def test_bizdays():
    assert (
        len(jpbizday.bizdays(datetime.date(YEAR, 1, 1), datetime.date(YEAR, 1, 18)))
        == 10
    )
    assert (
        len(jpbizday.bizdays(datetime.date(YEAR, 1, 1), datetime.date(YEAR, 2, 28)))
        == 37
    )
    assert (
        len(jpbizday.bizdays(datetime.date(YEAR, 5, 1), datetime.date(YEAR, 5, 16)))
        == 7
    )


def test_is_bizday():
    c.case_is_bizday(year=YEAR, days=DAYS_OK, result=True)
    c.case_is_bizday(year=YEAR, days=DAYS_NG, result=False)


def test_year_bizday():
    c.case_year_bizday(year=YEAR, days=DAYS)


def test_month_bizday():
    c.case_month_bizday(year=YEAR, days=DAYS_PER_MONTH)


def test_first_bizday_month():
    c.case_first_bizday_month(year=YEAR, days=FIRST_BIZ_DAYS)


def test_last_bizday_month():
    c.case_last_bizday_month(year=YEAR, days=LAST_BIZ_DAYS)
