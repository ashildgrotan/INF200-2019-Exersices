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
    if len(data) == 0:
        raise ValueError
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


def test_median_of_odd_number_of_elements():
    assert median([1, 2, 3]) == 2


def test_median_of_even_number_of_elements():
    assert median([1, 2, 4, 5]) == 3


def test_median_of_ordered_and_unordered_elements():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([5, 2, 4, 1, 3]) == 3
    assert median([5, 4, 3, 2, 1]) == 3


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_original_data_unchanged():
    test_data = [1, 2, 6, 5, 3]
    found_median = median(test_data)
    assert test_data == [1, 2, 6, 5, 3]
