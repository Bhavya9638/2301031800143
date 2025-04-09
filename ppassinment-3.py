import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            highlight_winner(row)
            return True
    
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            highlight_winner([board[i][col] for i in range(3)])
            return True
    
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        highlight_winner([board[i][i] for i in range(3)])
        return True
    
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        highlight_winner([board[i][2-i] for i in range(3)])
        return True
    
    if all(board[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        reset_board()
        return True 
    
    
    return False

def highlight_winner(cells):
    for cell in cells:
        cell.config(bg="lightgreen")
    messagebox.showinfo("Tic-Tac-Toe", f"Player {cells[0]['text']} wins!")
    reset_board()

def on_click(row, col):
    global turn
    if board[row][col]["text"] == "" and not check_winner():
        board[row][col]["text"] = turn
        if not check_winner():
            turn = "O" if turn == "X" else "X"

def reset_board():
    global turn
    turn = "X"
    for i in range(3):
        for j in range(3):
            board[i][j]["text"] = ""
            board[i][j].config(bg="white")

root = tk.Tk()
root.title("Tic-Tac-Toe")
board = [[None]*3 for _ in range(3)]
turn = "X"

for i in range(3):
    for j in range(3):
        board[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda r=i, c=j: on_click(r, c))
        board[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reset", font=("Arial", 16), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
