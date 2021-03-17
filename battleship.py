#Nathan Li - Battleship Game - 2/2/2021

from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

print("Welcome to the Battleship Game! Let's get started with the ocean below. You have 5 guesses.")

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

for turn in range(5):
  print("Turn", turn + 1)
  guess_row = int(input("Guess a row: ")) - 1 #subtract one because rows actually start at zero, but those playing will start with one
  guess_col = int(input("Guess a col: ")) - 1 #subtract one because columns actually start at zero, but those playing will start with one

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > len(board[0])) or (guess_col < 0 or guess_col > len(board[0])):
      print("Oops, that's not in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print("You guessed that spot already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    
    print_board(board)
else:
  print("Game Over! You're out of turns.")