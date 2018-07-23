# Andy Le 92855131
#import othello_game

def make_input_list(n: int):
    'Makes a list of the four inputs that the user types in'

    input_list = []
    for line in range(rows):
        input_list.append(' . ' * cols)
        
    return input_list

##if __name__ == '__main__':
##    print('FULL')
##    rows, columns, turn, mode = tuple(make_input_list(4))
##    board = make_input_list(int(rows))
##    othello = othello_game.game_state()
##    othello.play_game(board, turn, mode)
    
    
    

