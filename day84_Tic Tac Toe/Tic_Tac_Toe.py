from random import randint


print('Welcome to my Tic Tac Toe game (Two player)- Adam CHEN JINGHAO')

player1 = input('What is your name, player 1?')
player2 = input('What is your name, player 2?')

def game():
    print("Let's roll a dict to decide who go first?")

    is_tie = True
    while is_tie:
        player1_dice = randint(1,6)
        player2_dice = randint(1,6)
        if player1_dice != player2_dice:
            is_tie=False

    print(f'{player1}: {player1_dice} and {player2}: {player2_dice}\n')

    if player1_dice > player2_dice:
        first = player1
        second = player2
        print(f'{first} go first, you are "X"')
        print(f'{second} is "O"')
    else:
        first = player2
        second = player1
        print(f'{first} go first, you are "X"')
        print(f'{second} is "O"')

    theGame = {
        '1':'1', '2':'2', '3':'3',
        '4':'4', '5':'5', '6':'6',
        '7':'7', '8':'8', '9':'9'
            }
    def gameBoard(number, sign):
        if theGame[number] != number:
            print('Another plays has this spot already. Pick one other.')
        elif theGame[number] == number:
            theGame[number] = sign
            
            print("+-+-+-+")
            print(f"|{theGame['1']}|{theGame['2']}|{theGame['3']}|")
            print("+-+-+-+")
            print(f"|{theGame['4']}|{theGame['5']}|{theGame['6']}|")
            print("+-+-+-+")
            print(f"|{theGame['7']}|{theGame['8']}|{theGame['9']}|")
            print("+-+-+-+")
            
            return True

    def winner_is():
        if theGame['1'] == theGame['2'] == theGame['3']:
            if theGame['1'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        elif theGame['4'] == theGame['5'] == theGame['6']:
            if theGame['4'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        elif theGame['7'] == theGame['8'] == theGame['9']:
            if theGame['7'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        elif theGame['1'] == theGame['4'] == theGame['7']:
            if theGame['1'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        elif theGame['2'] == theGame['5'] == theGame['8']:
            if theGame['2'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        elif theGame['3'] == theGame['6'] == theGame['9']:
            if theGame['3'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
        elif theGame['1'] == theGame['5'] == theGame['9']:
            if theGame['1'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        elif theGame['3'] == theGame['5'] == theGame['7']:
            if theGame['3'] == 'X':
                print(f'{first} is the winner')
            else:
                print(f'{second} is the winner')
            return True
        else:
            pass

    turn = 0
    game_on = True

    print("+-+-+-+")
    print(f"|{theGame['1']}|{theGame['2']}|{theGame['3']}|")
    print("+-+-+-+")
    print(f"|{theGame['4']}|{theGame['5']}|{theGame['6']}|")
    print("+-+-+-+")
    print(f"|{theGame['7']}|{theGame['8']}|{theGame['9']}|")
    print("+-+-+-+")

    while game_on:
        if turn %2 == 0:
            while True:
                while True:
                    number = input(f'{first}, Select your column ')
                    if int(number) > 9:
                        print('Please enter number from 1 - 9.')
                    elif 1 <= int(number) <= 9:
                        break
                sign = "X"
                if gameBoard(number, sign):
                    break
        elif turn %2 != 0:
            while True:
                while True:
                    number = input(f'{second}, Select your column ')
                    if int(number) > 9:
                        print('Please enter number from 1 - 9.')
                    elif 1 <= int(number) <= 9:
                        break
                sign = "O"
                if gameBoard(number, sign):
                    break

        turn += 1

        if winner_is():
            game_on = False
        elif turn == 9:
            print('It is a tie')
            game_on = False
        
    game_restart = input('Do you like to play again? (Y/N)')

    if game_restart == 'y':
        return True
    elif game_restart == 'n':
        print('See you next time!')
        return False

while True:
    if game() == False:
        break