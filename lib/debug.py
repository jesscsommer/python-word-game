from classes.puzzle import Puzzle
from classes.player import Player

Player.drop_table()
# Puzzle.drop_table()
Player.create_table()
# Puzzle.create_table()

player_1 = Player.create_player('Winnr')
player_2 = Player.create_player('Loser')

print('complete')
import ipdb; ipdb.set_trace()