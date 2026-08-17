
import math

class AIPlayer:
    def __init__(self, symbol, opponent_symbol):
        self.symbol = symbol
        self.opponent_symbol = opponent_symbol

    def get_move(self, board):
        best_score = -math.inf
        best_move = None

        for move in board.available_moves():
            board.cells[move] = self.symbol
            score = self.minimax(board, False)
            board.cells[move] = " "
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, is_maximizing):
        if board.is_winner(self.symbol):
            return 1
        if board.is_winner(self.opponent_symbol):
            return -1
        if board.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in board.available_moves():
                board.cells[move] = self.symbol
                score = self.minimax(board, False)
                board.cells[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in board.available_moves():
                board.cells[move] = self.opponent_symbol
                score = self.minimax(board, True)
                board.cells[move] = " "
                best_score = min(score, best_score)
            return best_score