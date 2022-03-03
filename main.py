import tictactoe as ttt

piece = ttt.getEmptyBoard()

def printBoard(piece):
 for i in range(0,9,3):
  print(' '.join(piece[i: i +3]))

def gameOver(piece, players):
 if ttt.win(players[0], piece):
  return 0
 elif ttt.win(players[1], piece):
  return 1 
 elif piece.count(ttt.EMPTY) == 0:
  return -1
 return 2

def move(piece, i, player):
 if piece[i] == ttt.EMPTY:
  return piece[:i] + player + piece[i+1:]
 return piece

gameState = 2
player = False
while gameState == 2:
 oldPiece = piece
 piece = move(piece, int(input()), ttt.PLAYERS[player])
 player = not player if oldPiece != piece else player
 printBoard(piece)
 gameState = gameOver(piece, ttt.PLAYERS)

print(gameState)