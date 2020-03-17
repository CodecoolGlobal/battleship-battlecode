
# okok


import random
import os

import time


board = []

for x in range(0,10):
  board.append(["."] * 10)

# def print_board(board):
#   for row in board:
#     print (" ".join(row))

def print_board(board):
#     top = " ".join([chr(i) for i in range(ord('A'), ord('K'), +1)])# drukujemy alfabet w zakesie o skoku
    print("  0 1 2 3 4 5 6 7 8 9")
    cyfra = 0
    for row in board:
        print(cyfra, " ".join(row))
        cyfra += 1

print("Let's play Battleship!")

player_1 = input("Enter name: ")
players = [player_1]
os.system('cls||clear')


def random_pc_ship_row(board):
    return random.randint(0,len(board)-1)


def random_pc_ship_col(board):
    return random.randint(0, len(board[0])-1)

ship_row_1 = random_pc_ship_row(board)
ship_col_1 = random_pc_ship_col(board)

ship_row_2 = random_pc_ship_row(board)
ship_col_2 = random_pc_ship_col(board)

ship_row_3 = random_pc_ship_row(board)
ship_col_3 = random_pc_ship_col(board)

ship_row_4 = random_pc_ship_row(board)
ship_col_4 = random_pc_ship_col(board)

ship_row_5 = random_pc_ship_row(board)
ship_col_5 = random_pc_ship_col(board)

ship_row_6 = random_pc_ship_row(board)
ship_col_6 = random_pc_ship_col(board)

ship_row_7 = random_pc_ship_row(board)
ship_col_7 = random_pc_ship_col(board)

ship_row_8 = random_pc_ship_row(board)
ship_col_8 = random_pc_ship_col(board)

ship_row_9 = random_pc_ship_row(board)
ship_col_9 = random_pc_ship_col(board)

ship_row_10 = random_pc_ship_row(board)
ship_col_10 = random_pc_ship_col(board)


def prinit_pc_ships(board, ship_col_1, ship_row_1, ship_col_2, ship_row_2):
       if board[ship_col_1][ship_row_1] == '.' :
              board[ship_col_1][ship_row_1] = '='
       if board[ship_col_2][ship_row_2] == '.' :
              board[ship_col_2][ship_row_2] = '='
       if board[ship_col_3][ship_row_3] == '.' :
              board[ship_col_3][ship_row_3] = '='
       if board[ship_col_4][ship_row_4] == '.' :
              board[ship_col_4][ship_row_4] = '='
       if board[ship_col_5][ship_row_5] == '.' :
              board[ship_col_5][ship_row_5] = '='
       if board[ship_col_6][ship_row_6] == '.' :
              board[ship_col_6][ship_row_6] = '='
       if board[ship_col_7][ship_row_7] == '.' :
              board[ship_col_7][ship_row_7] = '='
       if board[ship_col_8][ship_row_8] == '.' :
              board[ship_col_8][ship_row_8] = '='
       if board[ship_col_9][ship_row_9] == '.' :
              board[ship_col_2][ship_row_9] = '='
       if board[ship_col_9][ship_row_9] == '.' :
              board[ship_col_10][ship_row_10] = '='

# def hint_12(ship_row_1, ship_col_1, ship_row_2, ship_col_2):
#        print ("Ship 1 is hidden:")    
#        print (board[ship_row_1][ship_col_1])
#        print ("Ship 2 is hidden:")    
#        print (board[ship_row_2][ship_col_2])

# def prinit_pc_ships(board, ship_col_1, ship_row_1, ship_col_2, ship_row_2):
#        if board[ship_col_1][ship_row_1] == '.' or board[ship_col_2][ship_row_2] == '.'  :
#               board[][] = "="


# prinit_pc_ships(board, ship_col_1, ship_row_1, ship_col_2, ship_row_2)

# print("hint :Ship1 :", str(ship_row_1), str(ship_col_1))
# print("hint :Ship2 :", str(ship_row_2), str(ship_col_2))

# def mark_pc(board, current_player, row, col):
#     board[int(row)][int(col)] = "s"
#     return board

print_board(board)


hit_count = 0

for turn in range(20):
    guess_row = int(float(input("Guess Row:(0-9) ")))
    guess_col = int(float(input("Guess Col:(0-9) ")))
    os.system('cls||clear')
    if hit_count == 1:
            print("You sunk first battleship!") 
    if hit_count == 20:
            print("Sorry You have lost the game, take a look on ships positions.")       
    if hit_count == 5:
            print("You sunk five battleships! You win!")
            print_board(board)
            break
    if turn == 3 :
            print("_"*20)
            print ("Hint :", ship_row_1, ship_col_1)
            print("_"*20)
    if turn == 6 :
            print("_"*20)
            print ("Hint :", ship_row_2, ship_col_2)
            print("_"*20)
    if turn == 9 :
            print("_"*20)
            print ("Hint :", ship_row_5, ship_col_5)
            print ("Hint :", ship_row_6, ship_col_6)
            print("_"*20)
    if turn == 12 :
            print("_"*20)
            print ("Hint :", ship_row_7, ship_col_7)
            print ("Hint :", ship_row_9, ship_col_9)
            print("_"*20)
    if turn == 18 :       
            print("_"*20)
            print ("Hint :", ship_row_3, ship_col_3)
            print ("Hint :", ship_row_4, ship_col_4)
            print ("Hint :", ship_row_8, ship_col_8)
            print("_"*20)
    if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
        hit_count = hit_count + 1
        board[guess_row][guess_col] = "H"
        print ("Congratulations! ")
    if (guess_row == ship_row_3 and guess_col == ship_col_3) or (guess_row == ship_row_4 and guess_col == ship_col_4) :
        hit_count = hit_count + 1
        board[guess_row][guess_col] = "H"
        print ("Congratulations! ")
    if (guess_row == ship_row_5 and guess_col == ship_col_5) or (guess_row == ship_row_6 and guess_col == ship_col_6) :
        hit_count = hit_count + 1
        board[guess_row][guess_col] = "H"
        print ("Congratulations! ")
    if (guess_row == ship_row_7 and guess_col == ship_col_7) or (guess_row == ship_row_8 and guess_col == ship_col_8) :
        hit_count = hit_count + 1
        board[guess_row][guess_col] = "H"
        print ("Congratulations! ")
    if (guess_row == ship_row_9 and guess_col == ship_col_9) or (guess_row == ship_row_10 and guess_col == ship_col_10):
        hit_count = hit_count + 1
        board[guess_row][guess_col] = "H"
        print ("Congratulations! ")
        if hit_count == 1:
                print("You sunk first battleship!") 
        if hit_count == 20:
                print("Sorry You have lost the game, take a look on ships positions.")       
        if hit_count == 5:
                print("You sunk five battleships! You win!")
                print_board(board)
                break
    else:
            if (guess_row < 0 or guess_row > 10)  or (guess_col < 0 or guess_col > 10):
                   print ("Oops, that's not even in the ocean.", player_1 )
            elif(board[guess_row][guess_col] == "H"):
                   board[guess_row][guess_col] = "S"
                   print ("You sunk first battleship!", player_1)
            else:
                 print ("You missed my battleship!", player_1)
                 board[guess_row][guess_col] = "M"
            print("_"*20)
            print( "You have killed", hit_count, "ships so far!", player_1)
            print (turn + 1, "turn out of 20")
            print("_"*20)
    print_board(board)
