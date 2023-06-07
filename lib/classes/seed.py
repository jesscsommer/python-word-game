from .player import Player
from .puzzle import Puzzle
from .result import Result 

# assumes some of these methods will exist

Player.drop_table()
Puzzle.drop_table()
Result.drop_table()

Player.create_table()
Puzzle.create_table()
Result.create_table()

# puzzle1 = Puzzle.create("Puzzle1", "harpy")
# puzzle2 = Puzzle.create("Puzzle2", "lemon")
# puzzle3 = Puzzle.create("Puzzle3", "smell")
# puzzle4 = Puzzle.create("Puzzle4", "overt")
# puzzle5 = Puzzle.create("Puzzle5", "route")

# player1 = Player.create("jess99")
# player2 = Player.create("wumbo")
# player3 = Player.create("meridith")

# result1 = Result.create(player1, puzzle3, 150, 4)
# result2 = Result.create(player2, puzzle3, 300, 1)
# resulte = Result.create(player3, puzzle3, 200, 3)