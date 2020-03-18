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


def top_label_print():
    top_label = " "
    counter_for_size_of_board = 1
    while counter_for_size_of_board < 6:
        top_label += (" " + str(counter_for_size_of_board))
        counter_for_size_of_board += 1
    print('{:^10}'.format(top_label))


def side_label_print(board):
    counter_for_chr_into_int = 65
    for row in board:
        print(chr(counter_for_chr_into_int), " ".join(row))
        counter_for_chr_into_int += 1


def print_board(board):
    top_label_print()
    side_label_print(board)
    

def user_input(): #greg

        pass
#return coordinates [][]


def user_input_check(): #piotrek
        input_check = input("Podaj lokalizacje statku : \n")
    


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
    
