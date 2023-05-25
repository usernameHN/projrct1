import pyfiglet 
import termcolor
import time
import random
from os import _exit

print( time.time())
taitel = pyfiglet.figlet_format("tic toc toe", font="slant")
print(termcolor.colored(taitel, color="yellow"), end="")

game_board = [["-" , "-" , "-"],
              ["-" , "-" , "-"],
              ["-" , "-" , "-"]]

def show() :
    for i in game_board :
        for j in i :
            if j == "X":

                print(termcolor.colored(j, color="blue"), end=" ")

            elif j == "O":
                print(termcolor.colored(j, color="red"), end=" ")   

            else:
                print(j, end=" ")
        print()             

def full() :
    sum = 0 
    for i in game_board :
        for j in i :
            if j == "-" :
                sum += 1

    if j == 0 :
        return 1
    else :
        return 0            

def check_game() :
    for i in range(3):
        x = 0
        o = 0
        for j in range (3):
            if game_board[i][j] == "X":
                x += 1

            elif game_board[i][j] == "O":
                o += 1
        if x == 3:
            print("player 1 win") 
            exit()       
       
        elif o == 3:
            print("player 2 win ")
            exit()

    for i in range(3):
        x = 0
        o = 0
        for j in range (3):
            if game_board[i][j] == "X":
                x += 1

            elif game_board[i][j] == "O":
                o += 1
        if x == 3:
            print("player 1 win") 
            exit()       
       
        elif o == 3:
            print("player 2 win ")
            exit()

    x = 0
    o = 0

    for i in range (3):
            if game_board[i][j] == "X":
                x += 1

            elif game_board[i][j] == "O":
                o += 1
    if x == 3:
        print("player 1 win") 
        exit()       
       
    elif o == 3:
        print("player 2 win ")
        exit()

print("playe with player : enter yes \n playe with mps : enter no")
choise_player = input("select player :")
    
if choise_player == "yes" :
    show()
    while True :

        print("player 1")
        while True:
            row = int(input("row :") )
            cell = int(input("cell :"))

            if 0 <= row <=2 and 0 <= cell <=2 :
                if game_board[row][cell] == "-":
                    game_board[row][cell] = "X" 
                    break

                else :
                    print("inja nemishe (-_-)")       
            else :
                print("adam bash")
        show()
        check_game()
        ful = full()
        if ful == 1 :
            print("drow")
            break

        print("player 2")
        while True:
            row = int(input("row :") )
            cell = int(input("cell :"))
            if 0 <= row <= 2 and 0 <= cell <= 2 :
                if game_board[row][cell] == "-" :
                    game_board[row][cell] = "O"
                    break

                else:
                    print("iz to baeed bod >_<")  
            else :
                print("adam bash ")
        show()
        check_game()
        ful = full()
        if ful == 1 :
            print("drow")
            break

elif choise_player == "no" :
    show()
    while True :

        print("player 1")
        while True:
            row = int(input("row :") )
            cell = int(input("cell :"))

            if 0 <= row <=2 and 0 <= cell <=2 :
                if game_board[row][cell] == "-":
                    game_board[row][cell] = "X" 
                    break

                else :
                    print("inja nemishe (-_-)")       
            else :
                print("adam bash")
        show()
        check_game()
        ful = full()
        if ful == 1 :
            print("drow")
            break

        print("mpc player :")
        while True :
            row = random.randint(0, 2)
            cell = random.randint(0, 2)

            if 0 <= row <=2 and 0 <= cell <=2 :
                if game_board[row][cell] == "-" :
                    game_board[row][cell] = "O"
                    break
        show()
        check_game()
        ful = full()
        if ful == 1 :
            print("drow")
            break

else:
    print("mesl adam vared kon ")                

print(time.time())
# hour = 0
# min = 0
# sec = int(finish - start)

# if sec >= 3600 :
#     hour = sec / 3600
#     sec = sec % 3600
#     if sec >= 60:
#         min = sec / 60
#         sec = sec % 60

# elif sec < 3600 :
#     min = sec / 60 
#     sec = sec % 60
                
# print("\ntime :", int(hour), ":", int(min), ":", sec)                