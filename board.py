
class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]

    def display(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def make_move(self, position, symbol):
        if self.cells[position] == " ":
            self.cells[position] = symbol
            return True
        return False

    def available_moves(self):
        return [i for i, cell in enumerate(self.cells) if cell == " "]

    def is_winner(self, symbol):
        win_patterns = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        return any(
            self.cells[a] == self.cells[b] == self.cells[c] == symbol
            for a, b, c in win_patterns
        )

    def is_full(self):
        return " " not in self.cells