from constants import *
selection = 8
FEN = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w KQkq - 0 1"
print(FEN.split("/")[white_locations[selection][1]][white_locations[selection][0]])
FEN = "".join(FEN.split("/")[:white_locations[selection][1]]) + "/" + "".join(FEN.split("/")[white_locations[selection][1][0]])

print(FEN)
