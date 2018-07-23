#ANDY LE 92855131

''' SORRY I COULD NOT GET THE WINNER TO DISPLAY
UNLESS U CLICK AFTER THE GAME IS OVER

Also sometimes the winner displays early before the game is over.
'''
import tkinter
import point
import project_5_model

scale = {4: 1, 6: 1, 8:1, 10: .75, 12: .60, 14: .55, 16:.50}
DEFAULT_FONT = ('Verdana', 14)
class Dialog:
    def __init__(self):
        
        
        self._root_window = tkinter.Tk()
        self._root_window.withdraw()
        
        self._dialog_window = tkinter.Toplevel()
        self._root = tkinter.Tk()
        self._root.withdraw()

        
        row_label = tkinter.Label(
            master = self._dialog_window, text = 'How many rows?',
            font = DEFAULT_FONT)

        row_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        col_label = tkinter.Label(
            master = self._dialog_window, text = 'How many columns?',
            font = DEFAULT_FONT)
        
        col_label.grid(
            row = 0, column = 1,  padx = 10, pady = 10,
            sticky = tkinter.W)        


        setting_label = tkinter.Label(
            master = self._dialog_window, text = 'Game Mode',
            font = DEFAULT_FONT)
        
        setting_label.grid(
            row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        turn_label = tkinter.Label(
            master = self._dialog_window, text = 'Starting Player',
            font = DEFAULT_FONT)
        
        turn_label.grid(
            row = 0, column = 3, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)
        self._dialog_window.columnconfigure(2, weight = 1)
        self._dialog_window.columnconfigure(3, weight = 1)

        


        self._Var1 = tkinter.IntVar()
        self._Var2 = tkinter.IntVar()
        self._Var3 = tkinter.StringVar()
        self._Var4 = tkinter.StringVar()
        # ROWS
        
        R1 = tkinter.Radiobutton(self._dialog_window, text = '4',variable = self._Var1, value = 4)
        R1.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        R2 = tkinter.Radiobutton(self._dialog_window, text = '6',variable = self._Var1, value = 6)
        R2.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        R3 = tkinter.Radiobutton(self._dialog_window, text = '8',variable = self._Var1, value = 8)
        R3.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        R4 = tkinter.Radiobutton(self._dialog_window, text = '10',variable = self._Var1, value = 10)
        R4.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        R5 = tkinter.Radiobutton(self._dialog_window, text = '12',variable = self._Var1, value = 12)
        R5.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        R6 = tkinter.Radiobutton(self._dialog_window, text = '14',variable = self._Var1, value = 14)
        R6.grid(
            row = 6, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        R7 = tkinter.Radiobutton(self._dialog_window, text = '16',variable = self._Var1, value = 16)
        R7.grid(
            row = 7, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        # COLUMNS
        C1 = tkinter.Radiobutton(self._dialog_window, text = '4',variable = self._Var2, value = 4)
        C1.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        C2 = tkinter.Radiobutton(self._dialog_window, text = '6',variable = self._Var2, value = 6)
        C2.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        C3 = tkinter.Radiobutton(self._dialog_window, text = '8',variable = self._Var2, value = 8)
        C3.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        C4 = tkinter.Radiobutton(self._dialog_window, text = '10',variable = self._Var2, value = 10)
        C4.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        C5 = tkinter.Radiobutton(self._dialog_window, text = '12',variable = self._Var2, value = 12)
        C5.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        C6 = tkinter.Radiobutton(self._dialog_window, text = '14',variable = self._Var2, value = 14)
        C6.grid(
            row = 6, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        C7 = tkinter.Radiobutton(self._dialog_window, text = '16',variable = self._Var2, value = 16)
        C7.grid(
            row = 7, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)


        # GAME SETTING
        S1 = tkinter.Radiobutton(self._dialog_window, text = '>',variable = self._Var3, value = '>')
        S1.grid(
            row = 1, column = 2, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        S2 = tkinter.Radiobutton(self._dialog_window, text = '<',variable = self._Var3, value = '<')
        S2.grid(
            row = 2, column = 2, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        # FIRST TURN
        T1 = tkinter.Radiobutton(self._dialog_window, text = 'W',variable = self._Var4, value = 'W')
        T1.grid(
            row = 1, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        T2 = tkinter.Radiobutton(self._dialog_window, text = 'B',variable = self._Var4, value = 'B')
        T2.grid(
            row = 2, column = 3, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        # BUTTON FRAME
        button_frame = tkinter.Frame(master = self._dialog_window)
        button_frame.grid(
            row = 8, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        # OKAY BUTTON
        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        # CANCEL BUTTON
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

        self._ok_clicked = False


        
    def _get_rows(self) -> int:
        'Returns the number of rows the user chooses'
        return self._Var1.get()
    
    def _get_columns(self) -> int:
        'Returns the number of columns the user chooses'
        return self._Var2.get()

    def _get_mode(self) -> int:
        'Returns the game mode the user chooses'
        return self._Var3.get()

    def _get_turn(self) -> int:
        'Return who the user chooses to go first'
        return self._Var4.get()

    

        
 
    def _on_ok_button(self) -> None:
        'If the okay button is clicked, destroy the dialog window'
        self._ok_clicked = True

        self._root_window.destroy()
   

    def _on_cancel_button(self) -> None:
        'If the cancel button is clicked, close the program'

        self._root_window.destroy()
    
        
    def show(self) -> None:
        'Turn control over to the dialog box and make it modal'

        self._dialog_window.grab_set()
        self._dialog_window.wait_window()






class Othello:
    def __init__(self, state: project_5_model.SpotsState):

        
        
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#006000')
        self._canvas.grid(row = 0, column = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        

        self._state = state
        self._turn = ''

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)



        # LABEL FRAME
        label_frame = tkinter.LabelFrame(master = self._root_window, text = "Score")
        label_frame.grid(
            row = 1, column = 0, columnspan = 8, padx = 5, pady = 5,
            sticky = tkinter.S)
        

        # WHITE
        self._white_score = tkinter.StringVar()
        self._white_score.set('WHITE:         ')
        
        self._black_score = tkinter.StringVar()
        self._black_score.set('BLACK:         ')
        
        white_label = tkinter.Label(master = label_frame,
                                    textvariable = self._white_score,
                                    font = DEFAULT_FONT)

        white_label.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10)
        
        # BLACK
        black_label = tkinter.Label(master = label_frame,
                                    textvariable = self._black_score,
                                    font = DEFAULT_FONT)

        black_label.grid(row = 1, column = 4, columnspan = 4, padx = 10, pady = 10)

        # TURN
        self._turn_text = tkinter.StringVar()
        self._turn_text.set('Turn:    ')
        
        turn_label = tkinter.Label(master = label_frame,
                                    textvariable = self._turn_text ,
                                   font = DEFAULT_FONT)

        turn_label.grid(row = 0, column = 2 , columnspan = 2, padx = 10, pady = 10)

        full_label = tkinter.Label(master = label_frame,
                                    text = "FULL", font = DEFAULT_FONT)

        full_label.grid(row = 0, column = 4 , columnspan = 2, padx = 10, pady = 10)


        
        self._button_frame = tkinter.LabelFrame(master = self._root_window)
        self._button_frame.grid(
            row = 0, column = 1, columnspan = 4, padx = 5, pady = 5,
            sticky = tkinter.E)


        place_white_button = tkinter.Button(master = self._button_frame,
                                            text = 'Place White Pieces',
                                            font = DEFAULT_FONT,
                                            command = self.white_pressed)
        place_white_button.grid(row = 1, column = 0, padx = 10, pady = 10)

        place_black_button = tkinter.Button(master = self._button_frame,
                                            text = 'Place Black Pieces',
                                            font = DEFAULT_FONT,
                                            command = self.black_pressed)
        place_black_button.grid(row = 2, column = 0, padx = 10, pady = 10)

        place_start_button = tkinter.Button(master = self._button_frame,
                                            text = 'Start Game',
                                            font = DEFAULT_FONT,
                                            command = self.start_game)
        place_start_button.grid(row = 3, column = 0, padx = 10, pady = 10)

        

        
    def white_pressed(self):
        'If white is pressed, set the turn to white and display it'
        self._state._turn = 'W'
        self._turn_text.set(f'Turn:   {self._state._turn}')
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        
    def black_pressed(self):
        'If white is pressed, set the turn to white and display it'
        self._state._turn = 'B'
        self._turn_text.set(f'Turn:   {self._state._turn}')
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        
    def start_game(self):
        'Starts the game ,destroys the button frame'
        self._button_frame.destroy()
        self._turn_text.set(f'Turn:   {self._state.display_opposite()}')
        self._state._turn = dialog._get_turn()
        self._state.start_game(dialog._get_columns(), dialog._get_rows())

        white_count = str(self._state._logic._white_counter)
        black_count = str(self._state._logic._black_counter)
        
        self._white_score.set(f'White:  {white_count}')
        self._black_score.set(f'Black:  {black_count}') 
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)
 

        
    def draw_board(self, row, col):
        'Draws the lines for the board'
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        n = 0
        m = 0
        for lat_line in range(col):
            self._canvas.create_line(((canvas_width / col) * n), 0,
                                     ((canvas_width / col) * n), canvas_height)
            n += 1
        for lng_line in range(row):
            self._canvas.create_line(0, ((canvas_height / row) * m),
                                     canvas_width, ((canvas_height / row) * m))

            m += 1        

    def _on_canvas_resized(self, event: tkinter.Event):
        'When the canvas is resized, redraw the game'
        self._redraw_all_spots_and_lines()


        
    def redraw_lines(self) -> None:
        'Redraws the lines'
        self.draw_board(dialog._get_rows(),dialog._get_columns())
        
    def run(self) -> None:
        'Runs the game'
        self.draw_board(dialog._get_rows(),dialog._get_columns())
   
    


    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        'When the canvas is clicked, handle the click'

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        row = dialog._get_rows()
        col = dialog._get_columns()
        mode = dialog._get_mode()

        click_point = point.from_pixel(
            event.x, event.y, width, height)
        

        self._state.handle_click(click_point, width, height, row, col,mode)


        white_count = str(self._state._logic._white_counter)
        black_count = str(self._state._logic._black_counter)
        self._turn_text.set(f'Turn:   {self._state._logic._turn}')
        self._state._logic.all_move_list()
        self._state._logic.viable_move_list()
          
        self._white_score.set(f'White:  {white_count}')
        self._black_score.set(f'Black:  {black_count}')       

        
        self._redraw_all_spots_and_lines()




    

    def _redraw_all_spots_and_lines(self) -> None:
        'Redraws all the spots and lines and scales the spots with rows/cols'

        self._canvas.delete(tkinter.ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for spot in self._state._white_spots:
            center_x, center_y = spot.center().pixel(canvas_width, canvas_height)

            radius_x = spot.radius_frac() * canvas_width * scale[dialog._get_columns()]
            radius_y = spot.radius_frac() * canvas_height * scale[dialog._get_rows()]
            
            self._canvas.create_oval(
                center_x - radius_x, center_y - radius_y,
                center_x + radius_x, center_y + radius_y,
                fill = '#ffffff', outline = '#ffffff')

        for spot in self._state._black_spots:
            center_x, center_y = spot.center().pixel(canvas_width, canvas_height)

            radius_x = spot.radius_frac() * canvas_width * scale[dialog._get_columns()]
            radius_y = spot.radius_frac() * canvas_height * scale[dialog._get_rows()]
            
            self._canvas.create_oval(
                center_x - radius_x, center_y - radius_y,
                center_x + radius_x, center_y + radius_y,
                fill = '#000000', outline = '#000000')       
        self.redraw_lines()

        if self._state._game_ended:
            self._turn_text.set(f'{self._state._winner}')
            
        

if __name__ == '__main__':
    dialog = Dialog()
    dialog.show()

    othello = Othello(project_5_model.SpotsState())
    othello.run()
 
    
