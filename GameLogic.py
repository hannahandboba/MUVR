# Check if a player has won
def check_win(player):
  # Check horizontal lines
  for row in board:
    if row.count(player) == 3:
      return True

  # Check vertical lines
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True

  # Check diagonal lines
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True

  return False

# Place a game piece on the board
def place_piece(player, row, col):
  if board[row][col] == "-":
    board[row][col] = player
    piece = None
    if player == "X":
      piece = x_piece
    else:
      piece = o_piece
    piece_position = UnityEngine.Vector3(col, 0.5, row)
    piece.transform.position = piece_position
    return True
  else:
    return False

# Check if the game is over
def check_game_over():
  if check_win("X"):
    return "X"
  elif check_win("O"):
    return "O"
  elif "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
    return "Tie"
  else:
    return None
