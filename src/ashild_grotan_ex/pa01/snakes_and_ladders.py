# -*- coding: utf-8 -*-
"""
INF200, pa01: Snakes and ladders
"""
__author__ = "Åshild Grøtan, Erik Heggelund"
__email__ = "ashild.grotan@nmbu.no, erik.heggelund@nmbu.no"


from random import randint


def throw_dice():
    """
    Throws dice
    :return: Number from 1 to 6
    """
    return randint(1, 6)


def make_players(num_players):
    """
    Makes a list with the positions for each player.
    :param num_players: number of players in the game
    :return: list with the positions for each player
    """
    return [0 for _ in range(num_players)]


def check_position(position):
    """
    Takes current position and moves position if there are snakes or ladders.
    :param position: Current position
    :return: old position if no snakes, ladders, new pos if snake or ladder
    """
    ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    if position in ladders:
        position = ladders[position]
    if position in snakes:
        position = snakes[position]
    return position


def play_single_round(positions):
    """
    Arguments:
    players: list with one element for each player, representing the current
    position.

    Plays one round for all players.
    :return: List with new positions for all players.
    """
    for player in range(len(positions)):
        dice = throw_dice()
        positions[player] += dice
        positions[player] = check_position(positions[player])
    return positions


def check_finished(positions):
    """
    Checks if any of the players are on position 90 or more.
    :param positions: Current positions
    :return: True or False
    """
    win = False
    for position in positions:
        if position > 89:
            win = True
            break
    return win


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    positions = make_players(num_players)
    turns = 0
    win = False
    while not win:
        positions = play_single_round(positions)
        turns += 1
        win = check_finished(positions)
    return turns


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """


if __name__ == "__main__":
    print(single_game(3))
