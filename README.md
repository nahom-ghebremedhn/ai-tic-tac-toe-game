# AI Tic-Tac-Toe
A command-line implementation of Tic-Tac-Toe built in Python. The application uses object-oriented programming principles and features an unbeatable AI opponent driven by the Minimax algorithm.
## Features
* **Unbeatable AI:** Evaluates all possible future board states using recursive search to guarantee either a win or a draw.
* **Modular Code Structure:** Clean separation of concerns between game logic, board state management, human input handling, and AI logic.
* **Input Validation:** Handles out-of-bounds numbers, invalid inputs, and occupied cell attempts gracefully.
## Project Structure

```text
ai-tic-tac-toe-game/
└──⁠ src/
    ├── ai.py         # AI decision-making (Minimaxalgorithm)
    ├── board.py      # Board representation, state tracking, and win checking
    ├── game.py       # Main entry point and game loopcontrol
   ├── player.py      #Human player input handling and validation
└──⁠  README.md
```
## How the AI Works
The AI relies on the Minimax algorithm to simulate all possible moves recursively down to terminal states (win, loss, or draw).
1  **Maximizing Player (AI):

⁠

⁠

⁠



