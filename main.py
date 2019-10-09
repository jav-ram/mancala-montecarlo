import players
from mancala import status
from utils import show


def game(player1, player2, status):
    while not status['finish']:
        turn = status['turn']
        show(status)
        if turn == 0:
            # first player
            player1(status, 0)
        elif turn == 1:
            # robot
            player2(status, 1)
    board = status['board']
    score = [board[6], board[13]]
    return score.index(max(score))

winner = game(players.monteCarlo, players.randomPlayer, status)
print("WINNER PLAYER " + str(winner + 1))
