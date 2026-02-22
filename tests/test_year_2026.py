#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

import jpbizday


def test_is_bizday():
    assert jpbizday.is_bizday(datetime.date(2026, 1, 1)) is False
    assert jpbizday.is_bizday(datetime.date(2026, 1, 2)) is False
    assert jpbizday.is_bizday(datetime.date(2026, 1, 3)) is False
    assert jpbizday.is_bizday(datetime.date(2026, 1, 4)) is False
    assert jpbizday.is_bizday(datetime.date(2026, 1, 5)) is True


def test_year_bizday():
    assert len(jpbizday.year_bizdays(2026)) == 243
