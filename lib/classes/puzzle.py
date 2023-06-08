class Puzzle:
    
    def __init__(self, solution, id=None):
        self.solution = solution
        self.id = id 
    
    @property
    def solution(self):
        return self._solution
    
    @solution.setter 
    def solution(self, solution):
        # should validate with RegEx too
        if (isinstance(solution, str)
            and len(solution) == 5
            and not hasattr(self, "_solution")):
            self._solution = solution
        else: 
            raise AttributeError("Puzzle solution must be a 5-letter string")
        
    def get_scores(self):
        return [(Player.find_by_id(result.player_id).username, result.score) for result in Result.get_all() if result.puzzle_id == self.id]
    
    def high_scores(self):
        scores = self.get_scores()
        if scores:
            sorted_scores = sorted(scores, key = lambda tup:tup[1], reverse = True)
        top_ten_scores = sorted_scores[:10] if len(sorted_scores) > 10 else sorted_scores[:len(sorted_scores)]
        print("HIGH SCORES: ")
        # can try to use enumerate instead of index
        index = 0
        for each_score in top_ten_scores:
            index+=1
            print(f"""
            {index}. {each_score[0]}: {each_score[-1]}
            """)
    def players(self):
        all_players = self.get_scores()
        players_list = list({each_player[0] for each_player in all_players})
        print("PLAYERS OF THIS PUZZLE: ")
        index = 0
        for player in players_list:
            index += 1
            print(f"""
            {index}. {player}
            """)     

    @classmethod
    def create_table(cls): 
        sql = """
            CREATE TABLE IF NOT EXISTS puzzles (
                id INTEGER PRIMARY KEY,
                solution TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def update(self):
        CURSOR.execute(
            """
            UPDATE puzzles
            SET solution = ?
            WHERE id = ?
        """,
            (self.solution),
        )
        CONN.commit()
        return type(self).find_by_id(self.id)
        
    def save(self):
        CURSOR.execute(
            """
            INSERT INTO puzzles (solution)
            VALUES (?);
        """,
            (self.solution,),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        CURSOR.execute(
            """
            DELETE FROM puzzles
            WHERE id = ?
        """,
            (self.id,),
        )
        CONN.commit()
        return self
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS puzzles;
        """
        )
        CONN.commit()
    
    @classmethod
    def get_all_puzzles(cls):
        sql = """
            SELECT * FROM puzzles;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[0]) for row in rows]
    
    @classmethod
    def create_puzzle(cls, solution):
        new_puzzle = cls(solution)
        new_puzzle.save()
        return new_puzzle
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM puzzles
            WHERE id is ?;
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls(row[1]) if row else None

from .__init__ import CONN, CURSOR
from .player import Player
from .result import Result