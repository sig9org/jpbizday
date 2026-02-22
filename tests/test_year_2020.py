#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

import jpbizday


def test_is_bizday():
    assert jpbizday.is_bizday(datetime.date(2020, 1, 1)) is False
    assert jpbizday.is_bizday(datetime.date(2020, 1, 2)) is False
    assert jpbizday.is_bizday(datetime.date(2020, 1, 3)) is False
    assert jpbizday.is_bizday(datetime.date(2020, 1, 4)) is False
    assert jpbizday.is_bizday(datetime.date(2020, 1, 5)) is False
    assert jpbizday.is_bizday(datetime.date(2020, 1, 6)) is True


def test_year_bizday():
    assert len(jpbizday.year_bizdays(2020)) == 244


def test_month_bizday():
    assert len(jpbizday.month_bizdays(2020, 1)) == 19
    assert len(jpbizday.month_bizdays(2020, 2)) == 18
    assert len(jpbizday.month_bizdays(2020, 3)) == 21
    assert len(jpbizday.month_bizdays(2020, 4)) == 21
    assert len(jpbizday.month_bizdays(2020, 5)) == 18
    assert len(jpbizday.month_bizdays(2020, 6)) == 22
    assert len(jpbizday.month_bizdays(2020, 7)) == 21
    assert len(jpbizday.month_bizdays(2020, 8)) == 20
    assert len(jpbizday.month_bizdays(2020, 9)) == 20
    assert len(jpbizday.month_bizdays(2020, 10)) == 22
    assert len(jpbizday.month_bizdays(2020, 11)) == 19
    assert len(jpbizday.month_bizdays(2020, 12)) == 23


def test_bizdays():
    assert (
        len(jpbizday.bizdays(datetime.date(2020, 1, 1), datetime.date(2020, 1, 18)))
        == 9
    )
    assert (
        len(jpbizday.bizdays(datetime.date(2020, 1, 1), datetime.date(2020, 2, 29)))
        == 37
    )
    assert (
        len(jpbizday.bizdays(datetime.date(2020, 5, 1), datetime.date(2020, 5, 16)))
        == 8
    )


def test_first_bizday_month():
    assert jpbizday.first_bizday(2020, 1) == datetime.date(2020, 1, 6)
    assert jpbizday.first_bizday(2020, 2) == datetime.date(2020, 2, 3)
    assert jpbizday.first_bizday(2020, 3) == datetime.date(2020, 3, 2)
    assert jpbizday.first_bizday(2020, 4) == datetime.date(2020, 4, 1)
    assert jpbizday.first_bizday(2020, 5) == datetime.date(2020, 5, 1)
    assert jpbizday.first_bizday(2020, 6) == datetime.date(2020, 6, 1)
    assert jpbizday.first_bizday(2020, 7) == datetime.date(2020, 7, 1)
    assert jpbizday.first_bizday(2020, 8) == datetime.date(2020, 8, 3)
    assert jpbizday.first_bizday(2020, 9) == datetime.date(2020, 9, 1)
    assert jpbizday.first_bizday(2020, 10) == datetime.date(2020, 10, 1)
    assert jpbizday.first_bizday(2020, 11) == datetime.date(2020, 11, 2)
    assert jpbizday.first_bizday(2020, 12) == datetime.date(2020, 12, 1)


def test_first_bizday_day():
    assert jpbizday.first_bizday(datetime.date(2020, 1, 1)) == datetime.date(2020, 1, 6)
    assert jpbizday.first_bizday(datetime.date(2020, 2, 1)) == datetime.date(2020, 2, 3)
    assert jpbizday.first_bizday(datetime.date(2020, 3, 1)) == datetime.date(2020, 3, 2)
    assert jpbizday.first_bizday(datetime.date(2020, 4, 1)) == datetime.date(2020, 4, 1)
    assert jpbizday.first_bizday(datetime.date(2020, 5, 1)) == datetime.date(2020, 5, 1)
    assert jpbizday.first_bizday(datetime.date(2020, 6, 1)) == datetime.date(2020, 6, 1)
    assert jpbizday.first_bizday(datetime.date(2020, 7, 1)) == datetime.date(2020, 7, 1)
    assert jpbizday.first_bizday(datetime.date(2020, 8, 1)) == datetime.date(2020, 8, 3)
    assert jpbizday.first_bizday(datetime.date(2020, 9, 1)) == datetime.date(2020, 9, 1)
    assert jpbizday.first_bizday(datetime.date(2020, 10, 1)) == datetime.date(
        2020, 10, 1
    )
    assert jpbizday.first_bizday(datetime.date(2020, 11, 1)) == datetime.date(
        2020, 11, 2
    )
    assert jpbizday.first_bizday(datetime.date(2020, 12, 1)) == datetime.date(
        2020, 12, 1
    )


