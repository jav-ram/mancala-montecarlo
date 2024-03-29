from utils import show
import random
import math

# game status
status = {
    'board': [
        # P1
        4, 4, 4,  4, 4, 4,  # [0 - 5]
        0,  # Mancala P1 [6]
        # P2
        4, 4, 4,  4, 4, 4,  # [7 - 12]
        0,  # Mancala P2 [13]
    ],
    'turn': 0,
    'finish': False,
}


def get_score(status):
    for player in range(2):
        mancala = 6 + (7 * player)
        score = status['board'][mancala]
        score += sum(status['board'][mancala - 6: mancala])
        status['board'][mancala] = score
    return status


def get_possibles_moves(player, status):
    possibles_moves = []
    board = status['board']

    start = 0 + (7 * player)
    end = 5 + (7 * player)

    for i in range(start, end + 1):
        if board[i] != 0:
            possibles_moves.append(i)

    return possibles_moves


def make_move(player, move, status):
    board = status['board']
    chips = board[move]  # how many chips are there
    board[move] = 0  # take the chips

    for i in range(0, chips):
        move = (move + 1) % len(board)
        board[move] = board[move] + 1

    if move != (6 + (7 * player)):  # if didnt stops on mancala
        status['turn'] = (player + 1) % 2  # next player
        # check if can steal
        if board[move] == 1:  # it was empty
            dif = 6 - move
            mirror_move = 6 + dif
            if board[mirror_move] > 0:  # mirror tile have something
                temp = board[mirror_move]
                board[mirror_move] = 0
                temp = temp + board[move]
                board[move] = 0

                board[6 + (7 * player)] += temp

    status['board'] = board
    return status


def make_turn(player, move, status):
    # validate move
    board = status['board']
    possible_moves = get_possibles_moves(player, status)

    # make move
    status = make_move(player, move, status)
    # end ?
    if (not get_possibles_moves(player, status) or
            not get_possibles_moves((player + 1) % 2, status)):
        # I lost or the other one lost, get winning score
        status['finish'] = True
        get_score(status)
        return status
    return status

if __name__ == "__main__":
    while True:
        if status['turn']:
            moves = get_possibles_moves(status['turn'], status)
            status = make_turn(status['turn'], random.choice(moves), status)
        else:
            while True:
                move = input('Por favor ingrese su movimiento: \n')
                turn = make_turn(status['turn'], int(move), status)
                if turn:
                    status = turn
                    break
