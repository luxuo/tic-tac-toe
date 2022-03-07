import tictactoe as ttt

piece = ttt.getEmptyBoard() # initialise ttt board

# printBoard(str[9])
# Prints the tic tac toe game
def printBoard(piece):
 for i in range(0,9,3):
  print(' '.join(piece[i: i +3]))

# gameOver(str[9], (char, char))
# returns -> int
# returns which player has won, tie, or 
#  if the game hasn't ended yet
def gameOver(piece, players):
 if ttt.win(players[0], piece):
  return 0 
 elif ttt.win(players[1], piece):
  return 1 
 elif piece.count(ttt.EMPTY) == 0:
  return -1 # tie
 return 2 # game isn't over

# move(str[9], int, char)
# returns -> str[9]
# Returns the play on the piece
def move(piece, player, i):
 if piece[i] == ttt.EMPTY:
  return ttt.playOnPiece(piece,player, i)
 return piece


# Game logic begins
gameState = 2
player = False
while gameState == 2:
 oldPiece = piece
 piece = move(piece, ttt.PLAYERS[player], int(input()))
 # should be cpu
 piece = ttt.cpuMove(piece,ttt.PLAYERS,1)
 printBoard(piece)
 gameState = gameOver(piece, ttt.PLAYERS)

print('Player', gameState, 'has won')