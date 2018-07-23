#ANDY LE 92855131
import point
import math
import othello_game


# This constant specifies the radius, in fractional coordinates, of the
# spots that are created.  Try changing this to be larger or smaller and
# see what happens.
SPOT_RADIUS_FRAC = 0.05



        

class Spot:
    def __init__(self, center: point.Point, radius_frac: float):
        '''
        Initialize a newly-created Spot object, given its center
        point (a Point object) and the spot's radius (in
        fractional coordinates).
        '''
        self._center = center
        self._radius_frac = radius_frac


    def center(self) -> point.Point:
        '''
        Returns a Point object representing this Spot's center.
        '''
        return self._center


    def radius_frac(self) -> float:
        '''
        Returns the radius of this Spot, in terms of fractional
        coordinates.
        '''
        return self._radius_frac

    
    def contains(self, point: point.Point) -> bool:
        '''
        Returns True if the given Point object lies within
        this Spot, False otherwise.
        '''


        return self._center.frac_distance_from(point) <= self._radius_frac



class SpotsState:
    def __init__(self, game = othello_game.game_state()):
        '''
        Initializes the state of the Spots application.  Initially,
        there are no spots.
        '''
        self._white_spots = []
        self._black_spots = []

        self._starting_white = []
        self._starting_black = []

        self._cell_width = 0
        self._cell_height = 0
        self._width = 0
        self._height = 0
        self._turn = ''
        self._mode = ''
        
        self._winner = ''
        self._game_started = False
        self._game_ended = False

        self._logic = game


    def display_winner(self):
        'Displays the winner of the game'
        return self._logic.determine_winner(self._mode)

    def display_opposite(self):
        'Returns the opposite turn'
        if self._turn == 'W':
            return 'B'
        elif self._turn == 'B':
            return 'W'
            
    def all_spots(self) -> [Spot]:
        '''Returns a list of all of the Spot objects that currently exist.'''
        return self._spots

          

        


    def handle_click(self, click_point: point.Point, width, height, row, col, mode) -> None:
        '''
        Handle a click on the given point, by either removing the
        spot in which the point lies, or by adding a new spot centered
        at the given point.
        '''

        self._mode = mode
        self._width = width
        self._height = height

        click_width , click_height = click_point.pixel(width, height)

        self._cell_width = width / col
        self._cell_height = height / row
        
        
        


    
        ratio_width = math.ceil(click_width / self._cell_width) 
        ratio_height = math.ceil(click_height / self._cell_height)
        
        if self._turn == 'B':
            


            circle_point = point.from_pixel(
                (self._cell_width * ratio_width) - (self._cell_width / 2)
                , (self._cell_height * ratio_height) - (self._cell_height / 2)
                , width, height)
            if not self._game_started:
                self.replace_initial_white(ratio_height, ratio_width, circle_point)

            if self._game_started:
                self._logic.all_move_list()
                self._logic.viable_move_list()
                
                if len(self._logic._valid_black_moves) != 0:

                    if self.check_move(ratio_height, ratio_width):
                        
                        self._black_spots.append(Spot(circle_point, SPOT_RADIUS_FRAC))
                        self.flip_white()
                        
                        self.valid_action(ratio_height, ratio_width, self._mode)
                        self.determine_winner()
       
                        self.switch_turns()
                        return
                        
                        
                elif len(self._logic._valid_black_moves) == 0:
                    
                    self.switch_turns()
                    self._logic.opposite_turn()
                    
                    self._logic.all_move_list()
                    self._logic.viable_move_list()
                    
                    if len(self._logic._valid_white_moves)!= 0:

                        if self.check_move(ratio_height, ratio_width):
                            self._white_spots.append(Spot(circle_point, SPOT_RADIUS_FRAC))
                            self.flip_black()
                           
                            self.valid_action(ratio_height, ratio_width, mode)
                            self.determine_winner()
                            self.switch_turns()
                    else:
                        self.determine_winner()

    

        elif self._turn == 'W':

        
            circle_point = point.from_pixel(
                (self._cell_width * ratio_width) - (self._cell_width / 2)
                , (self._cell_height * ratio_height) - (self._cell_height / 2)
                , width, height)
            if not self._game_started:
                self.replace_initial_black(ratio_height, ratio_width, circle_point)
            

            if self._game_started:
                self._logic.all_move_list()
                self._logic.viable_move_list()
                if len(self._logic._valid_white_moves) != 0:

                    if self.check_move(ratio_height, ratio_width):


                        self._white_spots.append(Spot(circle_point, SPOT_RADIUS_FRAC))
                        self.flip_black()
                        
                        self.valid_action(ratio_height, ratio_width,mode)
                        self.determine_winner()
                        self.switch_turns()
                        return
                        

                
                if len(self._logic._valid_white_moves) == 0:
                    self.switch_turns()
                    self._logic.opposite_turn()
                    
                    self._logic.all_move_list()
                    self._logic.viable_move_list()
                        
                    if len(self._logic._valid_black_moves) != 0:
                        
                        if self.check_move(ratio_height, ratio_width):
                            
                            self._black_spots.append(Spot(circle_point, SPOT_RADIUS_FRAC))
                            self.flip_white()
                            
                            self.valid_action(ratio_height, ratio_width, self._mode)
                            self.determine_winner()
                            self.switch_turns()
                    else:
                        self.determine_winner()
    


        



    def start_game(self, col, row):
        'Starts the game by initalizing the board'
        self._game_started = True
        self._logic.set_turn(self._turn)

        
        board_list = othello_game.make_board_list(col, row)
        self._logic.format_input(board_list)

        for black in self._starting_black:
            self._logic._board[black[0]-1][black[1]-1] = 'B'
        for white in self._starting_white:
            self._logic._board[white[0]-1][white[1]-1] = 'W'

        self._logic.count_pieces()
        self._logic.all_move_list()
        self._logic.viable_move_list()
        
        self.determine_winner()
        
 
        
    def check_move(self, row, col):
        'Checks if the clickpoint is a valid move'

        return self._logic.check_valid_move(row, col)
    
    def valid_action(self, row, col, mode):
        'Continues the game by making a valid action'
        self._logic.valid_action(row,col, mode)
        
    def flip_black(self):
        'Flips all the black discs that need to be fliped'
        for coordinate in self._logic._coordinate_list:
            row, col = coordinate
            
            circle_point = point.from_pixel(
                (self._cell_width * col) - (self._cell_width / 2)
                , (self._cell_height * row) - (self._cell_height / 2)
                , self._width, self._height)
            
            self.replace_black(circle_point)
        

    def flip_white(self):
        'Flips all the white discs that need to be fliped'
        for coordinate in self._logic._coordinate_list:
            row, col = coordinate
            
            circle_point = point.from_pixel(
                (self._cell_width * col) - (self._cell_width / 2)
                , (self._cell_height * row) - (self._cell_height / 2)
                , self._width, self._height)
            
            self.replace_white(circle_point)
    

        
    def replace_black(self, circle_point: point.Point):
        'Redraws the black spots to make them white spots'
        for spot in self._black_spots:
            if spot._center.pixel(self._width, self._height) == circle_point.pixel(self._width, self._height):
                self._black_spots.remove(spot)
                
        self._white_spots.append(Spot(circle_point, SPOT_RADIUS_FRAC))

    def replace_white(self, circle_point: point.Point):
        'Redraws the white spots to make them black spots'
        for spot in self._white_spots:
            if spot._center.pixel(self._width, self._height) == circle_point.pixel(self._width, self._height):
                self._white_spots.remove(spot)
                
        self._black_spots.append(Spot(circle_point, SPOT_RADIUS_FRAC))
        
    def replace_initial_black(self, ratio_height, ratio_width, circle_point):
        'Replaces an initial black piece with a white piece'
        for spot in self._starting_black:
            if spot == [ratio_height, ratio_width]:
                self._starting_black.remove(spot)
        self.replace_black(circle_point)
                
        self._starting_white.append([ratio_height, ratio_width])

    def replace_initial_white(self,ratio_height, ratio_width, circle_point):
        'Replaces an initial white piece with a black piece'
        for spot in self._starting_white:
            if spot == [ratio_height, ratio_width]:
                self._starting_white.remove(spot)
        self.replace_white(circle_point)
                
        self._starting_black.append([ratio_height, ratio_width])
        
    def switch_turns(self):
        'Switches the turn'
        if self._turn == 'W':
            self._turn = 'B'
        elif self._turn == 'B':
            self._turn = 'W'

    def game_over(self):
        'Checks if the game is over'
        return not self._logic.not_game_over()
    
    def determine_winner(self):
        'Determines the winner of the game'
        if self.game_over():
            self._game_ended = True
            self._winner = self._logic.determine_winner(self._mode)

            
            
    
        
        
