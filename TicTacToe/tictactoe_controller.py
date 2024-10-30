class TicTacToeController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_player = self.model.get_turn()
        self.view.add_action_listener(self)

    def play_game(self):
        self.view.display()

    def handle_click(self, r, c):
        try:
            self.model.move(r, c)
            self.view.display_move(r, c, self.current_player)
            self.current_player = self.model.get_turn()
            self.view.update_turn_label(self.current_player)

            winner = self.model.check_winner()
            if winner:
                self.view.display_message("Game is over! " + str(winner) + " wins.")
            elif self.model.is_full():
                self.view.display_message("Game is over! Tie game.")
            else:
                self.view.display_message("")
        except Exception as e:
            self.view.display_message(str(e))
