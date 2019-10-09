from players import player, monteCarlo, game
from mancala import status
from utils import show


winner = game(player, monteCarlo, status, True)
print("WINNER PLAYER " + str(winner + 1))
