"""
Tic-Tac-Toe Game with Minimax AI
"""

import math
import sys

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        """Display the current board state"""
        print('\n')
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
    
    def print_board_nums(self):
        """Show position numbers for user reference"""
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        print('\n')
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        print('\n')
    
    def available_moves(self):
        """Return list of available positions"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        """Check if there are empty squares"""
        return ' ' in self.board
    
    def num_empty_squares(self):
        """Count empty squares"""
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        """Make a move if valid"""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        """Check if the last move was a winning move"""
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False


def minimax(state, player, game):
    """
    Minimax algorithm with recursion
    Returns the best score for the given player
    """
    max_player = player  # AI player
    other_player = 'O' if player == 'X' else 'X'
    
    # Base cases
    if game.current_winner == other_player:
        return {'position': None, 'score': 1 * (game.num_empty_squares() + 1) if other_player == max_player else -1 * (game.num_empty_squares() + 1)}
    elif not game.empty_squares():
        return {'position': None, 'score': 0}
    
    if player == max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}
    
    for possible_move in game.available_moves():
        # Make a move
        game.make_move(possible_move, player)
        
        # Recurse using minimax to simulate game after making that move
        sim_score = minimax(state, other_player, game)
        
        # Undo the move
        game.board[possible_move] = ' '
        game.current_winner = None
        sim_score['position'] = possible_move
        
        # Update best move
        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    
    return best


def play_game():
    """Main game loops....."""
    game = TicTacToe()
    
    print("=" * 40)
    print("   Welcome to Tic-Tac-Toe!")
    print("=" * 40)
    print("\nYou are 'O' and the AI is 'X'")
    print("\nBoard positions:")
    game.print_board_nums()
    
    # Choose who goes first
    while True:
        first = input("Do you want to go first? (y/n): ").lower()
        if first in ['y', 'n']:
            break
        print("Please enter 'y' or 'n'")
    
    human = 'O'
    ai = 'X'
    current_player = human if first == 'y' else ai
    
    # Game loop
    while game.empty_squares():
        if current_player == human:
            game.print_board()
            valid_square = False
            while not valid_square:
                try:
                    square = int(input(f"Your turn (0-8): "))
                    if square not in range(9):
                        print("Invalid position! Choose 0-8")
                        continue
                    if square not in game.available_moves():
                        print("Square already taken! Choose another")
                        continue
                    valid_square = True
                except ValueError:
                    print("Invalid input! Enter a number 0-8")
            
            game.make_move(square, human)
            
            if game.current_winner:
                game.print_board()
                print("🎉 Congratulations! You won! 🎉")
                return
            
            current_player = ai
        
        else:
            print("\nAI is thinking...")
            square = minimax(game.board, ai, game)['position']
            game.make_move(square, ai)
            print(f"AI chose position {square}")
            
            if game.current_winner:
                game.print_board()
                print("🤖 AI wins! Better luck next time!")
                return
            
            current_player = human
    
    # If we get here, it's a tie
    game.print_board()
    print("🤝 It's a tie!")


def main():
    """Main program entry point"""
    while True:
        play_game()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()