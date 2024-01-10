from tkinter import *
from tkinter import messagebox


tk = Tk()

tk.title("Tic Tac Toe")
tk.resizable(0,0)

def create_board():
    for i in range(3):
        for j in range(3):
            button = Button(height=4, width=8, font=("Helvetica", "20"), command = lambda row = i, col = j : on_click(row,col))
            button.grid(row = i, column = j)
create_board() 
        
board = [[0,0,0], [0,0,0], [0,0,0]]
Player = 1


def on_click(row, col):
    global Player
    
    if board[row][col] == 0:
        if Player == 1:
            board[row][col] = "X"
            Player = 2
        else:
            board[row][col] = "O"
            Player = 1
            
        button = tk.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])
        
        win_or_tie()


def win_or_tie():
    winner = None
    
    #Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            break
    #Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board != 0:
            winner = board[0][col]
            print(board[0][col])
            
            break
    #Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]
        
    if all([all(row) for row in board]) and winner is None:
        winner = "tie"
    
    if winner:
        declare_winner(winner)
        
def declare_winner(winner):
    if winner == "tie":
        message = "It's a tie!"
    else: 
        message = f"Player {winner} wins"
        
    answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")

    if answer:
        global board
        board = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                button = tk.grid_slaves(row=i, column=j)[0]
                button.config(text="")
            
        global Player
        Player = 1 
    else:
        tk.quit()   

tk.mainloop()