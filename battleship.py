
def main():
    board = []
    init_board(board)
    print_board(board)
    print_menu()
    is_running = True
    ship = 1
    previous_move = []
    current_player = 1
    while is_running:
        coordinates = user_input()
        if not user_input_check(coordinates) :
            continue
        translated_cooridinates = translate_letters_to_numbers(coordinates)
        if not place_is_aviable(board, translated_cooridinates):
            continue
        if ship == 2:
            if place_is_aviable_next_part(board, previous_move, translated_cooridinates):
                continue
        if ship == 3:
            if not place_is_aviable_next_part(board, previous_move, translated_cooridinates):
                print("Dude only bertical or horizontal ships!")
                continue
        mark_player_coordinates(board, translated_cooridinates)
        previous_move = translated_cooridinates
        ship += 1
        print_board(board)
        if board.count('X') == 3:
            switch_player(current_player)


def init_board(board):
    for x in range(0, 5):
        board.append(["0"]*5)


def print_menu():
    print('Placement phase: Player 1 turn. 1 part ship.\nEnter coordinates\nSecond one will be two space ship.\nRemamber they can not be side by side!')


def round_menu():
    pass


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
    print("_"*12)
    print("NotSoBattleshipGame2")
    print("_"*12)
    top_label_print()
    side_label_print(board)


def user_input():
    coordinates = input("Please enter coordinates:\n")
    return coordinates


def place_is_aviable(board, coordinates):
    if board[coordinates[0]][coordinates[1]] == '0':
        return True
    else:
        print("Place already taken")
        return False


def place_is_aviable_next_part(board, previous_move, coordinates):
    if board[coordinates[0]] == board[previous_move[0]]:
        if coordinates[1] == previous_move[1] - 1 or coordinates[1] == previous_move[1] + 1:
            print("No no no - no side by side man!")
            return True
    if board[coordinates[1]] == board[previous_move[1]]:
        if coordinates[0] == previous_move[0] - 1 or coordinates[0] == previous_move[0] + 1:
            print("No no no - no side by side man!")
            return True


def user_input_check(coordinates):
    coordinates_list = list(coordinates)
    if len(coordinates_list) != 2:
        print("bla bla bla false input")
        return False
    possible_coordinates = ['a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E', '1', '2', '3', '4', '5']
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
        # coordinates_list[0] = int(coordinates_list[0]) + 1
        coordinates_list[1] = int(coordinates_list[1]) - 1
        # coordinates_list.reverse() bez reversa daje 4,0
    except:
        print('ERROR: Invalid input')
    return coordinates_list


def switch_player(current_player):
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1


def mark_player_coordinates(board, coordinates):
    board[coordinates[0]][coordinates[1]] = 'X'
    return board


def check_ship_end():
    pass


def shoot(coordinates):
    pass


def mark_shoot(coordinates, board):
    if board[coordinates[0]][coordinates[1]] == 'X':
        board[coordinates[0]][coordinates[1]] = 'H'
    if board[coordinates[0]][coordinates[1]] != 'X':
        board[coordinates[0]][coordinates[1]] = 'M'
# how to define Sunk status?      
    return board


def win_check():
    pass


if __name__ == '__main__':
    main()

