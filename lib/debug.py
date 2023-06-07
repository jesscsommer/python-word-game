from classes.puzzle import Puzzle
from classes.player import Player
from classes.result import Result
from random import sample

Result.drop_table()
Player.drop_table()
Puzzle.drop_table()

Player.create_table()
Puzzle.create_table()
Result.create_table()

player_1 = Player.create('Winnr')
player_2 = Player.create('Loser')

puzzle_matte = Puzzle.create_puzzle("title_matte", "Matte")

for num in range(1, 18):
    Result.create(player_1.id, puzzle_matte.id, num, sample([1, 2, 3, 4, 5], 1)[0])

print('complete')
import ipdb; ipdb.set_trace()