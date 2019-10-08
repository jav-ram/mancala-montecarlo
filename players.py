import random
from mancala import *
from utils import show


def player(status, player):
    choose = -1
    p = get_possibles_moves(player, status)
    while choose not in p:
        show(status)
        choose = input('please insert move')
        choose = -1 if choose == '' else int(choose)
        status = make_turn(player, choose, status)
    return status


def monteCarlo(status, player):
    # DO MONTECARLO
    pass


def randomPlayer(status, player):
    show(status)
    input()
    possible = get_possibles_moves(player, status)
    choose = random.choice(possible)
    return make_turn(player, choose, status)
