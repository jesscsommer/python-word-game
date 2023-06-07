from puzzle import Puzzle
from result import Result 
from player import Player
# assumes some of these methods will exist

Player.drop_table()
Puzzle.drop_table()
Result.drop_table()

Player.create_table()
Puzzle.create_table()
Result.create_table()

puzzle1 = Puzzle.create("harpy")
puzzle2 = Puzzle.create("lemon")
puzzle3 = Puzzle.create("smell")
puzzle4 = Puzzle.create("overt")
puzzle5 = Puzzle.create("route")

player1 = Player.create("jess99")
player2 = Player.create("wumbo")
player3 = Player.create("meridith")

result1 = Result.create(player1.id, puzzle3.id, 150, 4)
result2 = Result.create(player2.id, puzzle3.id, 300, 1)
resulte = Result.create(player3.id, puzzle3.id, 200, 3)