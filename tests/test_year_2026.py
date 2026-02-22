#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

import jpbizday

from . import common as c

YEAR = 2026
DAYS = 243
DAYS_OK = [[1, 5]]
DAYS_NG = [[1, 1], [1, 2], [1, 3], [1, 4]]
DAYS_PER_MONTH = [19, 18, 21, 21, 18, 22, 22, 20, 19, 21, 19, 23]
FIRST_BIZ_DAYS = [
    [1, 5],
    [2, 2],
    [3, 2],
    [4, 1],
    [5, 1],
    [6, 1],
    [7, 1],
    [8, 3],
    [9, 1],
    [10, 1],
    [11, 2],
    [12, 1],
]
LAST_BIZ_DAYS = [
    [1, 30],
    [2, 27],
    [3, 31],
    [4, 30],
    [5, 29],
    [6, 30],
    [7, 31],
    [8, 31],
    [9, 30],
    [10, 30],
    [11, 30],
    [12, 31],
]


def test_bizdays():
    assert (
        len(jpbizday.bizdays(datetime.date(YEAR, 1, 1), datetime.date(YEAR, 1, 18)))
        == 9
    )
    assert (
        len(jpbizday.bizdays(datetime.date(YEAR, 1, 1), datetime.date(YEAR, 2, 28)))
        == 37
    )
    assert (
        len(jpbizday.bizdays(datetime.date(YEAR, 5, 1), datetime.date(YEAR, 5, 16)))
        == 8
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
