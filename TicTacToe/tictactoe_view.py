import tkinter as tk


class TicTacToeView:

    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.turn_label = tk.Label(self.root, text="Turn: X", font=("Arial", 18))
        self.turn_label.pack()
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()
        self.message_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.message_label.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                button = tk.Button(self.grid_frame, text="", width=10, height=3, font=("Arial", 24))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def add_action_listener(self, controller):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(command=lambda r=r, c=c: controller.handle_click(r, c))

    def display_move(self, r, c, player):
        self.buttons[r][c].config(text=player, state="disabled")

    def update_turn_label(self, turn):
        self.turn_label.config(text="Turn: {}".format(turn))

    def display_message(self, message):
        self.message_label.config(text=message)

    def display(self):
        self.root.mainloop()
