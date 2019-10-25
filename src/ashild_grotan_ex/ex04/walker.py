# -*- coding: utf-8 -*-
"""
ex04 task B: class Walker simulates a student's random walk home.
"""

__author__ = 'Åshild Grøtan'
__email__ = 'ashild.grotan@nmbu.no'

from random import randint


class Walker:
    """A student's walk back home from x0 to h. """
    def __init__(self, x0, h):
        self.position = x0
        self.home = h
        self.steps = 0

    def move(self):
        """Move one step in a random direction (back or forth)"""
        dice = randint(1, 6)
        if dice > 3:
            self.position += 1
        if dice <= 3:
            self.position -= 1
        self.steps += 1
        return self.position

    def is_at_home(self):
        """Check if the student has arrived home"""
        if self.position == self.home:
            return True
        return False

    def get_position(self):
        """Check where the student is"""
        return self.position

    def get_steps(self):
        """Check how many steps the student has taken. """
        return self.steps


def one_walk_home(start, home):
    """Uses the class Walker to simulate a whole walk home"""
    student = Walker(start, home)
    while student.is_at_home() is False:
        student.move()
    return student.steps


if __name__ == "__main__":
    for distance in [1, 2, 5, 10, 20, 50, 100]:
        print(f'Distance: {distance} -> Path lengths: '
              f'{[one_walk_home(0, distance) for _ in range(5)]}')
