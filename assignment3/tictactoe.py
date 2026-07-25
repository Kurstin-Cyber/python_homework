

class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" ", " ", " "] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        
        self.board_array[row][column] = self.turn
        self.last_move = move_string
        
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            else:
                continue
            break
        if cat:
            return (True, "Cat's Game.")
        
        win = False
        for i in range(3): 
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): 
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True

        if not win:
            if self.turn == "X":
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
          
            winning_player = "O" if self.turn == "X" else "X"
            return (True, f"{winning_player} has won")


if __name__ == "__main__":
    game_board = Board()
    print("--- Welcome to Tic Tac Toe ---")
    print(game_board)

    while True:
        game_over, status_message = game_board.whats_next()
        if game_over:
            print(status_message)
            break

        move_input = input(f"{status_message} Enter your move: ").strip().lower()
        
        try:
            game_board.move(move_input)
            print("\nCurrent Board:")
            print(game_board)
        except TictactoeException as e:
            print(f"Error: {e.message}\n")