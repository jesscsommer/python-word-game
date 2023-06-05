class Puzzle:
    
    def __init__(self, title, solution):
        self.title = title
        self.solution = solution 
    
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
        if (isinstance(solution, str)
            and len(solution) == 5
            and not hasattr(self, "_solution")):
            self._solution = solution
        else: 
            raise AttributeError("Puzzle solution must be a 5-letter string")
        
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
        
    
from .__init__ import CONN, CURSOR 