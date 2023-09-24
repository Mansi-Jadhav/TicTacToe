import os
import random

def display_board(rows):
    clear = lambda: os.system('cls')
    print(rows[1] + '|' + rows[2] + '|' + rows[3])
    print(rows[4] + '|' + rows[5] + '|' + rows[6])
    print(rows[7] + '|' + rows[8] + '|' + rows[9])

def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'

def player_choice():
    choice = 'Wrong'
    while choice not in ('X', 'O'):
        choice = input("Player1 choose : (X or O) ").upper()
        if choice not in ('X', 'O'):
            print("Enter a valid choice")
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def check_space(rows,position):
    return rows[position] == ' '

def check_full(rows):
    for i in range(1, 10):
        if check_space(rows, i):
            return False
    return True

def player_input(rows):
    position = 0
    while (position not in range(1, 10)) or not check_space(rows, position):
        position = int(input("Player position: ").upper())
    return position

def check_result(rows, mark):
    return (rows[1]==rows[2]==rows[3]==mark
            or rows[4]==rows[5]==rows[6]==mark
            or rows[7]==rows[8]==rows[9]==mark
            or rows[1]==rows[4]==rows[7]==mark
            or rows[2]==rows[5]==rows[8]==mark
            or rows[3]==rows[6]==rows[9]==mark
            or rows[1]==rows[5]==rows[9]==mark
            or rows[3]==rows[5]==rows[7]==mark)

def play_again():
    again = input("Do you want to play again? Y or N: ").upper()
    return again == 'Y'

while True:
    rows = [' '] * 10
    player1, player2 = player_choice()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N : ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(rows)
            position = player_input(rows)
            rows[position] = player1
            if check_result(rows, player1):
                display_board(rows)
                print("Player1 has won!!")
                game_on = False
            else:
                if check_full(rows):
                    display_board(rows)
                    print("It's a TIE!")
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            display_board(rows)
            position = player_input(rows)
            rows[position] = player2
            if check_result(rows, player2):
                display_board(rows)
                print("Player2 has won!!")
                game_on = False
            else:
                if check_full(rows):
                    display_board(rows)
                    print("It's a TIE!")
                    game_on = False
                else:
                    turn = 'Player1'

    if not play_again():
        break
