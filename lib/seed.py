from classes.puzzle import Puzzle
from classes.result import Result 
from classes.player import Player

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
result3 = Result.create(player3.id, puzzle3.id, 200, 3)
result4 = Result.create(player1.id, puzzle2.id, 100, 5)
result5 = Result.create(player3.id, puzzle2.id, 250, 2)
result6 = Result.create(player1.id, puzzle1.id, 0, 6)