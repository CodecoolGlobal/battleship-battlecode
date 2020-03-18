def main():
    board = []
    init_board(board)
    print_board(board)


def init_ships():       #greg
        pass
#return two ships 1 unit 2unit


def init_board(board):       
    for x in range(0,5):
        board.append(["0"]*5)
    


def print_menu():       #greg
        pass
# initial menu


def round_menu():       #piotrek
        pass
#round menu with player info


def print_board(board):
    i = 65
    print("  1 2 3 4 5")
    for row in board:
        print(chr(i), " ".join(row))
        i += 1
    

def user_input():
        pass
#return coordinates [][]
def user_input_check():
        pass
#correct input true false
def switch_player():
        pass
# return current player
def mark_player_coordinates(): #greg
        pass

def check_ship_end():
        pass
def switch_ship():
        pass
def shoot(coordinates):
        pass
# return hit or miss
def mark_shoot(coordinates):
        pass
#return H or M or Sink
def win_check():
        pass
# return True False if 3xH on player board
if __name__ == '__main__':
    main()
    
