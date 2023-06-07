class Puzzle:
    
    def __init__(self, title, solution, id=None):
        self.title = title
        self.solution = solution
        self.id = id 
    
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, title):
        if (isinstance(title, str)
            and 1 <= len(title) <= 25
            and not hasattr(self, "_title")):
            self._title = title 
        else: 
            raise AttributeError("Puzzle title must be a string of 1-25 chars")
    
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
        return [result.score for result in Result.get_all() if result.puzzle_id == self.id]
        # rework to have tuples for result.player and result.score]
        # return [(result.player, result.score) for result in Result.get_all() if result.puzzle_id == self.id]
    
    def high_scores(self):
        scores = self.get_scores()
        if scores:
            sorted_scores = sorted(scores, reverse = True)
        top_ten_scores = sorted_scores[:10] if len(sorted_scores) > 10 else sorted_scores[:len(sorted_scores)]
        print("HIGH SCORES: ")
        for each_score in top_ten_scores:
            print(f"""
                {each_score}: {each_score}
            """)
        
    @classmethod
    def create_table(cls): 
        sql = """
            CREATE TABLE IF NOT EXISTS puzzles (
                id INTEGER PRIMARY KEY,
                title TEXT, 
                solution TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def update(self):
        CURSOR.execute(
            """
            UPDATE puzzles
            SET title = ?
            SET solution = ?
            WHERE id = ?
        """,
            (self.title, self.solution),
        )
        CONN.commit()
        return type(self).find_by_id(self.id)
        
    def save(self):
        CURSOR.execute(
            """
            INSERT INTO puzzles (title)
            VALUES (?);
        """,
            (self.title,),
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
        return [cls.new_from_db(row) for row in rows]
    
    @classmethod
    def create_puzzle(cls, title, solution):
        new_puzzle = cls(title, solution)
        new_puzzle.save()
        return new_puzzle
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM results
            WHERE id is ?;
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None
    
    @classmethod
    def find_by_puzzle_name(cls, title):
        CURSOR.execute(
            """
            SELECT * FROM puzzles
            WHERE title is ?;
            """,
        (title,)
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

from .__init__ import CONN, CURSOR
from .player import Player
from .result import Result