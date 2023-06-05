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

    elif choice == 2: 
        username = input("Your username: ")
        # validate that user does exist in DB already
        # if not --> throw message; try again or type 1 to create one 
        select_puzzle()

    elif choice == 3: 
        title = input("Your puzzle title, e.g. Puzzle1: ")
        solution = input("Your puzzle solution, a 5-letter word: ")
        new_puzzle = Puzzle(title.lower(), solution.lower())
        if new_puzzle: 
            print("Puzzle created")
            main_menu()
    
    elif choice == 4: 
        pass 

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
    # (only display what this user hasn't played)
    selected_puzzle = input("Enter puzzle name: ")
    # validate that selected_puzzle in list of available puzzles 
    #don't let user play a puzzle they've already played 
    play_game(selected_puzzle)

def play_game(puzzle): 
    for guess_num in range(7):
        guess = input("Enter your guess: ")
        # validate guesses with regex -> A-z only, no guesses more than 5 letters
        # eventually this would be does this equal puzzle.solution
        if guess.lower() == "snake":
            print("Correct")
            break
        else: 
            correct_letters = {
                letter for letter, correct in zip(guess, "snake") if letter == correct
            }
            print(f"Correct: {correct_letters}")
            print("Wrong")

if __name__ == '__main__':
    main()