def test_last_bizday_month():
    assert jpbizday.last_bizday(2020, 1) == datetime.date(2020, 1, 31)
    assert jpbizday.last_bizday(2020, 2) == datetime.date(2020, 2, 28)
    assert jpbizday.last_bizday(2020, 3) == datetime.date(2020, 3, 31)
    assert jpbizday.last_bizday(2020, 4) == datetime.date(2020, 4, 30)
    assert jpbizday.last_bizday(2020, 5) == datetime.date(2020, 5, 29)
    assert jpbizday.last_bizday(2020, 6) == datetime.date(2020, 6, 30)
    assert jpbizday.last_bizday(2020, 7) == datetime.date(2020, 7, 31)
    assert jpbizday.last_bizday(2020, 8) == datetime.date(2020, 8, 31)
    assert jpbizday.last_bizday(2020, 9) == datetime.date(2020, 9, 30)
    assert jpbizday.last_bizday(2020, 10) == datetime.date(2020, 10, 30)
    assert jpbizday.last_bizday(2020, 11) == datetime.date(2020, 11, 30)
    assert jpbizday.last_bizday(2020, 12) == datetime.date(2020, 12, 31)


def test_last_bizday_day():
    assert jpbizday.last_bizday(datetime.date(2020, 1, 1)) == datetime.date(2020, 1, 31)
    assert jpbizday.last_bizday(datetime.date(2020, 2, 1)) == datetime.date(2020, 2, 28)
    assert jpbizday.last_bizday(datetime.date(2020, 3, 1)) == datetime.date(2020, 3, 31)
    assert jpbizday.last_bizday(datetime.date(2020, 4, 1)) == datetime.date(2020, 4, 30)
    assert jpbizday.last_bizday(datetime.date(2020, 5, 1)) == datetime.date(2020, 5, 29)
    assert jpbizday.last_bizday(datetime.date(2020, 6, 1)) == datetime.date(2020, 6, 30)
    assert jpbizday.last_bizday(datetime.date(2020, 7, 1)) == datetime.date(2020, 7, 31)
    assert jpbizday.last_bizday(datetime.date(2020, 8, 1)) == datetime.date(2020, 8, 31)
    assert jpbizday.last_bizday(datetime.date(2020, 9, 1)) == datetime.date(2020, 9, 30)
    assert jpbizday.last_bizday(datetime.date(2020, 10, 1)) == datetime.date(
        2020, 10, 30
    )
    assert jpbizday.last_bizday(datetime.date(2020, 11, 1)) == datetime.date(
        2020, 11, 30
    )
    assert jpbizday.last_bizday(datetime.date(2020, 12, 1)) == datetime.date(
        2020, 12, 31
    )


def test_is_first_bizday():
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 1)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 3)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 4)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 5)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 6)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 1, 7)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 2, 1)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 2, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 2, 3)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 2, 4)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 3, 1)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 3, 2)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 3, 3)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 4, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 4, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 5, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 5, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 6, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 6, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 7, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 7, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 8, 1)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 8, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 8, 3)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 8, 4)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 9, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 9, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 10, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 10, 2)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 11, 1)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 11, 2)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 11, 3)) is False
    assert jpbizday.is_first_bizday(datetime.date(2020, 12, 1)) is True
    assert jpbizday.is_first_bizday(datetime.date(2020, 12, 2)) is False


def test_is_last_bizday():
    assert jpbizday.is_last_bizday(datetime.date(2020, 1, 31)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 1, 30)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 2, 29)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 2, 28)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 2, 27)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 3, 31)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 3, 30)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 4, 30)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 4, 29)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 5, 31)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 5, 30)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 5, 29)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 5, 28)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 6, 30)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 6, 29)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 7, 31)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 7, 30)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 8, 31)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 8, 30)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 9, 30)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 9, 29)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 10, 31)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 10, 30)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 10, 29)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 11, 30)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 11, 29)) is False
    assert jpbizday.is_last_bizday(datetime.date(2020, 12, 31)) is True
    assert jpbizday.is_last_bizday(datetime.date(2020, 12, 30)) is False
