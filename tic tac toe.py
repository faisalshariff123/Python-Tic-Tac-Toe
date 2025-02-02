import tkinter as tk
def on_click(row, column):
    global current_player
    global game_over
    
    if (game_over):
        return
    
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = current_player
    
    if current_player == player_x:
        current_player = player_o
    elif current_player == player_o:
        current_player = player_x
        
    label["text"] = current_player+"'s turn"
    
    check_winner()

def check_winner():
    global current_player
    global turns
    global game_over
    turns += 1
    #horizontal check
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground = color_green, background = color_yellow )
            game_over = True
            return
    #vertical check
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground = color_green, background = color_yellow )
            game_over = True
            return
        
    #diagonal
        if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
            label.config(text=board[0][0]["text"]+" is the winner!", foreground = color_green, background = color_yellow )
            game_over = True
            return
        
    #anti-diagonal
        if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
            label.config(text=board[0][2]["text"]+" is the winner!", foreground = color_green, background = color_yellow )
            game_over = True
            return
            
    #draw
        if turns == 9:
            game_over = True
            label.config(text="It's a Draw!", foreground = color_blue, background = color_white)


    
def restart():
    global current_player
    global game_over
    global turns
    current_player = player_x
    game_over = False
    turns = 0
    label["text"] = current_player + "'s turn"
    for row in range(3):
        for column in range(3):
            board[row][column]["text"] = ""
#game setup
player_x = "X"
player_o = "O"
current_player = player_x
board = [[0,0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]
#variables setup
color_blue = "sky blue"
color_red = "tomato"
color_white = "white"
color_black = "black"
color_green = "green"
color_yellow = "yellow"
turns = 0
game_over = False
#app window setup
app = tk.Tk()
app.title("Tic Tac Toe")
app.geometry("300x300")
app.resizable(False, False)
#frame setup
frame = tk.Frame(app, width=300, height=300)
label = tk.Label(frame, text=current_player + "'s turn.", font=("Arial", 20), background=color_black, 
                 foreground=color_white)
#game logic
for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button( frame, text="", font=("Arial", 20), width=3, height=1, background=color_white, foreground=color_black, command=lambda row=row, column=column: on_click(row, column))
        board[row][column].grid(row=row+1, column=column)
        
button = tk.Button(frame, text="Restart Game", font=("Arial", 20), width=3, height=1, background=color_white, foreground=color_black, command=restart)
button.grid(row=4, column=0, columnspan=3, sticky="we")

label.grid(row=0, column=0, columnspan=3, sticky="we")




frame.pack()
app.mainloop()



