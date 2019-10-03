# -*- coding: utf-8 -*-
"""
INF200, ex03_project: writing tests for the bubble sort function.
"""
__author__ = "Åshild Grøtan"
__email__ = "ashild.grotan@nmbu.no"


from random import randint


def bubble_sort(data):
    """
    Takes a list or tuple of sortable elements and sorts it by the
    "Bubble sort" method.
    :param data: list or tuple
    :return: sorted list
    """
    sorted_data = list(data)

    for i in range(len(sorted_data) - 1):
        for j in range(len(sorted_data) - 1 - i):
            if sorted_data[j] > sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] =\
                    sorted_data[j + 1], sorted_data[j]
    return sorted_data


if __name__ == "__main__":

    for data in ((), (1,), (1, 3, 8, 12), (12, 8, 3, 1), (8, 3, 12, 1)):
        print("{!s:>15} --> {!s:>15}".format(data, bubble_sort(data)))


def test_empty():
    """Test that the sorting function works for empty list"""
    test_data = []
    assert len(bubble_sort(test_data)) == 0


def test_single():
    """Test that the sorting function works for single-element list"""
    test_data = [randint(0, 10)]
    assert len(bubble_sort(test_data)) == 1


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    test_data = [3, 2, 1]
    sorted_data = bubble_sort(test_data)
    assert sorted_data != test_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    test_data = [3, 2, 1]
    sorted_data = bubble_sort(test_data)
    assert test_data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    test_data = [1, 2, 3]
    sorted_data = bubble_sort(test_data)
    assert sorted_data == test_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    reverse_sorted_data = [3, 2, 1]
    sorted_data = bubble_sort(reverse_sorted_data)
    assert sorted_data == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    test_data = [1, 1, 1]
    sorted_data = bubble_sort(test_data)
    assert sorted_data == [1, 1, 1]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    assert bubble_sort([8, 5, 3, 4, 2, 6, 1, 7]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert bubble_sort('sorted letters') == [' ', 'd', 'e', 'e', 'e', 'l', 'o',
                                             'r', 'r', 's', 's', 't', 't', 't']
    assert bubble_sort(['s', 'o', 'r', 't', 'e', 'd']) == ['d', 'e', 'o', 'r',
                                                           's', 't']
    pass
