from funcionts import *
from arguments import *

clear_console()
instruction()

while True:
    print("1. Zacznij gre")
    print("2. Zobacz najlepszze wyniki")
    print("3. Wybierz poziom trudnosci")
    choice = int(input("\nWybierz liczbe: "))


    if choice == 1:
        clear_console()
        disturb_list()
        clear_console()

        print("Twoj czas gry: {0}m:{1}s".format(minutes, seconds))
        print("Twoja aktualna liczba punktów: ", points)
        print()

        while True:    
            print_board()
            change_field()
            x = check_status()
            if(x):
                clear_console()
                save_score()
                win_game()
                break 

    if choice == 2:
        clear_console()
        show_score_board()
        print()

    if choice == 3:
        clear_console()
        change_level()
    





