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

    @property
    def player(self):
        # assumes methods on Player
        row = Player.find_by_id(self.player_id)
        return Player.new_from_db(row) if row else None

    @player.setter 
    def player(self, player_id):
        if (isinstance(player_id, int)
            and player_id > 0 
            and Player.find_by_id(player_id)):
            self._player_id = player_id
        else: 
            raise ValueError("Player must exist and have a positive integer ID")
        
    @property
    def puzzle(self):
        # assumes methods on puzzle
        row = Puzzle.find_by_id(self.puzzle_id)
        return Puzzle.new_from_db(row) if row else None

    @puzzle.setter 
    def puzzle(self, puzzle_id):
        if (isinstance(puzzle_id, int)
            and puzzle_id > 0 
            and Puzzle.find_by_id(puzzle_id)):
            self._puzzle_id = puzzle_id
        else: 
            raise ValueError("Puzzle must exist and have a positive integer ID")
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) == int and 0<= score <= 300:
            self._score = score
        else:
            raise ValueError("Score must be an integer between 0 and 300")
    
    @property
    def num_guesses(self):
        return self._num_guesses
    
    @num_guesses.setter
    def num_guesses(self, num_guesses):
        if type(num_guesses) == int and 0 <= num_guesses <= 6:
            self._num_guesses = num_guesses
        else:
            raise ValueError("Guesses must be an integer between 0 and 6")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                player_id INTEGER,
                puzzle_id INTEGER,
                score INTEGER,
                num_guesses INTEGER,
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
