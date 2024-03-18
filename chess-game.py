!pip install chess
import chess
import chess.svg
import IPython
import sys

# Subroutines

"""
Evaluate the utility of each move
"""
def evaluate(board):

  #Assign values to each piece
  values = {
    chess.PAWN: 1,
    chess.ROOK: 5,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.QUEEN: 100,
    chess.KING: 999
  }

  white = 0
  black = 0

  # Calculate the total of all pieces on board
  for square in chess.SQUARES:
    piece = board.piece_at(square)

    if not piece:
      continue
    elif piece.color == chess.WHITE:
      white += values[piece.piece_type]
    else:
      black += values[piece.piece_type]

  return black - white

"""
Driver method for the minimax method
"""
def root(board, depth, maxPlayer):
  maxVal = -float('inf')
  bestMove = None
  value = 0
  # Check every move to find the max
  for move in board.legal_moves:
    board.push(move)
    value = max(maxVal, minimax(board, depth - 1, -10000, 10000, not maxPlayer))
    board.pop()
    if value > maxVal:
      maxVal = value
      bestMove = move

  return bestMove

"""
Minimax method to evaluate each move
"""
def minimax(board, depth, alpha, beta, maxPlayer):
  if depth == 0 or board.is_game_over():
    return evaluate(board)

  # Max
  if maxPlayer:
    value = -float("inf")
    for move in board.legal_moves:
      board.push(move)
      value = max(value, minimax(board, depth - 1, alpha, beta, False))
      board.pop()
      alpha = max(alpha, value)
      if beta <= alpha:
        break

    return value

  # Min
  else:
    value = float("inf")
    for move in board.legal_moves:
      board.push(move)
      value = min(value, minimax(board, depth - 1, alpha, beta, True))
      board.pop()
      beta = max(beta, value)
      if beta <= alpha:
        break

    return value

board = chess.Board()
gameOver = False

print("Welcome to chess!")
svg = chess.svg.board(board, size=350)
display(IPython.display.HTML(svg))

"""
Main loop
"""
while board.king(chess.WHITE):
  move = input("Please move your first piece: ")
  move = chess.Move.from_uci(str(move))
  board.push(move)
  svg = chess.svg.board(board, size=350)
  display(IPython.display.HTML(svg))

  print("Computer's turn: ")
  board.push(root(board, 3, True))
  svg = chess.svg.board(board, size=350)
  display(IPython.display.HTML(svg))
