from classes.puzzle import Puzzle
from classes.player import Player

def main(): 
    print("Welcome to the Python Word Game!")
    print("How would you like to begin?")
    print("""
Please select from the following:
------------------------------------""")
    print("1) Create new player")
    print("2) Play game")
    print("3) Create new puzzle")
    print("4) View leaderboard")
    print("5) Quit")

    choice = int(input())

    if choice == 1: 
        username = input("Your username: ")
        Player(username)
        print(f"Hi there, {username}!")
        ready_to_play = input("Ready to play? Y/N: ")
    
    if choice == 3: 
        title = input("Your puzzle title, e.g. Puzzle1: ")
        solution = input("Your puzzle solution, a 5-letter word: ")
        Puzzle(title, solution)

if __name__ == '__main__':
    main()

