from classes.puzzle import Puzzle
from classes.player import Player

def main(): 
    print("Welcome to the Python Word Game!")
    print("How would you like to begin?")
    main_menu()
    choice = int(input())

    if choice == 1: 
        username = input("Your username: ")
        a = Player(username)
        print(a)
        print(f"Hi there, {username}!")
        ready_to_play = input("Ready to play? Y/N: ")
        if ready_to_play.upper() == "Y":
            select_puzzle()

    if choice == 3: 
        title = input("Your puzzle title, e.g. Puzzle1: ")
        solution = input("Your puzzle solution, a 5-letter word: ")
        new_puzzle = Puzzle(title, solution)
        if new_puzzle: 
            print("Puzzle created")
            main_menu()

def main_menu(): 
    print("""
Please select from the following:
------------------------------------""")
    print("1) Create new player")
    print("2) Play game")
    print("3) Create new puzzle")
    print("4) View leaderboard")
    print("5) Quit")

def select_puzzle():
    print("Which puzzle would you like to play?")
    # show list of puzzle options from DB, a get_all & display
    selected_puzzle = input("Enter puzzle name: ")
    # validate that selected_puzzle in list of avaialble puzzles 
    play_game(selected_puzzle)

def play_game(puzzle): 
    guess = input("Enter your guess: ")
    if guess.upper() == "SNAKE":
        print("Correct")
    else: 
        print("Wrong")

if __name__ == '__main__':
    main()

