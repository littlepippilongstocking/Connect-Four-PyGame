"""
Dilyana Koleva, August 2022
Connect Four game on PyGame
Command Line Edition (No Graphics)
"""
import numpy

rows = 6
cols = 7


def create_board():
    board = numpy.zeros((rows, cols))
    return board


# Places the element on the board
def place(board, row, col, piece):
    board[row][col] = piece


# Checks if the location is available
def is_valid(board, col):
    return board[rows - 1][col] == 0


# Gets the next row while the element is dropping
def get_next_row(board, col):
    for r in range(rows):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(numpy.flip(board, 0))


def winning(board, piece):
    # Check horizontal locations
    for c in range(cols - 3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical Locations
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check for diagonals
    for c in range(cols - 3):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece:
                return True

    for c in range(cols - 3):
        for r in range(3, rows):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True


board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, make your choice (0-6): "))

        if is_valid(board, col):
            row = get_next_row(board, col)
            place(board, row, col, 1)
            if winning(board, 1):
                print("Congratulations, Player 1. You won!")
                game_over = True


    # Ask for player 2 input
    else:
        col = int(input("Player 2, make your choice (0-6): "))

        if is_valid(board, col):
            row = get_next_row(board, col)
            place(board, row, col, 2)
            if winning(board, 1):
                print("Congratulations, Player 1. You won!")
                game_over = True

    print_board(board)

    turn += 1
    turn = turn % 2
