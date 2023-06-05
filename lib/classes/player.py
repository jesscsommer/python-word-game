class Player:
    all = []
    
    def __init__(self, username, personal_best):
        self.username = username
        self.personal_best = personal_best
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
        
    @property
    def personal_best(self):
        return self._personal_best
    @personal_best.setter
    def personal_best(self, personal_best):
        if isinstance(personal_best, int):
            self._personal_best = personal_best
        else:
            raise AttributeError('personal best must be an integer')
        
    
        
        
        
from classes.puzzle import Puzzle
from classes.result import Result