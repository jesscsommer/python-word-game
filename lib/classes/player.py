
class Player:
    
    def __init__(self, username):
        self.username = username
        
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 1 <= len(username) <= 8 and not hasattr(self, '_username'):
            self._username = username
        else:
            raise AttributeError('username must be a string between 1 and 8 characters and cannot be recreated')
        
    @classmethod
    def create_table(cls): 
        sql = """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                username TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    
from .__init__ import CONN, CURSOR 
from classes.puzzle import Puzzle
from classes.result import Result