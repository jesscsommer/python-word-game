# update these to actually reference the SQL updates
from rich.console import Console 
import re

# do more with rich & console
# create some global styles to reference throughout
# rich supports themes --> check out 
console = Console(width=150)

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
    check_username = Player.find_by_username(username)

    if (check_username is None 
        and re.match(r"^[a-zA-Z0-9]+$", username)):
        new_player = Player.create(username)
        print(f"Hi there, {new_player.username}!")
        select_puzzle(new_player)
    else:
        print("That username is taken")
        # offer option for user to retry with new username 
        # or go back to play game as the player with that name
        register_player()

def validate_player():
    # should refactor this so that the username logic is in one place; 
    # also I don't think we need the regex here 

    username = input("Your username: ")
    current_player = Player.find_by_username(username)
    if current_player is None and re.match(r"^[a-zA-Z0-9]+$", username):
        print('That username does not exist create the new username then start game')
        register_player()
    else:
        print(f"Welcome back {username}")
        select_puzzle(current_player)

def select_puzzle(current_player):
    unplayed_puzzles = list(set(Puzzle.get_all()) - set(current_player.puzzles()))
    unplayed_puzzle_ids = [puzzle.id for puzzle in unplayed_puzzles]
    
    print("Which puzzle would you like to play?")
    for puzzle in unplayed_puzzles: 
        print(f"Puzzle {puzzle.id}")

    selected_puzzle_id = input("Enter puzzle number: ")
    if int(selected_puzzle_id) in unplayed_puzzle_ids:
        play_game(current_player, selected_puzzle_id)
    else: 
        print("Not a valid puzzle number")
        select_puzzle(current_player)
    # validate that selected_puzzle in list of available puzzles 
    #don't let user play a puzzle they've already played 
    
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