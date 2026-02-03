
from board import Board
from player import Player
from ai import AIPlayer

def play_game():
    board = Board()
    human = Player("X")
    ai = AIPlayer("O", "X")

    print("Welcome to Tic-Tac-Toe!")
    print("You are X. AI is O.")
    board.display()

    while True:
        # Human move
        move = human.get_move(board)
        board.make_move(move, human.symbol)
        board.display()

        if board.is_winner(human.symbol):
            print("You win!")
            break
        if board.is_full():
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = ai.get_move(board)
        board.make_move(ai_move, ai.symbol)
        board.display()

        if board.is_winner(ai.symbol):
            print("AI wins!")
            break
        if board.is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()