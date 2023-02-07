""" Tic-Tac-Toe
class board: init for board, create rows and print board, check for victory, check for draw
class player: init for player, player move
initialize 1 board obj, and 2 players(x and o).
start game: while true: print board, player move, check for victory and draw - for 2 players. """

class Board:

    def __init__(self):
        """Initialize a board"""
        self.board = ["-" for x in range(9)]

    def print_board(self):
        """create rows and print board"""
        row1 = "|{}|{}|{}|".format(self.board[0], self.board[1], self.board[2])
        row2 = "|{}|{}|{}|".format(self.board[3], self.board[4], self.board[5])
        row3 = "|{}|{}|{}|".format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def is_victory(self, player):
        """Return true if a player has won"""
        if (self.board[0] == player and self.board[1] == player and self.board[2] == player) or \
        (self.board[3] == player and self.board[4] == player and self.board[5] == player) or \
        (self.board[6] == player and self.board[7] == player and self.board[8] == player) or \
        (self.board[0] == player and self.board[3] == player and self.board[6] == player) or \
        (self.board[1] == player and self.board[4] == player and self.board[7] == player) or \
        (self.board[2] == player and self.board[5] == player and self.board[8] == player) or \
        (self.board[0] == player and self.board[4] == player and self.board[8] == player) or \
        (self.board[2] == player and self.board[4] == player and self.board[6] == player):
            return True
        else:
            return False
        
    def is_draw(self):
        """Return true if there's a tie"""
        if not "-" in self.board:  #if we don't have whitespace, is a draw
            return True
        else:
            return False


class Player:
    def __init__(self, player):
        """Initialize a player"""
        self.player = player

    def player_move(self, board):
        """Assign players,ask for a move from each player and display it on the board"""
        # assign X to num 1, and O to num 2
        if self.player == "X":
            number = 1
        elif self.player == "O":
            number = 2
        
        print(f"It's your turn, player {number}") #print who's turn to play
        move = int(input("Please choose a number between 1-9: ")) #ask player to choose a num

        if board[move-1] == "-": #check if the spot available. (-1 cause of the idx)
            board[move-1] = self.player #assign player to this spot. 
        else:
            print("This space is taken.")
            self.player_move(board) #ask again for a space


#initialize a board and 2 players(x and o)
board = Board()
player1 = Player("X")
player2 = Player("O")


while True:
    #player1
    board.print_board() 
    player1.player_move(board.board) #player1 plays
    if board.is_victory(player1.player): #if player has won break the game
        print(f"{player1.player} is the winner!")
        break
    elif board.is_draw(): #elif draw, break the game
        print("It's a draw!")
        break
    #same for player2
    board.print_board() 
    player2.player_move(board.board)
    if board.is_victory(player2.player):
        print(f"{player2.player} is the winner!")
        break
    elif board.is_draw():
        print("It's a draw!")  
        break 





