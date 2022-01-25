import random
import sys
from arguments import *
from termcolor import colored
import os
import time 
import math
import csv

def instruction():
    conformation = "n"
    while conformation == "n":
        print("Witaj w grze w kolko i krzyzyk!\n")
        print("Twoim celem jest zapelnienie tabeli gry w taki sposob, by nie znajdowaly sie w niej zadne kolka\n")
        print("Z kazdym ruchem bedziesz proszony o podanie wspolrzednej x-owej punktu, nacisniecie przycisku enter")
        print("a nastepnie powtorzenie tego samego dla wspolrzednej y-grekowej\n")
        print("Uwazaj na czerwone pola! Sa to pola zabronione. Za wybranie czerwonego pola twoje punkty zmniejsza sie o 2\n")
        print("Poziom latwy - tablica gry 8x8,  punkty ujemne za wybor zlego pola -2")
        print("Poziom sredni - tablica gry 12vs12, punkty ujemne za wybor zlego pola -4, bardziej nieregularny wybierak")
        print("Poziom trudny - tablica gry 20x20, punkty za wybor zlego pola -6\n")
        conformation = input("Wcisnij enter, zeby zaczac ")
        clear_console()

        
def win_game():
    print("Brawo! Udalo Ci sie wygrac po {0} ruchach, a Twoja liczba punktow wynosi {1}".format(move_number, round(points,2)))
    # for i in range(0,3):
    #     if points == player[i][1]:
    #         print("Gratulacje! Twoj wynik jest {0} najlepszym wynikiem! Zostales zapisany do tablicy najlepszych wynikow!".format(i))
    
    # print(player[0][1], player[1][1], player[2][1])
    
    for x in range(0,8):
         field_list[x] = (['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'])

def clear_console():
    os.system('clear')

