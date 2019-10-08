import random
from mancala import *
from utils import show

if __name__ == "__main__":
    while not status['finish']:
        turn = status['turn']
        if turn == 0:
            # first player
            choose = -1
            p = get_possibles_moves(0, status)
            while choose not in p:
                show(status)
                choose = int(input('please insert move'))
                choose = -1 if choose == '' else choose
                status = make_turn(0, choose, status)
                print(status['turn'])
        elif turn == 1:
            # robot
            show(status)
            input()
            possible = get_possibles_moves(1, status)
            choose = random.choice(possible)
            status = make_turn(1, choose, status)
