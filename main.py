import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9

        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text="", font=('normal', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tie", "The game is a tie!")
                self.reset_board()
            else:
                self.switch_player()

    def update_button(self, row, col):
        index = row * 3 + col
        button = self.master.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state="disabled")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            # Check rows
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return True
            # Check columns
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                button = self.master.grid_slaves(row=i, column=j)[0]
                button.config(text="", state="normal")
        self.current_player = "X"
        self.board = [""] * 9


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
