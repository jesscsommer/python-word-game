class Player:
    all = []
    
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
        
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 1 <= len(username) <= 8 and not hasattr(self, '_username'):
            self._username = username
        else:
            raise AttributeError('username must be a string between 1 and 8 characters and cannot be recreated')

    def get_scores(self, puzzle):
        # validate that puzzle is a puzzle
        # return player's scores for this puzzle
        return [result.score for result in Result.get_all() if result.player_id == self.id]

    @classmethod
    def create_table(cls):
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS players(
            id INTEGER PRIMARY KEY,
            username TEXT,
            personal best INTEGER
            )""")
    @classmethod
    def insert_data(cls, username):
        new_user = Player(username)
        if new_user:
            pass
        else:
            raise Exception('could not create a new user, check that everything is correct and try again')
        


from classes.puzzle import Puzzle
from .__init__ import CONN, CURSOR 
# from classes.result import Result