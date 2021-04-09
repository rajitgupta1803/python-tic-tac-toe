import random

current_Player = str()
current_symbol_Player = str()
current_symbol_Computer = str()
avail_Players = ["Computer", "Player"]
Player_current = str()
Player_played = str()
Computer_choice = str()
inp_coordinate = []
row_1 = ["_", "_", "_"]
row_2 = ["_", "_", "_"]
row_3 = ["_", "_", "_"]
row_coor = ["a", "b", "c"]  
board = [row_1, row_2, row_3]
avail_choices = ["a 1", "a 2", "a 3", "b 1", "b 2", "b 3", "c 1", "c 2", "c 3"]
total_choices = ["a 1", "a 2", "a 3", "b 1", "b 2", "b 3", "c 1", "c 2", "c 3"]
col = int()
horiz_symbols = []
vert_symbols = []
diag_symbols = []
current_row = int()
Computer_choice_from_list = str()

current_row = int()
T = True
R = True

def draw_board():
    global board
    
    for i in board:
        for j in i:
            print(" " + j + "\u0332", end=" |")
        print()
        print()
    print()


def who_will_play():
    global Player_played
    global Player_current

    Player_current = random.choice(avail_Players)
    print(f"{Player_current} will play now!")
    Player_played = Player_current


def set_symbol():
    global current_symbol_Player
    global current_symbol_Computer
    
    inp_1 = str.upper(input("Which Symbol Do You Want?(X/O): "))
    if inp_1 == "X":
        current_symbol_Player = "X"
        current_symbol_Computer = "O"
    elif inp_1 == "O":
        current_symbol_Player = "O"
        current_symbol_Computer = "X"
    else:
        print("Please Enter A Valid Symbol")
        print()
        set_symbol()
        
def switch_Player():
    global Player_current
    global Player_played
    
    if Player_played == "Player":
        Player_current = "Computer"
        Player_played = "Computer"
        print(f"{Player_current} will play now!")
        print()
    elif Player_played == "Computer":
        Player_current = "Player"
        Player_played = "Player"
        print(f"{Player_current} will play now!")
        print()


def set_coordinate():
    global Computer_choice
    global inp_coordinate
    global R

    if Player_current == "Player":
        inp = str.lower(input("Enter the address of the cell you want to edit: "))
        inp_coordinate = inp.split()
        while R:
            if inp not in total_choices:
                print("Please Enter A Valid Address")
                print()
                inp = str.lower(input("Enter the address of the cell you want to edit: "))
                inp_coordinate = inp.split()
            else:
                if inp in avail_choices:
                    avail_choices.pop(avail_choices.index(inp))
                    break
                elif inp not in avail_choices:
                    print("This cell has been already edited!")
                    print()
                    inp = str.lower(input("Enter the address of the cell you want to edit: "))
                    inp_coordinate = inp.split()

def edit_board_comp(current_row, col, avail_choices, Computer_choice_from_list):
    global vert_symbols
    global horiz_symbols
    global diag_symbols
    global Computer_choice
    g = False   
    
    for u in range(0, 3):
        diag_symbols.append(board[u][u])
        if diag_symbols.count(current_symbol_Player) == 2 or diag_symbols.count(current_symbol_Computer) == 2:
            if "_" in diag_symbols:
                col = diag_symbols.index("_") + 1
                current_row = diag_symbols.index("_") 
                g = True
                break
    if not g:
        diag_symbols = []
        diag_symbols = [board[0][2], board[1][1], board [2][0]]
        if diag_symbols.count(current_symbol_Player) == 2 or diag_symbols.count(current_symbol_Computer) == 2:
                if "_" in diag_symbols:
                    current_row = diag_symbols.index("_") 
                    if current_row == 0:
                        col = 3
                    elif current_row == 1:
                        col = 2
                    elif current_row == 2:
                        col = 1
                    g = True
    diag_symbols = []
    if not g:
        for k in range (0,3):
            for l in range(0,3):
                vert_symbols.append(board[l][k])
                horiz_symbols.append(board[k][l])
                if horiz_symbols.count(current_symbol_Player) == 2 or horiz_symbols.count(current_symbol_Computer) == 2:
                    if "_" in horiz_symbols:
                        vert_symbols = [] 
                        col = horiz_symbols.index("_") + 1
                        current_row = k
                        g = True
                        break
                elif vert_symbols.count(current_symbol_Player) == 2 or vert_symbols.count(current_symbol_Computer) == 2:
                    if "_" in vert_symbols:
                        current_row = vert_symbols.index("_") 
                        col = k + 1
                        g = True
                        break
            vert_symbols = []
            horiz_symbols = [] 
    if not g:
        while True:
            Computer_choice_from_list = random.choice(avail_choices)
            Computer_choice = Computer_choice_from_list.split()
            avail_choices.pop(avail_choices.index(Computer_choice_from_list))
            
            if Computer_choice[0] == "a":
                current_row = 0
            elif Computer_choice[0] == "b":
                current_row = 1
            elif Computer_choice[0] == "c":
                current_row = 2
            col = int(Computer_choice[1])

            if board[current_row][col - 1] == "_":
                board[current_row][col - 1] = current_symbol_Computer   
                break
    elif g:
        board[current_row][col - 1] = current_symbol_Computer     
          
def edit_board_player(player_symbol, inp, current_row):
    global col

    if inp[0] == "a":
        current_row = 0
    elif inp[0] == "b":
        current_row = 1
    elif inp[0] == "c":
        current_row = 2
    else:
        print("Please enter a valid address")

    col = int(inp_coordinate[1])
        
    board[current_row][col - 1] = player_symbol

def move(Player):
    if Player == "Player":
        edit_board_player(current_symbol_Player, inp_coordinate, current_row)
    else:
        edit_board_comp(current_row, col, avail_choices, Computer_choice_from_list)
        
def check_win():
    global vert_symbols
    global horiz_symbols
    global diag_symbols
    global T
    global board
    
    for n in range(0,3):
        diag_symbols.append(board[n][n])   
    for k in range (0,3):
        for l in range(0,3):
            vert_symbols.append(board[l][k])
            horiz_symbols.append(board[k][l])
        if vert_symbols[0] == vert_symbols[1] == vert_symbols[2] != "_":
            print(f"{Player_played} wins!")
            quit()
        elif horiz_symbols[0] == horiz_symbols[1] == horiz_symbols[2] != "_":
            print(f"{Player_played} wins!")
            quit()
        else:
            if diag_symbols[0] == diag_symbols[1] == diag_symbols[2] != "_":
                print(f"{Player_played} wins!")
                quit()
            elif board[0][2] == board[1][1] == board[2][0] != "_":
                print(f"{Player_played} wins!")
                quit()
        vert_symbols = []
        horiz_symbols = []
    diag_symbols = []
    if "_" not in row_1 and "_" not in row_2 and "_" not in row_3:
        print("Its a draw!")
        quit()

print()
print("Instructions:", "\nTo enter the address of the cells, type the address of the row followed by the space and then the address of the column", "\nThe addresses of the rows are a, b, c and those of columns are 1, 2, 3", "\nFor eg, if you want to put your symbol on the first cell of the first row, type->a 1(make sure to put the space between row address and column address)")   
print()     
draw_board()
set_symbol()
who_will_play()

while T:    
    set_coordinate()
    move(Player_current)
    draw_board()    
    check_win()
    switch_Player()

