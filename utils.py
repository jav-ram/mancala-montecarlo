def show(state):
    print('Turno del jugador: ', state['turn'] + 1)
    board = '  '
    for index, item in enumerate(state['board']):
        if index == 6:
            board = board + '\n'
            board = board + str(item) + ' '*15 + str(state['board'][13])
            board = board + '\n  '
            continue
        elif index == 13:
            continue
        board = board + ' ' + str(item)
    print(board)
