from helpers import ( 
    welcome, 
    menu,
    invalid_input,
    register_or_find_player,
    create_puzzle,
    view_leaderboard,
    exit_cli,
    invalid_input,
)

def main(): 
    welcome()
    while True: 
        menu()
        choice = input("> ")
        if choice == "1": 
            register_or_find_player()
        elif choice == "2":
            register_or_find_player()
        elif choice == "3": 
            create_puzzle()
        elif choice == "4": 
            view_leaderboard()
        elif choice == "5":
            exit_cli()
        else: 
            invalid_input()
    
if __name__ == '__main__':
    main()

