ALL_SPACES = list('123456789') # The keys for the TTT board
X, O, BLANK = 'X','O', ' ' # Constants for string values

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic-Tac-Toe!')
    gameboard = TTTBoard() # Create a board object
    currentPlayer, nextPlayer = X, O # X goes first, then O
    
    while True:
        print(gameBoard.getBoardStr()) # Display the board on the screen
        
        # Keep asking the player until they enter a number 1-9
        move = None
        
    while not gameBoard.isValidSpace(move):
        print(f'What is {currentPlayer}\'s move? (1-9)')
        move = input()
    gameBoard.updateBoard(move, currentPlayer) # Make a move