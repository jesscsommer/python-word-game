# Feel free to use faker to generate seed data for your project, or create your own seed data.
# In addition you may also fire up a get request to an API or scrape a webpage to get seed data for your project.
from classes.player import Player
from classes.puzzle import Puzzle
from classes.result import Result
from random import sample
from faker import Faker
fake = Faker()
USERNAMES = [
    'Wnnr',
    'Losr',
    'Drew',
    'Jess',
    'Meredith',
    'Jeff',
    'Matilda',
    'Compy',
    'Legend27',
    '1234',
    #TODO ADD SPECIAL CHARACTER FUNCTIONALITY
    # '@drew'
]   

Player.drop_table()
Puzzle.drop_table()
Result.drop_table()

Player.create_table()
Puzzle.create_table()
Result.create_table()

for _ in range(10):
    try:
        Player.create_player(sample(USERNAMES, 1)[0])
        Puzzle.create(fake.name())
        print('created usernames and puzzles')
    except Exception as e:
        print('Failed to create usernames and puzzles because of: ', e)
        
for _ in range(10):
    try:
        players = Player.get_all()
        puzzles = Puzzle.get_all()
        Result.create(fake.number(), fake.number(), fake.number())
        print('Created results')
    except Exception as e:
        print('Failed to create results because of: ', e)
        
print('Seed data complete')