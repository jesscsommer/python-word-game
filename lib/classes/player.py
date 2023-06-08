class Player:

    def __init__(self, username, id=None):
        self.username = username
        self.id = id
    def __repr__(self):
        return (f"<Username: {self.username}>")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if (isinstance(username, str) 
            and 1 <= len(username) <= 8 
            and not hasattr(self, '_username')
            ):
            self._username = username
        else:
            # raise Exception('')
            print('usernames must be between 1 and 8 characters and cannot contain special characters(@!$&%...)')
            # register_player()
    
    def results(self):
        return [result for result in Result.get_all() if result.player_id == self.id]

    def puzzles(self):
        return [Puzzle.find_by_id(result.puzzle_id) for result in self.results()]
    
    def scores(self, puzzle):
        # validate that puzzle is a puzzle
        # return player's scores for this puzzle
        # still needs to make use of the puzzle arg
        return [result.score for result in self.results()]
    
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

    def update(self):
        CURSOR.execute(
            """
            UPDATE players
            SET username = ?
            WHERE id = ?
        """,
            (self.username,),
        )
        CONN.commit()
        return type(self).find_by_id(self.id)

    def save(self):
        CURSOR.execute(
            """
            INSERT INTO players (username)
            VALUES (?);
        """,
            (self.username,),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

    def delete(self):
        CURSOR.execute(
            """
            DELETE FROM players
            WHERE id = ?
        """,
            (self.id,),
        )
        CONN.commit()
        return self

    @classmethod
    def create(cls, username):
        new_player = cls(username)
        new_player.save()
        return new_player

    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """
                SELECT * FROM players;
            """
        )
        rows = CURSOR.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
            SELECT * FROM players
            WHERE id is ?;
        """,
            (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS players;
        """
        )
        CONN.commit()

    @classmethod
    def find_by_username(cls, username):
        CURSOR.execute(
            """
            SELECT * FROM players
            WHERE username is ?;
        """,
            (username,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

from .__init__ import CONN, CURSOR 
from classes.puzzle import Puzzle
from classes.result import Result
