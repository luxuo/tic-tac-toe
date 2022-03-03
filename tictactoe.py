EMPTY = ' '
X = 'X'
O = 'O'
PLAYERS = (X, O)

# getEmptyBoard()
# returns -> str[9]
# Returns an empty tic tac toe board
def getEmptyBoard():
 return EMPTY * 9

# win(char, str[9])
# returns -> bool
# Returns whether the player has won
# the tic tac toe game
def win(player, piece):
 straight = player * 3
 for i in range(0,9,3): # Horizontal win
  if piece[i:i+3] == straight:
   return True
 for i in range(3): # Vertical win
  if piece[i::3] == straight:
     return True
 if piece[::4] == straight: # Left Diagonal
  return True
 if piece[2:8:2] == straight: # Right Diagonal
  return True
 return False # No win

# permutation(int, str[9])
# returns -> int
# Returns the index of the next
#  possible move on the board
def permutation(index, piece): # TODO RENAME
 offset = 0
 i = -1
 for char in piece:
   i += 1
   offset += 1 * (char != EMPTY) # adds if there is an X or O
   if i - offset == index: # if move is possible
    return i    
 return -1 # move not possible
 
# countPossibleWins(str[9], (char, char), set{str[9]}, int = -1)
# returns -> int
# Returns the number of possible unique wins that can happen
#  with the current board
# Assumes that players[0] is the first player to have played
#  or will play
def countPossibleWins(piece, players, setBoards = set({}), i = -1):
 count = 0 # win counter
 if i == -1: # set i
  i = 9 - piece.count(EMPTY)
 for play in range(0, 9-i): # for all possible plays
  char = players[i % 2] # who plays

  split = permutation(play,piece)
  newPiece = piece[:split] + char + piece[split+1:] # set new board

  if newPiece not in setBoards:
   setBoards.add(newPiece) # Add in the set
   if win(players[0], newPiece): # if player[0] wins
    count += 1
   elif not win(players[1],newPiece): # if player[0] hasn't lost
    count += countPossibleWins(newPiece, players, setBoards, i + 1)
 
 return count

 # getWinCounts(str[9], (char, char))
 # 