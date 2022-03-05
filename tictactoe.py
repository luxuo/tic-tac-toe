EMPTY = ' '
X = 'X'
O = 'O'
PLAYERS = (X, O)


# getEmptyBoard()
# returns -> str[9]
# Returns an empty tic tac toe board
def getEmptyBoard():
 return EMPTY * 9

# validGame(str[9], (char, char))
# returns -> bool
# Returns wheter the game of tic tac toe
#  follows the correct playing order
# PLAYING ORDER : players[0] always
#  begins the game, then the plays
#  alternate between players[0] and
#  players[1]
def validGame(piece, players):
 diff = piece.count(players[0]) - piece.count(players[1])
 return diff == 0 or diff == 1

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
 

# playOnPiece(str[9], char, int)
# returns -> str[9]
# Returns a new piece with the next play
def playOnPiece(piece, player, at):
 return piece[:at] + player + piece[at + 1:]


# countPossibleWins(str[9], int, (char, char), set{str[9]}, int = -1)
# returns -> int
# Returns the number of possible unique wins that can happen
#  with the current board, assuming the wins are for the next
#  playing player
# Assumes that players[0] is the first player to have played
#  or will play
def countPossibleWins(piece, player, players, setBoards = set({}), i = -1):
 count = 0 # win counter
 if i == -1: # set i
  i = 9 - piece.count(EMPTY)
 for play in range(0, 9-i): # for all possible plays
  char = players[i % 2] # who plays

  split = permutation(play,piece)
  newPiece = playOnPiece(piece, char, split) # set new board

  if newPiece not in setBoards:
   setBoards.add(newPiece) # Add in the set
   if win(players[player], newPiece): # if the player wins
    count += 1
   elif not win(players[player],newPiece): # if the player hasn't lost
    count += countPossibleWins(newPiece, player, players, setBoards, i + 1)
 
 return count


# getWinCounts(str[9], (char, char))
# returns -> int[9]
# Returns an array of all possible win counts
#  for the next playing player
def getWinCounts(piece, players):
 winCounts = [-1] * 9

 availablePlays = piece.count(EMPTY) # how many possible plays
 if availablePlays == 0: # if the game is over
  return winCounts
 
 player = (availablePlays - 1) % 2 # determine the 
 for play in range(availablePlays): # for all available plays
  index = permutation(play,piece)
  # get the play
  newPiece = playOnPiece(piece, players[player], index)
  # get all possible wins from said play
  wins = countPossibleWins(newPiece, player, players, set({}))
  winCounts[index] = wins
 
 return winCounts

# cpuMove(str[9], int, (char, char), int)
# returns -> str[9]
# Returns a piece with a cpu making the
#  next move
def cpuMove(piece, players, level):
 pass # TODO