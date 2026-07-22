class TictacToeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Board:
    def __init__(self):

        self.board_array = [[' ' for _ in range(3) ]for _ in range(3)]
        self.turn = "X"

    def display(self):
        print('\nBoard State:')
        for r_idx, row in enumerate(self.board_array):
            print(' | '.join(row))
            if r_idx < 2:
                print('---------')
        print(f'Current Turn: {self.turn}\n')
    
    def make_move(self, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            raise TictacToeException(f'Invalid move: ({row}, {col}) is out of bounds (0-2).')

        if self.board_array[row][col] != " ":
            raise TictacToeException(f'Invalid move: Position ({row}, {col}) is already occupied.')
        

        self.board_array[row][col] = self.turn
        self.turn = 'O' if self.turn == 'X' else 'X'

if __name__ == '__main__':
    game_board = Board()
    game_board.display()

    try:
        game_board.make_move(1,1)
        game_board.display()

        game_board.make_move(0,0)
        game_board.display()

        print('Testing duplicate move exception handling:')
        game_board.make_move(1, 1)

    except TictacToeException as e:
        print(f'Caught expected TicTacToe Error: {e.message}')