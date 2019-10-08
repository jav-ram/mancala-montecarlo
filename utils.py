global str

# game status
status = {
    'board': [
        # P1
        0, 1, 2,  3, 4, 5,  # [0 - 5]
        6,  # Mancala P1 [6]
        # P2
        7, 8, 9,  10, 11, 12,  # [7 - 12]
        13,  # Mancala P2 [13]
    ],
    'turn': 0,
    'finish': False,
}


def show(state):
    board = state['board']
    boards = [board[0:7], board[7:14]]
    print('turn of player: %d' % (state['turn'] + 1))
    txt = '  '
    for i in range(5, -1, -1):
        txt = txt + str(boards[1][i]) + '  '
    print(txt)

    txt = str(boards[1][6]) + '                  ' + str(boards[0][6])
    print(txt)

    txt = '  '
    for i in range(0, 6):
        txt = txt + str(boards[0][i]) + '  '
    print(txt)
