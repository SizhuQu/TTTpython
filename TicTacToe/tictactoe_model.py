class Player:
    X = "X"
    O = "O"


class TicTacToeModel:

    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = Player.X

    def move(self, r, c):
        if self.is_game_over():
            # raise an exception if the game is over
            raise Exception("Game is over!")
            # raise an exception if the position is occupied
        if self.board[r][c] is not None:
            raise Exception("Position occupied")
        
        self.board[r][c] = self.turn
        self.turn = Player.O if self.turn == Player.X else Player.X

    def get_turn(self):
        return self.turn

    def is_game_over(self):
        return self.is_full() or self.check_winner() is not None

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        
        return None

    def is_full(self):
        return all(cell is not None for row in self.board for cell in row)
