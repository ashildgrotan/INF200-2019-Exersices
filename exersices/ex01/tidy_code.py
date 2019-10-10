"""
INF200 EX01 task D.
"""

from random import randint

__author__ = "Åshild Grøtan"
__email__ = "ashigrot@nmbu.no"


def throw_dice():
    """
    Throws two dice to get the correct answer in the game
    :return: int
    """
    return randint(1, 6) + randint(1, 6)


def guess_number():
    """
    Allows player to guess a number
    :return: int
    """
    guess = 0
    while guess < 1:
        guess = int(input("Your guess: "))
    return guess


def check_guess(f, g):
    """
    Checks if the guessed number is equal to the correct answer.
    :param f: int. The correct answer from the dice.
    :param g: int. The player's guess.
    :return: bool.
    """
    return f == g


if __name__ == "__main__":

    right_guess = False
    points = 3
    dice = throw_dice()
    while not right_guess and points > 0:
        your_guess = guess_number()
        right_guess = check_guess(dice, your_guess)
        if not right_guess:
            print("Wrong, try again!")
            points -= 1

    if points > 0:
        print("You won {} points.".format(points))
    else:
        print("You lost. Correct answer: {}.".format(dice))
