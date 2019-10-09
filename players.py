import random
from mancala import *
from utils import show
import numpy as np
import copy


def player(status, player):
    choose = -1
    p = get_possibles_moves(player, status)
    while choose not in p:
        choose = input('please insert move')
        choose = -1 if choose == '' else int(choose)
        status = make_turn(player, choose, status)
    return status


def monteCarlo(status, player, iters=10000):
    # DO MONTECARLO
    results = [0]*14
    ocurrances = [1]*14
    possible = get_possibles_moves(player, status)
    for i in range(iters):
        choice = random.choice(possible)
        ns = copy.deepcopy(status)
        make_turn(player, choice, ns)
        ocurrances[choice] += 1
        results[choice] += randomGame(ns) == player
    win_percents = [i / j for i, j in zip(results, ocurrances)]
    print(win_percents)
    move = win_percents.index(max(win_percents))
    return make_turn(player, move, status)


def randomPlayer(status, player):
    possible = get_possibles_moves(player, status)
    choose = random.choice(possible)
    return make_turn(player, choose, status)


def randomGame(status):
    while not status['finish']:
        randomPlayer(status, status['turn'])
    board = status['board']
    score = [board[6], board[13]]
    return score.index(max(score))
