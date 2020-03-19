<<<<<<< HEAD
def init_ships():       #greg
        ship1 = 1
        ship2 = 2
        return ship1, ship2

#return two ships 1 unit 2unit
=======
>>>>>>> Grzesiek

def main():
    board = []
    init_board(board)
    print_board(board)
    user_input_check()

def init_board(board):       
    for x in range(0,5):
        board.append(["0"]*5)
   

def init_ships():       #greg
        ship1 = 1
        ship2 = 2
        return ship1, ship2


def print_menu():       #greg
        print('Placement phase: Player 1 turn. 1 part ship. Enter coordinates')
<<<<<<< HEAD
=======

# initial menu
>>>>>>> Grzesiek

# initial menu

def round_menu():       #piotrek
        pass
#round menu with player info

<<<<<<< HEAD
def print_board():
        print(board)
#print board
=======


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


class ValidationError(ValueError): 
    pass

def RangeValidator(text, num, r):
    if num in r:
        return num
    raise ValidationError(text)

def ValidCol(c): 
    return RangeValidator("Columns must be in the range of 1 to 5 (inclusive)", c, range(1,6))

def ValidRow(r): 
    return RangeValidator("Rows must be in the range of A to E(exclusive)", r, range(chr(ord('a'), ord('e')))) # do korkety

def user_input_check(): #piotrek
    def GetInt(text, validator=None):
        print()
        while True:
            n = input(text)
            try:
                n = int(n)

                return n if validator is None else validator(n)

            except ValueError as ve:
                # prints ValidationErrors directly - else generic message:
                if isinstance(ve, ValidationError):
                    print(ve)
                else:
                    print("Invalid input: ", n)


    column = GetInt("Pleased enter column: ", ValidCol)
    row = GetInt("Pleased enter row: ", ValidRow)
    print( row, column)


def switch_player():
        pass
# return current player


def mark_player_coordinates(): #greg
        pass

def check_ship_end():
        pass


>>>>>>> Grzesiek
def user_input():
        pass
#return coordinates [][]

def user_input_check(coordinates):
        coordinates_list = list(coordinates)
    if len(coordinates_list) != 2:
        return False
    possible_coordinates = ['a','b','c','d','e','A','B','C','D','E','1','2','3','4','5','6']
    if coordinates_list[0] not in possible_coordinates or coordinates_list[1] not in possible_coordinates:
        print("Invalid Input try agian")
        return False
    return True

def translate_letters_to_numbers(coordinates):
    coordinates_list = list(coordinates)
    try:
        if coordinates_list[0] == 'A' or coordinates_list[0] == 'a':
            coordinates_list[0] = 0
        if coordinates_list[0] == 'B' or coordinates_list[0] == 'b':
            coordinates_list[0] = 1
        if coordinates_list[0] == 'C' or coordinates_list[0] == 'c':
            coordinates_list[0] = 2
        if coordinates_list[0] == 'D' or coordinates_list[0] == 'd':
            coordinates_list[0] = 3
        if coordinates_list[0] == 'E' or coordinates_list[0] == 'e':
            coordinates_list[0] = 4
        if coordinates_list[0] == 'F' or coordinates_list[0] == 'f':
            coordinates_list[0] = 5
        # coordinates_list[0] = int(coordinates_list[0]) + 1
        coordinates_list[1] = int(coordinates_list[1]) -1
        coordinates_list.reverse() 
    except:
        print('ERROR: Invalid input')
    return coordinates_list    

def place_is_aviable(board, coordinates):
    try:
        if board[coordinates[0]][coordinates[1]] == 0:
            return True
    except:
        return False

#correct input true false
def switch_player():
        pass
# return current player
def mark_player_coordinates(board, coordinates): #greg
        board[coordinates[0]][coordinates[1]] = 'X'
        return board

def check_ship_end():
        pass
def switch_ship(current_ship):
        current_ship += 1
        pass
def shoot(coordinates):
        pass
# return hit or miss
    

def mark_shoot(coordinates, board)
        if board[coordinates[0]][coordinates[1]] = 'X'
                board[coordinates[0]][coordinates[1]] = 'H'
        if board[coordinates[0]][coordinates[1]] != 'X'
                board[coordinates[0]][coordinates[1]] = 'M'
        # how to define Sunk status?       
                return board

#return H or M or Sink
def win_check():
        pass
# return True False if 3xH on player board

if __name__ == '__main__':
    main()
