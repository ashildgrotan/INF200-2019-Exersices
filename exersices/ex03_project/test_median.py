# -*- coding: utf-8 -*-
"""
INF200, ex03_project: writing tests for the median function.
"""
__author__ = "Åshild Grøtan"
__email__ = "ashild.grotan@nmbu.no"


import pytest
from random import randint


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    return (
        sorted_data[n // 2]
        if n % 2 == 1
        else 0.5 * (sorted_data[n // 2 - 1] + sorted_data[n // 2])
    )


def test_median_of_single_element():
    test_value = [randint(0, 10)]
    assert median([test_value]) == test_value