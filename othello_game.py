# Andy Le 92855131



def make_board_list(col, row):
    'Makes a list of the board'

    input_list = []
    for line in range(row):
        input_list.append(' . ' * col)
        
    return input_list

class game_state:
    def __init__(self):
        self._board = []
        self._turn = ''
        self._coordinate_list = []
        self._move_list = []
        self._valid_white_moves = []
        self._valid_black_moves = []
        self._command = []
        self._black_counter = 0
        self._white_counter = 0
        self._winner = ''
        self._mode =  ''

    ### Formatting functions

    

        
    def format_input(self, list_str):
        'Formats the inputted board'
        for each in list_str:
            self._board.append(each.split())
                           
    def set_turn(self, turn):
        'Sets the first turn'
        self._turn = turn
        
    def format_turn(self):
        'Formats and prints the turn'
        print('TURN: ' + self._turn)
                           
    def opposite_turn(self):
        'Changes the turn from one to another'
        if self._turn == 'W':
            self._turn = 'B'
        else:
            self._turn = 'W'

        
    def count_pieces(self):
        'Count the pieces of each color on the board and prints it'
        
        for row in self._board:
            for cell in row:
                if cell == 'W':
                    self._white_counter += 1
                elif cell == 'B':
                    self._black_counter += 1
                    
    def print_board(self):
        'Prints the board'
        for i in range(len(self._board)):
            for l in range(len(self._board[i])):
                print(self._board[i][l], end = ' ')
            print()

    ### GAME MECHANICS

            
    def place_disc(self, row, col, piece):
        'Places a disc onto the board with the correct piece'
        self._board[row-1][col-1] = piece


    def check_empty(self, row, col):
        'Checks if a cell is empty'
        return self._board[row-1][col-1] == '.'


    def check_cell_exists(self, row, col):
        'Checks if a cell exists'
        return 1 <= row <= len(self._board) and 1 <= col <= len(self._board[0])
    
        
    def get_coord_down(self, row, col):
        'Checks if the cells below can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row+1,col) and self._board[row][col-1] != self._turn and not self.check_empty(row+1,col):
            row += 1
            temp_list.append((row,col))
            
            if not self.check_cell_exists(row+1,col):
                temp_list = []
            
            
        if len(temp_list) > 0:
            if self._board[row][col-1] != self._turn:
                temp_list = []
                
        self._coordinate_list.extend(temp_list)


    def get_coord_up(self, row, col):
        'Checks if the cells above can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row-1,col) and self._board[row-2][col-1] != self._turn and not self.check_empty(row-1,col):
            row += -1
            temp_list.append((row,col))
            
            if not self.check_cell_exists(row-1,col):
                temp_list = []
            
        if len(temp_list) > 0 :
            if self._board[row-2][col-1] != self._turn:
                temp_list = []
        self._coordinate_list.extend(temp_list)
            

    
    def get_coord_left(self, row, col):
        'Checks if the cells to the left can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row,col-1) and self._board[row-1][col-2] != self._turn and not self.check_empty(row,col-1):
            col += -1
            temp_list.append((row,col))

            if not self.check_cell_exists(row,col-1):
                temp_list = []
                
        if len(temp_list) > 0:
            if self._board[row-1][col-2] != self._turn:
                temp_list = []

        self._coordinate_list.extend(temp_list)

    
    def get_coord_right(self, row, col):
        'Checks if the cells to the right can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row,col+1) and self._board[row-1][col] != self._turn and not self.check_empty(row,col+1):
            col += 1
            temp_list.append((row,col))

            if not self.check_cell_exists(row,col+1):
                temp_list = []
                
        if len(temp_list) > 0:
            if self._board[row-1][col] != self._turn:
                temp_list = []
                    
        self._coordinate_list.extend(temp_list)
                


    def get_coord_upleft(self, row, col):
        'Checks if the cells up and to the left can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row-1,col-1) and self._board[row-2][col-2] != self._turn and not self.check_empty(row-1,col-1):
            col += -1
            row += -1
            temp_list.append((row,col))

            if not self.check_cell_exists(row-1,col-1):
                temp_list = []
                
        if len(temp_list) > 0:
            if self._board[row-2][col-2] != self._turn:
                temp_list = []
        self._coordinate_list.extend(temp_list)
                


    def get_coord_upright(self, row, col):
        'Checks if the cells up and to the right can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row-1,col+1) and self._board[row-2][col] != self._turn and not self.check_empty(row-1,col+1):
            col += 1
            row += -1
            temp_list.append((row,col))

            if not self.check_cell_exists(row-1,col+1):
                temp_list = []
                
            if len(temp_list) > 0:
                if self._board[row-2][col] != self._turn:
                    temp_list = []
            self._coordinate_list.extend(temp_list)


    def get_coord_downright(self, row, col):
        'Checks if the cells down and to the right can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row+1,col+1) and self._board[row][col] != self._turn and not self.check_empty(row+1,col+1):
            col += 1
            row += 1
            temp_list.append((row,col))

            if not self.check_cell_exists(row+1,col+1):
                temp_list = []
                
            if len(temp_list) > 0:
                if self._board[row][col] != self._turn:
                    temp_list = []
            self._coordinate_list.extend(temp_list)
                


    def get_coord_downleft(self, row, col):
        'Checks if the cells down and to the left can be flipped, and appends those to a list'
        temp_list = []
        while self.check_cell_exists(row+1,col-1) and self._board[row][col-2] != self._turn and not self.check_empty(row+1,col-1):
            col += -1
            row += 1
            temp_list.append((row,col))
            
            if not self.check_cell_exists(row+1,col-1):
                temp_list = []

            if len(temp_list) > 0:
                if self._board[row][col-2] != self._turn:
                    temp_list = []
                    
            self._coordinate_list.extend(temp_list)

    def check_all_directions(self, row, col):
        'Check all the directions from the inputted move'
        self.get_coord_downleft(row, col)
        self.get_coord_left(row,col)
        self.get_coord_right(row,col)
        self.get_coord_up(row,col)
        self.get_coord_down(row,col)
        self.get_coord_downright(row,col)
        self.get_coord_upleft(row,col)
        self.get_coord_upright(row,col)



    def flip_all(self):
        'Flips all the cells in the coordinate list and resets the attributes'
        for coordinate in self._coordinate_list:
            row, col = coordinate
            if self._board[row-1][col-1] == 'W':
                self._board[row-1][col-1] = 'B'
            elif self._board[row-1][col-1] == 'B':
                self._board[row-1][col-1] = 'W'
                
        self._coordinate_list = []
        self._valid_white_moves = []
        self._valid_black_moves = []
        self._move_list = []
        self._black_counter = 0
        self._white_counter = 0
                
    def get_move(self):
        'Prompts the user for the next move'
        self._command = input().split()
        self._command = list(map(int, self._command))
        
            
    def all_move_list(self):
        'Creates a list of valid cells'
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self.check_empty(row+1,col+1):
                    self._move_list.append([row+1,col+1])

    def viable_move_list(self):
        'Creates a list of valid moves'
        for move in self._move_list:
            if self.check_valid_move(move[0],move[1]):
                if self._turn == 'W':
                    self._valid_white_moves.append(move)
                else:
                    self._valid_black_moves.append(move)
        self._coordinate_list = []
        
                    

    def switch_turns(self):
        'Switches turns if no possible moves for current turn'

        if self._turn == 'W':
            if len(self._valid_white_moves) == 0:
                self.opposite_turn()
                self.viable_move_list()
        else:
            if len(self._valid_black_moves) == 0:
                self.opposite_turn()
                self.viable_move_list()
                
    def not_game_over(self):
        'Checks if the game is still not over'
        return len(self._valid_white_moves) >0 or len(self._valid_black_moves) > 0

    def check_valid_move(self, row, col):
        'Checks if the current move is valid'
        
        temp_list = list(self._coordinate_list)
        self.check_all_directions(row,col)

        return self._coordinate_list > temp_list and  self.check_empty(row,col) and self.check_cell_exists(row,col)
        
            


    def white_winner(self):
        'Sets winner to white'
        self._winner = 'WINNER: WHITE'
        
    def black_winner(self):
        'Sets winner to black'
        self._winner = 'WINNER: BLACK'

    def determine_winner(self, setting):
        'Determines who wins the game'
        
        self._winner = 'WINNER: NONE'
        if setting == '<':
            if self._black_counter < self._white_counter:
                self.black_winner()
                
            elif self._white_counter < self._black_counter:
                self.white_winner()
                


        else:
            if self._black_counter > self._white_counter:
                self.black_winner()
            elif self._white_counter > self._black_counter:
                self.white_winner()
                
        return self._winner

    ### PLAYING THE GAME
        
    def start_game(self, board, turn):
        'Formats the users input and starts the game'
        self.format_input(board)
        self.count_pieces()
        self.print_board()

        self.set_turn(turn)
        

        self.switch_turns()
       


    def valid_action(self, row,col,mode):
        'If the inputted move is valid, continue the game'

        self.place_disc(row,col, self._turn)

        self.flip_all()

        self.opposite_turn()
        self.all_move_list()
        self.viable_move_list()
        self.count_pieces()

 
    
 #Testing purposes       print(self._valid_white_moves, self._valid_black_moves)


    def play_game(self, board, turn, mode):
        'Plays the game'
        self.start_game(board, turn)
        

        if not self.not_game_over():
            self.determine_winner(mode)
            return
        else:
            self.format_turn()
            self.get_move()
            
        while self.not_game_over:           
            while self.check_valid_move(self._command[0], self._command[1]):

                self.valid_action(mode)
                if not self.not_game_over():
                    self.determine_winner(mode)
                    return
                self.format_turn()
        
                self.get_move()
                            
            else:
                print('INVALID')
                self.get_move()
        
  



    





        
    
