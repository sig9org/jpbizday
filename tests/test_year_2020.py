#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import unittest
from jpbizday import jpbizday


class TestYear2020(unittest.TestCase):
    """
    jpbizday のテスト用クラスです。 2020 年関連のユニットテストを実行します。
    """


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def test_is_bizday(self):
        self.assertEqual(jpbizday.is_bizday(datetime.date(2020, 1, 1)), False)
        self.assertEqual(jpbizday.is_bizday(datetime.date(2020, 1, 2)), False)
        self.assertEqual(jpbizday.is_bizday(datetime.date(2020, 1, 3)), False)
        self.assertEqual(jpbizday.is_bizday(datetime.date(2020, 1, 4)), False)
        self.assertEqual(jpbizday.is_bizday(datetime.date(2020, 1, 5)), False)
        self.assertEqual(jpbizday.is_bizday(datetime.date(2020, 1, 6)), True)


    def test_year_bizday(self):
        self.assertEqual(len(jpbizday.year_bizdays(2020)), 244)


    def test_month_bizday(self):
        self.assertEqual(len(jpbizday.month_bizdays(2020, 1)), 19)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 2)), 18)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 3)), 21)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 4)), 21)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 5)), 18)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 6)), 22)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 7)), 21)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 8)), 20)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 9)), 20)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 10)), 22)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 11)), 19)
        self.assertEqual(len(jpbizday.month_bizdays(2020, 12)), 23)


    def test_bizdays(self):
        self.assertEqual(len(jpbizday.bizdays(datetime.date(2020, 1, 1), datetime.date(2020, 1, 18))), 9)
        self.assertEqual(len(jpbizday.bizdays(datetime.date(2020, 1, 1), datetime.date(2020, 2, 29))), 37)
        self.assertEqual(len(jpbizday.bizdays(datetime.date(2020, 5, 1), datetime.date(2020, 5, 16))), 8)


    def test_first_bizday_month(self):
        self.assertEqual(jpbizday.first_bizday(2020, 1), datetime.date(2020, 1, 6))
        self.assertEqual(jpbizday.first_bizday(2020, 2), datetime.date(2020, 2, 3))
        self.assertEqual(jpbizday.first_bizday(2020, 3), datetime.date(2020, 3, 2))
        self.assertEqual(jpbizday.first_bizday(2020, 4), datetime.date(2020, 4, 1))
        self.assertEqual(jpbizday.first_bizday(2020, 5), datetime.date(2020, 5, 1))
        self.assertEqual(jpbizday.first_bizday(2020, 6), datetime.date(2020, 6, 1))
        self.assertEqual(jpbizday.first_bizday(2020, 7), datetime.date(2020, 7, 1))
        self.assertEqual(jpbizday.first_bizday(2020, 8), datetime.date(2020, 8, 3))
        self.assertEqual(jpbizday.first_bizday(2020, 9), datetime.date(2020, 9, 1))
        self.assertEqual(jpbizday.first_bizday(2020, 10), datetime.date(2020, 10, 1))
        self.assertEqual(jpbizday.first_bizday(2020, 11), datetime.date(2020, 11, 2))
        self.assertEqual(jpbizday.first_bizday(2020, 12), datetime.date(2020, 12, 1))


    def test_first_bizday_day(self):
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 1, 1)), datetime.date(2020, 1, 6))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 2, 1)), datetime.date(2020, 2, 3))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 3, 1)), datetime.date(2020, 3, 2))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 4, 1)), datetime.date(2020, 4, 1))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 5, 1)), datetime.date(2020, 5, 1))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 6, 1)), datetime.date(2020, 6, 1))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 7, 1)), datetime.date(2020, 7, 1))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 8, 1)), datetime.date(2020, 8, 3))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 9, 1)), datetime.date(2020, 9, 1))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 10, 1)), datetime.date(2020, 10, 1))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 11, 1)), datetime.date(2020, 11, 2))
        self.assertEqual(jpbizday.first_bizday(datetime.date(2020, 12, 1)), datetime.date(2020, 12, 1))


    def test_last_bizday_month(self):
        self.assertEqual(jpbizday.last_bizday(2020, 1), datetime.date(2020, 1, 31))
        self.assertEqual(jpbizday.last_bizday(2020, 2), datetime.date(2020, 2, 28))
        self.assertEqual(jpbizday.last_bizday(2020, 3), datetime.date(2020, 3, 31))
        self.assertEqual(jpbizday.last_bizday(2020, 4), datetime.date(2020, 4, 30))
        self.assertEqual(jpbizday.last_bizday(2020, 5), datetime.date(2020, 5, 29))
        self.assertEqual(jpbizday.last_bizday(2020, 6), datetime.date(2020, 6, 30))
        self.assertEqual(jpbizday.last_bizday(2020, 7), datetime.date(2020, 7, 31))
        self.assertEqual(jpbizday.last_bizday(2020, 8), datetime.date(2020, 8, 31))
        self.assertEqual(jpbizday.last_bizday(2020, 9), datetime.date(2020, 9, 30))
        self.assertEqual(jpbizday.last_bizday(2020, 10), datetime.date(2020, 10, 30))
        self.assertEqual(jpbizday.last_bizday(2020, 11), datetime.date(2020, 11, 30))
        self.assertEqual(jpbizday.last_bizday(2020, 12), datetime.date(2020, 12, 31))


    def test_last_bizday_month(self):
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 1, 1)), datetime.date(2020, 1, 31))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 2, 1)), datetime.date(2020, 2, 28))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 3, 1)), datetime.date(2020, 3, 31))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 4, 1)), datetime.date(2020, 4, 30))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 5, 1)), datetime.date(2020, 5, 29))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 6, 1)), datetime.date(2020, 6, 30))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 7, 1)), datetime.date(2020, 7, 31))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 8, 1)), datetime.date(2020, 8, 31))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 9, 1)), datetime.date(2020, 9, 30))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 10, 1)), datetime.date(2020, 10, 30))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 11, 1)), datetime.date(2020, 11, 30))
        self.assertEqual(jpbizday.last_bizday(datetime.date(2020, 12, 1)), datetime.date(2020, 12, 31))


    def test_is_first_bizday(self):
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 1)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 3)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 4)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 5)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 6)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 1, 7)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 2, 1)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 2, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 2, 3)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 2, 4)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 3, 1)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 3, 2)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 3, 3)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 4, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 4, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 5, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 5, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 6, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 6, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 7, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 7, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 8, 1)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 8, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 8, 3)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 8, 4)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 9, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 9, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 10, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 10, 2)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 11, 1)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 11, 2)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 11, 3)), False)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 12, 1)), True)
        self.assertEqual(jpbizday.is_first_bizday(datetime.date(2020, 12, 2)), False)


    def test_is_last_bizday(self):
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 1, 31)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 1, 30)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 2, 29)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 2, 28)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 2, 27)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 3, 31)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 3, 30)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 4, 30)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 4, 29)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 5, 31)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 5, 30)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 5, 29)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 5, 28)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 6, 30)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 6, 29)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 7, 31)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 7, 30)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 8, 31)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 8, 30)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 9, 30)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 9, 29)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 10, 31)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 10, 30)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 10, 29)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 11, 30)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 11, 29)), False)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 12, 31)), True)
        self.assertEqual(jpbizday.is_last_bizday(datetime.date(2020, 12, 30)), False)


if __name__ == "__main__":
    unittest.main()
