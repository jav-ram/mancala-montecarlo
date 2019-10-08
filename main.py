import players
from mancala import status

if __name__ == "__main__":
    while not status['finish']:
        turn = status['turn']
        if turn == 0:
            # first player
            status = players.player(status, 0)
        elif turn == 1:
            # robot
            status = players.randomPlayer(status, 1)
    board = status['board']
    print("Player 1 score: " + str(board[6]))
    print("Player 2 score: " + str(board[13]))