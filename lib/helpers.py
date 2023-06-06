# update these to actually reference the SQL updates
from rich.console import Console 
from rich.theme import Theme


console = Console(width=50)

def welcome():
    print("Welcome to the Python Word Game!")

def menu():
    print("Choose an option: ")
    print("-------------------")
    print("1) Create new player")
    print("2) Play game")
    print("3) Create new puzzle")
    print("4) View leaderboard")
    print("5) Quit")

def register_player():
    username = input("Your username: ")
    a = Player(username)
    print(a)
    print(f"Hi there, {username}!")
    ready_to_play = input("Ready to play? Y/N: ")
    if ready_to_play.upper() == "Y":
        # select_puzzle()
        selected_puzzle_dummy_test = Puzzle("Puzzle1", "snake")
        play_game(selected_puzzle_dummy_test)

def validate_player():
    username = input("Your username: ")
    # validate that user does exist in DB already
    # if not --> throw message; try again or type 1 to create one 
    select_puzzle()

def select_puzzle():
    print("Which puzzle would you like to play?")
    # show list of puzzle options from DB, a get_all & display 
    # (only display what this user hasn't played)
    selected_puzzle = input("Enter puzzle name: ")
    # validate that selected_puzzle in list of available puzzles 
    #don't let user play a puzzle they've already played 
    play_game(selected_puzzle)

def create_puzzle():
    title = input("Your puzzle title, e.g. Puzzle1: ")
    solution = input("Your puzzle solution, a 5-letter word: ")
    new_puzzle = Puzzle(title.lower(), solution.lower())
    if new_puzzle: 
        print("Puzzle created")

def play_game(puzzle):
    # this should probably end up split into many functions 
    guesses = []
    for guess_num in range(1,7):
        new_guess = input("Enter your guess: ")
        # validate guesses with regex -> A-z only, no guesses more than 5 letters
        # eventually this would be does this equal puzzle.solution
        guesses.append(new_guess)
        handle_guess(guesses, puzzle.solution)
        if new_guess.lower() == puzzle.solution:
            console.print(f"[bold white on magenta] You guessed it! The word was {puzzle.solution} [/]")
            # create a new result
            exit_cli()
            break
    else: 
        end_game(puzzle.solution)

def handle_guess(guesses, word):
    for guess in guesses: 
        styled_guess = []
        for letter, correct_letter in zip(guess, word):
            if letter == correct_letter: 
                style = "bold white on green"
            elif letter in word: 
                style = "bold white on yellow"
            else: 
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
        console.print("".join(styled_guess))

def end_game(answer):
    # create a result here or before this is called?? 
    print(f"Game over! The word was {answer}")

def exit_cli():
    print("Until next time!")
    exit()

def invalid_input():
    print("That input is not valid. Type a number to select an option.")

from classes.puzzle import Puzzle
from classes.player import Player

