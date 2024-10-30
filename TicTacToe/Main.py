from tictactoe_model import TicTacToeModel
from tictactoe_view import TicTacToeView
from tictactoe_controller import TicTacToeController

if __name__ == "__main__":
    model = TicTacToeModel()
    view = TicTacToeView("Tic-Tac-Toe")
    controller = TicTacToeController(model, view)
    controller.play_game()
