#!/usr/bin/env python
# -*- coding:utf-8 -*-

import calendar
import datetime
import jpholiday
from functools import singledispatch


def is_bizday(day: datetime.date):
    """
    day が営業日か、否かを判定し、論理値を返します。 1/1 ～ 1/3 は祝日と判定します。 12 月の祝日はカレンダー通りに扱います。
    """
    if(jpholiday.is_holiday(day)):
        return(False)
    elif(day.weekday() == 5 or day.weekday() == 6):
        return(False)
    elif(day.month == 1 and day.day == 1):
        return(False)
    elif(day.month == 1 and day.day == 2):
        return(False)
    elif(day.month == 1 and day.day == 3):
        return(False)
    else:
        return(True)


def year_bizdays(year: int):
    """
    year 年の営業日をリストで返します。
    """
    day = datetime.date(year, 1, 1)
    result = []
    while(day.year == year):
        if(is_bizday(day)):
            result.append(day)
        day = day + datetime.timedelta(days=1)
    return(result)


def month_bizdays(year: int, month: int):
    """
    year 年 month 月の営業日をリストで返します。
    """
    day = datetime.date(year, month, 1)
    result = []
    while(day.month == month):
        if(is_bizday(day)):
            result.append(day)
        day = day + datetime.timedelta(days=1)
    return(result)


def bizdays(start: datetime.date, end: datetime.date):
    """
    start 日から end 日の間の営業日をリストで返します。
    """
    result = []
    while(start <= end):
        if(is_bizday(start)):
            result.append(start)
        start = start + datetime.timedelta(days=1)
    return(result)


@singledispatch
def first_bizday(year: int, month: int):
    """
    year 年 month 月の、最初の営業日を datetime.date で返します。
    """
    day = datetime.date(year, month, 1)
    while(not is_bizday(day)):
        day = day + datetime.timedelta(days=1)
    return(day)


@first_bizday.register(datetime.date)
def _first_bizday(day: datetime.date):
    """
    day 日を含む月の、最初の営業日を datetime.date で返します。
    """
    return(first_bizday(day.year, day.month))


@singledispatch
def last_bizday(year: int, month: int):
    """
    year 年 month 月の、最初の営業日を datetime.date で返します。
    """
    _, lastday = calendar.monthrange(year, month)
    day = datetime.date(year, month, lastday)
    while(not is_bizday(day)):
        day = day - datetime.timedelta(days=1)
    return(day)


@last_bizday.register(datetime.date)
def _last_bizday(day: datetime.date):
    """
    day 日を含む月の、最後の営業日を datetime.date で返します。
    """
    return(last_bizday(day.year, day.month))


def is_first_bizday(day: datetime.date):
    """
    day 日が、その月の最初の営業日か、否かを判定し、論理値を返します。
    """
    firstbizday = first_bizday(day)
    if(firstbizday == day):
        return(True)
    else:
        return(False)


def is_last_bizday(day: datetime.date):
    """
    day 日が、その月の最後の営業日か、否かを判定し、論理値を返します。
    """
    lastbizday = last_bizday(day)
    if(lastbizday == day):
        return(True)
    else:
        return(False)
