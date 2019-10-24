# -*- coding: utf-8 -*-

__author__ = 'Åshild Grøtan'
__email__ = 'ashild.grotan@nmbu.no'


class LCGRand:
    """ Implements a linear congruential generator (LCG) to generate
    random numbers.
    """
    def __init__(self, seed):
        a = 7**5
        m = 2**31-1
        self.random = a * seed % m

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
        pass

    def rand(self):
        """Returns the next random number
        """
        pass


if __name__ == "__main__":
    r = LCGRand(1)
    print(r.random)
    LCGRand.rand(r)
    print(r.random)
    LCGRand.rand(r)
    print(r.random)
