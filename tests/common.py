#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

import jpbizday


def case_is_bizday(year: int, days: list, result: bool = True):
    for _ in days:
        _year = year
        _month = _[0]
        _day = _[1]
        assert jpbizday.is_bizday(datetime.date(_year, _month, _day)) is result


def case_year_bizday(year: int, days: int):
    assert len(jpbizday.year_bizdays(year)) == days


def case_month_bizday(year: int, days: list):
    for i, _ in enumerate(days):
        month = i + 1
        assert len(jpbizday.month_bizdays(year, month)) == _


def case_first_bizday_month(year: int, days: list):
    for i, _ in enumerate(days):
        month = i + 1
        assert jpbizday.first_bizday(year, month) == datetime.date(year, _[0], _[1])


def case_last_bizday_month(year: int, days: list):
    for i, _ in enumerate(days):
        month = i + 1
        assert jpbizday.last_bizday(year, month) == datetime.date(year, _[0], _[1])
