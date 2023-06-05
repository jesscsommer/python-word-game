import sqlite3

CONN = sqlite3.connect("word_game.db")
CURSOR = CONN.cursor()