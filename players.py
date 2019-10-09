import random
from mancala import *
from main import game
from utils import show
import copy


def player(status, player):
    choose = -1
    p = get_possibles_moves(player, status)
    while choose not in p:
        show(status)
        choose = input('please insert move')
        choose = -1 if choose == '' else int(choose)
        status = make_turn(player, choose, status)
    return status


def monteCarlo(status, player, iters=10000):
    # DO MONTECARLO
    results = [0]*14
    possible = get_possibles_moves(player, status)
    for i in range(iters):
        choice = random.choice(possible)
        ns = copy.deepcopy(status)
        make_turn(player, choice, ns)
        results[choice] += game(randomPlayer, randomPlayer, ns) == player
    move = results.index(max(results))
    return make_turn(player, move, status)


def randomPlayer(status, player):
    possible = get_possibles_moves(player, status)
    choose = random.choice(possible)
    return make_turn(player, choose, status)
