class Result:

    def __init__(self, player_id, puzzle_id, score = 0, num_guesses = 0, id = None):
        self.player_id = player_id
        self.puzzle_id = puzzle_id
        self.score = score
        self.num_guesses = num_guesses
        self.id = id

    def __repr__(self):
        # the below assumes that the find by id methods will exist
        return (
            f"<Result {self.id}: "
            + f"Player: {Player.find_by_id(self.player_id).username}"
            + f"Puzzle: {Puzzle.find_by_id(self.puzzle_id).title}"
            + f"Score: {self.score}"
            + f"Guesses: {self.num_guesses}>"
        )

    # update player id & puzzle id properties based on example 
    
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

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS result (
                id INTEGER PRIMARY KEY,
                player_id INTEGER,
                puzzle_id INTEGER,
                score INTEGER,
                num_guesses INTEGER,
                score_rank INTEGER,
                FOREIGN KEY (player_id) REFERENCES players(id),
                FOREIGN KEY (puzzle_id) REFERENCES puzzles(id)
                );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS results;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def new_from_db(cls, row): 
        return cls(row[1], row[2], row[3], row[4], row[0])

    @classmethod
    def get_all(cls):
        # add optional sort by??? or optional limit???
        sql = """
            SELECT * FROM results;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.new_from_db(row) for row in rows]
    
    def save(self):
        sql = """
            INSERT INTO results (player_id, puzzle_id, score, num_guesses)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.player_id, self.puzzle_id, 
                        self.score, self.num_guesses))
        CONN.commit()
        self.id = CURSOR.lastrowid 
    
    @classmethod
    def create(cls, player_id, puzzle_id, score, num_guesses):
        new_result = cls(player_id, puzzle_id, score, num_guesses)
        new_result.save()
        return new_result 
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM results
            WHERE id is ?;
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.new_from_db(row) if row else None 

from .__init__ import CONN, CURSOR
from .puzzle import Puzzle
from .player import Player
