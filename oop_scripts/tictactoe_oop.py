ALL_SPACES = list('123456789') # The keys for the TTT board
X, O, BLANK = 'X','O', ' ' # Constants for string values

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = TTTBoard() # Create a board object
    currentPlayer, nextPlayer = X, O # X goes first, then O
    
    while True:
        print(gameBoard.getBoardStr()) # Display the board on the screen
        
        # Keep asking the player until they enter a number 1-9
        move = None
        
    while not gameBoard.isValidSpace(move):
        print(f'What is {currentPlayer}\'s move? (1-9)')
        move = input()
    gameBoard.updateBoard(move, currentPlayer) # Make a move
    
    # Check if the game is over 
    if gameBoard.isWinner(currentPlayer): # First check for victory
        print(gameBoard.getBoardStr()) # Display the board on the screen
        print(currentPlayer + ' has won the game!')
        break
    elif gameBoard.isBoardFull(): # Next check for tie
        print(gameBoard.getBoardStr())
        print('The game is a tie!')
        break
    currentPlayer, nextPlayer = nextPlayer, currentPlayer # Swap turns
print('Thanks for playing!')

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic tac toe board."""
        self._spaces= {} # the board is represented as a Python Dictionary
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # All spaces are blank
    
    def getBoardStr(self):
        """Return a text-representation of the board"""
        return f'''
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9'''
        
    def isValidSpace(self, space):
        """Returns True if the space is a valid space number and the space is blank"""
        return space in ALL_SPACES and self._spaces[space] == BLANK
    
    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard"""
        s, p = self._spaces, player # Shorter names for simplicity
        # Check for 3 marks across the board
        return ((s['1'] == s['2'] == s['3'] == p) or # Across the top
                (s['4'] == s['5'] == s['6'] == p) or # Across the middle
                (s['7'] == s['8'] == s['9'] == p) or # Across the bottom
                (s['1'] == s['4'] == s['7'] == p) or # Down the left
                (s['2'] == s['5'] == s['8'] == p) or # Down the middle
                (s['3'] == s['6'] == s['9'] == p) or # Down the right
                (s['3'] == s['5'] == s['7'] == p) or # Diagonal
                (s['1'] == s['5'] == s['9'] == p)) # Diagonal
        
    def isBoardFull(self):
        """Return Trueif every space in the board are full"""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # if a single space is blank then return False
        return True  # No spaces are blank
    
    def updateBoard(self, space, player):
        """Sets the space on the board to player's current position"""
        self._spaces[space] = player
        
if __name__ == '__main__':
    main() # Call main()