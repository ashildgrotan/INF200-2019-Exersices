# -*- coding: utf-8 -*-

__author__ = 'Åshild Grøtan'
__email__ = 'ashild.grotan@nmbu.no'


class LCGRand:
    """ Implements a linear congruential generator (LCG) to generate
    random numbers.
    """
    def __init__(self, seed):
        self.random = seed

    def rand(self):
        """Returns the next random number
        """
        a = 7**5
        m = 2**31-1
        self.random = a * self.random % m
        return self.random


class ListRand:
    """Random number generator based on a list of numbers.
    """
    def __init__(self, list_of_numbers):
        self.random_list = list_of_numbers
        self.random = 0

    def rand(self):
        """Returns the next random number
        """
        if len(self.random_list) == 0:
            raise RuntimeError
        self.random = self.random_list.pop(0)
        return self.random


if __name__ == "__main__":
    lcg = LCGRand(50)
    print(lcg.rand())
    print(lcg.rand())
    print(lcg.rand())

    lr = ListRand([1, 2, 3, 4])
    print(lr.rand())
    print(lr.rand())
    print(lr.rand())
    print(lr.rand())