def show_score_board():
    player = []
    file_names = ['best_scores_easy.csv', 'best_scores_medium.csv', 'best_scores_hard.csv']
    
    for i in range(0,3):
        with open(file_names[i], 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            
            for n in range (1,4):
                player.append(next(csv_reader))   
                
        if i == 0:
            print("Poziom latwy: \n ")
        if i == 1:
            print("Poziom sredni: \n ")
        if i == 2:
            print("Poziom trudny: \n")
        
        print("Miejsce 1: Nick {0}, wynik: {1}, czas gry: {2}, liczba ruchów {3}".format(player[0][0], player[0][1], player[0][2], player[0][3]))
        print("Miejsce 2: Nick {0}, wynik: {1}, czas gry: {2}, liczba ruchów {3}".format(player[1][0], player[1][1], player[1][2], player[1][3]))
        print("Miejsce 3: Nick {0}, wynik: {1}, czas gry: {2}, liczba ruchów {3}".format(player[2][0], player[2][1], player[2][2], player[2][3]))
        print()
        player.clear()
        
def save_score():
    global points, nickname, minutes, seconds, move_number, choice 
    
    if choice == 1:
        name = 'best_scores_easy.csv'
    if choice == 2:
        name = 'best_scores_medium.csv'
    if choice == 3:
        name = 'best_scores_hard.csv'
        
    nickname = input("Wpisz swoj nick: ")
    default = ['nickname','score','time','move_number']
    player = [] 
    player_statistics = [nickname, round(points,2), seconds, move_number]

    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for i in range (1,4):
            player.append(next(csv_reader))

    if float(player[0][1]) < player_statistics[1]:
        player[2] = player[1]
        player[1] = player[0]
        player[0] = player_statistics
    
    elif float(player[1][1]) < player_statistics[1]:
        player[2] = player[1]
        player[1] = player_statistics
    
    elif float(player[2][1]) < player_statistics[1]:
        player[2] = player_statistics

    with open(name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(default)
        csv_writer.writerows(player)
                

def disturb_list():
    global field_list, choice, n
    
    if choice == 1:
        m = random.randint(2,6)
    if choice == 2: 
        m = random.randint(8, 22)
    if choice == 3:
        m = random.randint(24, 60)
    
    while(m):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        field_list[i][j] = '+' 
        m -= 1
    return field_list
        
def print_board():
    global choice, n 
    
    print("     ", end = "")
    for x in range (1, n+1):
        if x < 10:
            print(x, end = "   ")
        else:
            print(x, end = "  ")
    print("\n   ", end = "")
    print("═" * (n * 4 + 1), end = "")
    
    for i in range(0,n):
        print()
        print(i + 1, end = ' ')
        for j in range(0,n):
            if j == 0 and i < 9:
                print(' ║', end = " ")
            else:
                print('║', end = " ")
            
            
            if field_list[i][j] == "O":
                text = colored(field_list[i][j], color = "blue")
                print(text, end = " ")
            elif field_list[i][j] == "X":
                text = colored(field_list[i][j], color = "yellow")
                print(text, end = " ")
            elif field_list[i][j] == "+":
                text = colored(field_list[i][j], color = "red")
                print(text, end = " ")
                
            if j == n - 1:
                 print('║\n ', end = "  ")
                 print('═' * (n * 4 + 1), end = " ")
    print()

def get_values():
    global  move_number, seconds, minutes, points
    print()
    start_time = time.perf_counter()
    
    try:
        x = int(input('Wprowadz numer wiersza: '))
    except ValueError:
        print("Wartosc musi byc liczba calkowita od 0 do 8")
        x = int(input('Wprowadz numer wiersza: '))
    try:
        y = int(input('Wprowadz number kolumny: '))
    except ValueError:
        print("Wartosc musi byc liczba calkowita od 0 do 8")
        y = int(input('Wprowadz number kolumny: '))
        
    x -= 1
    y -= 1
    move_number += 1

    end_time = time.perf_counter()
    current_time = math.trunc(end_time - start_time)
    seconds += current_time
    points -= (minutes * 1 + seconds * 0.017 + 0.1)
    
    while seconds > 59:
        seconds -= 60
        minutes += 1
        
    clear_console()
    print("Twoj czas gry: {0}m:{1}s".format(minutes, seconds))
    print("Twoja aktualna liczba punktów", round(points,2))
    print()
    return x, y
    

def check_fields(x, y):
    global n 
    
    if (x < 0 or x > n - 1):
        pass 
    elif (y < 0 or y > n - 1):
        pass
    else:  
        if field_list[x][y] == 'O':
            field_list[x][y] = "X" 


def change_field():
    global points, choice
    x, y= get_values()
    
    if choice == 1:
        m = 5 
    if choice == 2:
        m = 8
    if choice == 3:
        m = 12 
        
    if x in legal_fields and y in legal_fields and field_list[x][y] == "+":
       
        print("Nie można zmienić wartości pola zabronionego!")
        if choice == 1:
            text = colored('LICZBA PUNKTOW -2!', 'red')
        if choice == 2:
            text = colored('LICZBA PUNKTOW -4!', 'red')
        if choice == 3:
            text = colored('LICZBA PUNKTOW -6!', 'red')
        print(text)
        print()
        points -= choice * 2
  
    else: 
        k = random.randint(1, m )     
        check_fields(x, y)
        if k > 1:
            check_fields(x + 1, y)
        if k > 2:
            check_fields(x - 1, y)
        if k > 3:
            check_fields(x, y + 1)
        if k > 4:
            check_fields(x, y - 1)
        if k > 5:
            check_fields(x+2, y - 1)
        if k > 6:
            check_fields(x + 2, y + 2)
        if k > 7:
            check_fields(x - 1, y - 4)
        if k > 8:
            check_fields(x, y +3)
        if k > 9:
            check_fields(x+3, y +3)
        if k > 10:
            check_fields(x - 1, y - 3)
        if k > 11:
            check_fields(x - 2, y - 2)
        
def check_status():
    global o_number, number, n
    
    for x in range(0, n):
        for y in range(0, n):
            if field_list[x][y] == 'O':
                number +=1 
    o_number = number
    number = 0

    if(o_number < 120):
        return 1 
    else:
        return 0
    
def change_level():
    global choice, field_list, n
     
    print("1. Latwy ")
    print("2. Sredni ")
    print("3. Trudny")
    
    choice = int(input(("Wybierz poziom rozgrywki: (wpisz liczbe od 1 do 3) ")))
    while choice not in [1, 2, 3]:
        print("Liczba spoza zakresu! ")
        print("Wybierz poziom rozgrywki: (wpisz liczbe od 1 do 3) ")
    
    field_list.clear()
    
    if choice == 1:
        n = 8 
    if choice == 2:
        n = 12
    if choice == 3:
        n = 20
        
    for i in range(1,n+1):
        field_list.append(['O'] * n)
        