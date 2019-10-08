import players
from mancala import status


def game(player1, player2, status):
    while not status['finish']:
        turn = status['turn']
        if turn == 0:
            # first player
            status = player1(status, 0)
        elif turn == 1:
            # robot
            status = player2(status, 1)
    board = status['board']
    score = [board[6], board[13]]
    print("Player 1 score: " + str(score[0]))
    print("Player 2 score: " + str(score[1]))
    return score.index(max(score))

winner = game(players.player, players.randomPlayer, status)
print("WINNER PLAYER " + str(winner + 1))
