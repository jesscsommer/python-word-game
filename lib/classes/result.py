class Appointment:

    def __init__(self, player_id, puzzle_id, score, num_guesses, score_rank):
        self.player_id = player_id
        self.puzzle_id = puzzle_id
        self.score = score
        self.num_guesses = num_guesses
        self.score_rank = score_rank
    
    @property
    def player_id(self):
        return self._player_id
    
    @player_id.setter
    def player_id (self, player_id):
        if type(player_id) == int:
            self._player_id = player_id
        else:
            raise Exception("invalid player_id type")
        
    @property
    def puzzle_id(self):
        return self._puzzle_id
    
    @puzzle_id.setter
    def puzzle_id (self, puzzle_id):
        if type(puzzle_id) == int:
            self._puzzle_id = puzzle_id
        else:
            raise Exception("invalid puzzle_id type")
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and 0<= score <= 300:
            self._score = score
        else:
            raise Exception("Score is not an integer between 0 and 300")
    
    @property
    def num_guesses(self):
        return self._num_guesses
    
    @num_guesses.setter
    def num_guesses(self, num_guesses):
        if type(num_guesses) == int and 0<= num_guesses <= 6:
            self._num_guesses = num_guesses
        else:
            raise Exception("invalid num_guesses")
        
    @property
    def score_rank(self):
        return self._score_rank

    @score_rank.setter
    def score_rank(self, score_rank):
        if type(score_rank) == int and 1 <= score_rank <= 100:
            return self._score_rank
        else:
            raise Exception("invalid high score")

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS result (
                id INTEGER PRIMARY KEY,
                player_id INTEGER,
                puzzle_id INTEGER,
                score INTEGER,
                num_guesses INTEGER,
                score_rank INTEGER,
                )
        """
        )
        print("attempted to create table")

from .__init__ import CURSOR
