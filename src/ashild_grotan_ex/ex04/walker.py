# -*- coding: utf-8 -*-

__author__ = 'Åshild Grøtan'
__email__ = 'ashild.grotan@nmbu.no'

from random import randint


class Walker:
    """A student's walk back home from x0 to h. """
    def __init__(self, x0, h):
        self.position = x0
        self.home = h

    def move(self):
        """Move one step in a random direction (back or forth)"""
        dice = randint(1, 6)
        if dice > 3:
            self.position += 1
        if dice <= 3:
            self.position -= 1
        return self.position

    def is_at_home(self):
        """Check if the student has arrived home"""
        if self.position == self.home:
            return True
        return False

    def get_position(self):
        """Check where the student is"""
        pass

    def get_steps(self):
        """Check how many steps the student has taken. """
        pass


if __name__ == "__main__":
    student = Walker(0, 3)
    for _ in range(20):
        student.move()
        print(student.position)
        print(student.is_at_home())
