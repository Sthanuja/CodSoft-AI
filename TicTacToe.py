import tkinter as tk
import tkinter.messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]  # Representing the Tic-Tac-Toe board
        self.buttons = [tk.Button(self.window, text=" ", font=('normal', 20), width=5, height=2,
                                  command=lambda i=i: self.click(i)) for i in range(9)]

        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[i].grid(row=row, column=col)

        self.reset_button = tk.Button(self.window, text="Play Again", font=('normal', 14),
                                      command=self.reset_game)
        self.reset_button.grid(row=3, column=1, columnspan=3)

        self.current_player = "X"
        self.game_over = False

    def click(self, index):
        if not self.game_over and self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.game_over = True
                tkinter.messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif " " not in self.board:
                self.game_over = True
                tkinter.messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        if empty_cells:
            index = self.minimax(self.board, "O")['index']
            self.click(index)

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ")
        self.current_player = "X"
        self.game_over = False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
            if self.board[3 * i] == self.board[3 * i + 1] == self.board[3 * i + 2] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def minimax(self, board, player):
        empty_cells = [i for i in range(9) if board[i] == " "]

        if self.check_winner():
            if player == "O":
                return {'score': -1}
            else:
                return {'score': 1}
        elif not empty_cells:
            return {'score': 0}

        moves = []
        for cell in empty_cells:
            move = {}
            move['index'] = cell
            board[cell] = player

            if player == "O":
                result = self.minimax(board, "X")
                move['score'] = result['score']
            else:
                result = self.minimax(board, "O")
                move['score'] = result['score']

            board[cell] = " "
            moves.append(move)

        if player == "O":
            best_move = max(moves, key=lambda x: x['score'])
        else:
            best_move = min(moves, key=lambda x: x['score'])

        return best_move

    def run(self):
        self.window.mainloop()

# Create and run the TicTacToe game
game = TicTacToe()
game.run()
