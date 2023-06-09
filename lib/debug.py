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

p1 = Puzzle.create("matte")
p2 = Puzzle.create("snake")
p3 = Puzzle.create("misty")
p4 = Puzzle("snake", 2)

# #  def __init__(self, player_id, puzzle_id, score = 0, num_guesses = 0, id = None):

r1 = Result.create(player_1.id, p1.id, 0, 6)
r2 = Result.create(player_2.id, p2.id, 300, 1)
r3 = Result.create(player_1.id, p2.id, 150, 4)

selected_puzzle = Puzzle.find_by_id(2)
testing = selected_puzzle in player_1.puzzles()

print("player 1 puzzles")
for p in player_1.puzzles(): print(p.solution)

# for x in Puzzle.get_all():
#     print(x.solution)

# for x in player_1.puzzles():
#     print(x.solution)

# # test = list(set(Puzzle.get_all()) - set(player_1.puzzles()))
# for x in test: print(x.solution)

# test2 = p3.id not in [puzzle.id for puzzle in player_1.puzzles()]
# test3 = p2.id not in [puzzle.id for puzzle in player_1.puzzles()]
# test4 = p1.id not in [puzzle.id for puzzle in player_1.puzzles()]

for num in range(1, 18):
    Result.create(player_1.id, p1.id, num, sample([1, 2, 3, 4, 5], 1)[0])
    Result.create(player_2.id, p1.id, num, sample([1, 2, 3, 4, 5], 1)[0])
    # Result.create(player_3.id, p1.id, num, sample([1, 2, 3, 4, 5], 1)[0])
    # Result.create(player_4.id, p1.id, num, sample([1, 2, 3, 4, 5], 1)[0])

print('complete')
import ipdb; ipdb.set_trace()