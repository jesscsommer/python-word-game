from rich.console import Console 
from rich.padding import Padding
from rich.theme import Theme
from classes.style import Style
import re

# do more with rich & console
# create some global styles to reference throughout
# rich supports themes --> check out 
cli_theme = Theme({
    "header": "bold black on white",
    "correct_letter": "bold white frame on green",
    "misplaced_letter": "bold white frame on yellow",
    "wrong_letter": "dim frame",
    "error": "bold white on red"
})
rich_style = Style.__rich_console__

console = Console(theme=cli_theme)

EXIT_WORDS = ["5", "exit", "quit"]

def welcome():
    welcome = Padding("Welcome to Letter Lasso!", (1, 1), style="header")
    console.print(welcome, justify="center")

def menu():
    console.print("Choose an option: ", style="header")
    print("1) Create new player")
    print("2) Play game")
    print("3) Create new puzzle")
    print("4) View leaderboard")
    print("5) Quit")
    
def check_input_for_exit(input):
    check = input.lower()
    if check in EXIT_WORDS:
        exit_cli()

def register_or_find_player():
    username = input("Your username: ").strip()
    check_input_for_exit(username)
    user = Player.find_by_username(username)
    
    if (user is None 
        and re.match(r"^[A-z0-9]+$", username)
        and 1 <= len(username) <= 8):
        new_player = Player.create(username)
        print(f"Hi there, {new_player.username}!")
        select_puzzle(new_player)
    elif not re.match(r"^[A-z0-9]+$", username) or len(username) < 1 or len(username) > 8:
        print('Usernames must be between 1 and 8 characters and cannot contain special characters(@_!$^...)')
        print('Please try again')
        register_or_find_player()
    else:
        print(f"Welcome back, {username}!")
        select_puzzle(user)

def select_puzzle(current_player):
    unplayed_puzzles = list(set(Puzzle.get_all()) - set(current_player.puzzles()))

    print("Which puzzle would you like to play?")
    for puzzle in unplayed_puzzles:
        print(f"Puzzle {puzzle.id}")

    selected_puzzle_id = input("Enter puzzle number: ") 
    selected_puzzle = Puzzle.find_by_id(int(selected_puzzle_id))

    if selected_puzzle in unplayed_puzzles:
        play_game(current_player, selected_puzzle, 1, [])
    else: 
        print("Not a valid puzzle number")
        select_puzzle(current_player)
    
def create_puzzle():
    solution = input("Your puzzle solution, a 5-letter word: ")
    solution = solution.strip()
    check_input_for_exit(solution)

    if (re.match(r"^[A-z]{5}$", solution)
        and not Puzzle.find_by_solution(solution)):
        Puzzle.create(solution.lower())
        print(f"Puzzle created for {solution}")
    else: 
        print("Solution must be a 5-letter word and unique among puzzles")
        create_puzzle()

def play_game(player, puzzle, start = 1, prev_guesses = []):
    guesses = prev_guesses
    console.print(f"[bold white frame on yellow] When a letter turns yellow it means that letter is in the solution word, but it is not in the correct spot [/]")
    console.print(f"[bold white frame on green] When a letter turns green it means that letter is in the solution word, and it is in the correct place [/]")
    console.print('You can type exit at any time to leave the CLI')
    for guess_num in range(start, 7):
        new_guess = input("Enter your guess: ")
        new_guess = new_guess.strip()
        check_input_for_exit(new_guess)

        if re.match(r"^[A-z]{5}$", new_guess):
            guesses.append(new_guess)
            handle_guess(guesses, puzzle.solution)
            if new_guess.lower() == puzzle.solution:
                console.print(f"[bold white on magenta] You guessed it! The word was {puzzle.solution} [/]")
                score = 350 - (50 * guess_num)
                new_result = Result.create(player.id, puzzle.id, score, guess_num)
                console.print(f"[bold white] Here are your results: {new_result} [/]")
                break
        else: 
            console.print(f"[bold white on red] Each guess must be a 5-letter string. Please try again. [/]")
            play_game(player, puzzle, guess_num, guesses)

    else: 
        new_result = Result.create(player.id, puzzle.id, 0, guess_num)
        print(f"Game over! The word was {puzzle.solution}")
        #menu()


def handle_guess(guesses, word):
    for guess in guesses: 
        styled_guess = []
        for letter, correct_letter in zip(guess, word):
            if letter == correct_letter: 
                style = "correct_letter"
            elif letter in word: 
                style = "misplaced_letter"
            else: 
                style = "wrong_letter"
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