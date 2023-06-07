# update these to actually reference the SQL updates
from rich.console import Console 
import re


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
    username = input("Your username: ").strip()
    check_username = Player.find_by_username(username)
    if check_username is None and re.match(r"^[a-zA-Z0-9]+$", username) and username != "5":
        Player.create(username)
        print(f"Hi there, {username}!")
        ready_to_play = input("Ready to play? Y/N: ")
        if ready_to_play.upper() == "Y":
            # selected_puzzle_dummy_test = Puzzle("Puzzle1", "snake")
            select_puzzle()
        else:
            menu()
    elif username == "5":
        exit_cli()
    else:
        print('That username is taken or invalid try another one')
        register_player()

def validate_player():
    username = input("Your username: ").strip()
    check_username = Player.find_by_username(username)
    if check_username is not None and re.match(r"^[a-zA-Z0-9]+$", username) and username != "5":
        print(f"Welcome back {username}")
        ready_to_play = input("Ready to play? Y/N: ")
        if ready_to_play.upper() == "Y":
                select_puzzle()
        else:
                menu()
    elif username == "5":
        exit_cli()
    else:
        print('That username does not exist create the new username then start game')
        register_player()

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

def play_game(player, puzzle, start = 1, prev_guesses = []):
    guesses = prev_guesses
    for guess_num in range(start, 7):
        new_guess = input("Enter your guess: ")
        if re.match(r"^[A-z]{5}$", new_guess):
            guesses.append(new_guess)
            handle_guess(guesses, puzzle.solution)
            if new_guess.lower() == puzzle.solution:
                console.print(f"[bold white on magenta] You guessed it! The word was {puzzle.solution} [/]")
                # create a new result
                score = 350 - (50 * guess_num)
                new_result = Result.create(player.id, puzzle.id, score, guess_num)
                console.print(f"[bold white] Here are your results: {new_result} [/]")
                exit_cli()
                break
        else: 
            console.print(f"[bold white on red] Each guess must be a 5-letter string. Please try again. [/]")
            play_game(player, puzzle, guess_num, guesses)

    else: 
        new_result = Result.create(player.id, puzzle.id, 0, guess_num)
        print(f"Game over! The word was {puzzle.solution}")
        exit_cli()


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

def exit_cli():
    print("Until next time!")
    exit()

def invalid_input():
    print("That input is not valid. Type a number to select an option.")

from classes.puzzle import Puzzle
from classes.player import Player
from classes.result import Result