import random
import random

# set up the game board
board_size = 5
board = []
for i in range(board_size):
    row = ["O"] * board_size
    board.append(row)

# place the treasure on the board
treasure_row = random.randint(0, board_size-1)
treasure_col = random.randint(0, board_size-1)
board[treasure_row][treasure_col] = "X"

# set up the player's starting position
player_row = random.randint(0, board_size-1)
player_col = random.randint(0, board_size-1)

# play the game
while True:
    # show the game board
    for row in board:
        print(" ".join(row))

    # ask the player to move
    move = input("Enter a direction to move (up, down, left, right): ")

    # update the player's position
    if move == "up":
        player_row -= 1
    elif move == "down":
        player_row += 1
    elif move == "left":
        player_col -= 1
    elif move == "right":
        player_col += 1

    # check if the player has found the treasure
    if board[player_row][player_col] == "X":
        print("You found the treasure! Game over.")
        break

    # check if the player is out of bounds
    if player_row < 0 or player_row >= board_size or \
       player_col < 0 or player_col >= board_size:
        print("You fell off the map! Game over.")
        break

    # update the game board with the player's new position
    board[player_row][player_col] = "P"
