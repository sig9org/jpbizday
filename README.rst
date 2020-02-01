.. image:: https://img.shields.io/pypi/v/jpbizday.svg
 :target: https://pypi.org/project/jpbizday/
.. image:: https://img.shields.io/pypi/l/jpbizday.svg
 :target: https://pypi.org/project/jpbizday/
.. image:: https://img.shields.io/pypi/pyversions/jpbizday.svg
 :target: https://pypi.org/project/jpbizday/
.. image:: https://img.shields.io/github/contributors/sig9org/jpbizday.svg
 :target: https://github.com/sig9org/jpbizday/graphs/contributors

JPBizDay
====================================================

日本の営業日を取得するライブラリです。 `jpholiday <https://pypi.org/project/jpholiday/>`_ に依存しています (作者の `Lalcs <https://github.com/Lalcs>`_ さんに感謝します)。

.. contents:: 目次

インストール
=========================

pip でインストールします。

.. code-block:: bash

    $ pip install jpbizday

サンプルコード
=========================

指定日が営業日かを判定する
-------------------------

.. code-block:: python

    > import jpbizday
    > import datetime
    > jpbizday.is_bizday(datetime.date(2020, 1, 1))
    False
    > jpbizday.is_bizday(datetime.date(2020, 1, 6))
    True

指定年の営業日を取得する
-------------------------

.. code-block:: python

    > jpbizday.year_bizdays(2020)
    [datetime.date(2020, 1, 6),
     datetime.date(2020, 1, 7),
     datetime.date(2020, 1, 8),
     datetime.date(2020, 1, 9),
     datetime.date(2020, 1, 10),
     datetime.date(2020, 1, 14),
     datetime.date(2020, 1, 15),
        .
        .
        .
     datetime.date(2020, 12, 23),
     datetime.date(2020, 12, 24),
     datetime.date(2020, 12, 25),
     datetime.date(2020, 12, 28),
     datetime.date(2020, 12, 29),
     datetime.date(2020, 12, 30),
     datetime.date(2020, 12, 31)]
    > len(jpbizday.year_bizdays(2020))
    244

指定月の営業日を取得する
-------------------------

.. code-block:: python

    > jpbizday.month_bizdays(2020, 1)
    [datetime.date(2020, 1, 6),
     datetime.date(2020, 1, 7),
     datetime.date(2020, 1, 8),
     datetime.date(2020, 1, 9),
     datetime.date(2020, 1, 10),
     datetime.date(2020, 1, 14),
     datetime.date(2020, 1, 15),
     datetime.date(2020, 1, 16),
     datetime.date(2020, 1, 17),
     datetime.date(2020, 1, 20),
     datetime.date(2020, 1, 21),
     datetime.date(2020, 1, 22),
     datetime.date(2020, 1, 23),
     datetime.date(2020, 1, 24),
     datetime.date(2020, 1, 27),
     datetime.date(2020, 1, 28),
     datetime.date(2020, 1, 29),
     datetime.date(2020, 1, 30),
     datetime.date(2020, 1, 31)]
    > len(jpbizday.month_bizdays(2020, 1))
    19

指定月の営業日を取得する
-------------------------

.. code-block:: python

    > jpbizday.bizdays(datetime.date(2020, 1, 1), datetime.date(2020, 1, 18))
    [datetime.date(2020, 1, 6),
     datetime.date(2020, 1, 7),
     datetime.date(2020, 1, 8),
     datetime.date(2020, 1, 9),
     datetime.date(2020, 1, 10),
     datetime.date(2020, 1, 14),
     datetime.date(2020, 1, 15),
     datetime.date(2020, 1, 16),
     datetime.date(2020, 1, 17)]
    > len(jpbizday.bizdays(datetime.date(2020, 1, 1), datetime.date(2020, 1, 18)))
    9

指定月の最初の営業日を取得する
-------------------------

.. code-block:: python

    > jpbizday.first_bizday(2020, 1)
    datetime.date(2020, 1, 6)
    > jpbizday.first_bizday(datetime.date(2020, 1, 1))
    datetime.date(2020, 1, 6)
    > datetime.datetime.today()
    datetime.datetime(2020, 2, 2, 4, 54, 15, 305254)
    > jpbizday.first_bizday(datetime.datetime.today())
    datetime.date(2020, 2, 3)

指定月の最後の営業日を取得する
-------------------------

.. code-block:: python

    > jpbizday.last_bizday(2020, 5)
    datetime.date(2020, 5, 29)
    > jpbizday.last_bizday(datetime.date(2020, 5, 15))
    datetime.date(2020, 5, 29)
    > datetime.datetime.today()
    datetime.datetime(2020, 2, 2, 4, 55, 33, 664474)
    > jpbizday.last_bizday(datetime.datetime.today())
    datetime.date(2020, 2, 28)

指定月の最初の営業日なのかを判定する
-------------------------

.. code-block:: python

    > jpbizday.is_first_bizday(datetime.date(2020, 1, 1))
    False
    > jpbizday.is_first_bizday(datetime.date(2020, 1, 6))
    True
    > datetime.datetime.today()
    datetime.datetime(2020, 2, 2, 4, 58, 5, 843849)
    > jpbizday.is_first_bizday(datetime.datetime.today())
    False

指定月の最後の営業日なのかを判定する
-------------------------

.. code-block:: python

    > jpbizday.is_last_bizday(datetime.date(2020, 1, 31))
    True
    > jpbizday.is_last_bizday(datetime.date(2020, 1, 30))
    False
    > datetime.datetime.today()
    datetime.datetime(2020, 2, 2, 4, 59, 6, 89896)
    > jpbizday.is_last_bizday(datetime.datetime.today())
    False
