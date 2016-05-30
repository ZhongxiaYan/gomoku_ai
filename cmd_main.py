from config import *
from game import *

players = [HUMAN_CMD_LINE, HUMAN_CMD_LINE] # two players, both human
display = DISPLAY_COMMAND_LINE
game = Game(players, display)

# main loop
while True:
    game.show_board()
    game.transition(game.get_input())
    if game.has_ended():
        break
