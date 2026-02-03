
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move in board.available_moves():
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
