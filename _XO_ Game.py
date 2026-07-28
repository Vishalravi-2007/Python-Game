import tkinter as tk
win = tk.Tk()
win.title("XOX Game")
player = "X"
board = [""] * 9
btns = []
def clicked(i):
    global player
    if board[i] != "":
        return
    board[i] = player
    btns[i].config(text=player)

    if check(player):
        win.title(f"Player {player} Wins!")
        disable()
    elif "" not in board:
        win.title("Draw!")
    else:
        player = "O" if player == "X" else "X"
def check(p):
    combos = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in combos)
def disable():
    for b in btns:
        b.config(state="disabled")
for i in range(9):
    b = tk.Button(win, text="", font=("Arial", 30), width=3, height=1,
                  command=lambda i=i: clicked(i))
    b.grid(row=i//3, column=i%3)
    btns.append(b)
win.mainloop()
