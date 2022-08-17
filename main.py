"""
Dilyana Koleva, August 2022
Connect Four Game on PyGame
"""

import numpy
import math
import pygame
import sys

BLUE_COLOUR = (0, 0, 255)
BLACK_COLOUR = (0, 0, 0)
RED_COLOUR = (255, 0, 0)
YELLOW_COLOUR = (255, 255, 0)

rows = 6
cols = 7


# Creates the command line board and fills it with zeros
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


# Prints the board from downwards
def print_board(board):
    print(numpy.flip(board, 0))


# Checks if the player is winning
def winning(board, piece):
    # Check horizontal locations
    for c in range(cols - 3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical Locations
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
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


# Draws the board with all elements and ensure that when an element is dropped the color of the circle changes
def draw_board(board):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.rect(window, BLUE_COLOUR,
                             (c * square_size, r * square_size + square_size, square_size, square_size))
            pygame.draw.circle(window, BLACK_COLOUR, (
                int(c * square_size + square_size / 2), int(r * square_size + square_size + square_size / 2)), radius)

    for c in range(cols):
        for r in range(rows):
            if board[r][c] == 1:
                pygame.draw.circle(window, RED_COLOUR, (
                    int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(window, YELLOW_COLOUR, (
                    int(c * square_size + square_size / 2), height - int(r * square_size + square_size / 2)),
                                   radius)
    pygame.display.update()


board = create_board()
game_over = False
turn = 0

# Initialises the game and adjusts the size of the window
pygame.init()

# Adjust the size to your screen
square_size = 80

width = cols * square_size
# Adds a supplementary row for moving the element
height = (rows + 1) * square_size
size = (width, height)
radius = int(square_size / 2 - 5)

window = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

font = pygame.font.SysFont("monospace", 50)

while not game_over:
    for event in pygame.event.get():
        # Ensures the game exits once the X is clicked
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(window, BLACK_COLOUR, (0, 0, width, square_size))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(window, RED_COLOUR, (pos_x, int(square_size / 2)), radius)
            else:
                pygame.draw.circle(window, YELLOW_COLOUR, (pos_x, int(square_size / 2)), radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(window, BLACK_COLOUR, (0, 0, width, square_size))

            # Player 1 Input
            if turn == 0:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / square_size))

                if is_valid(board, col):
                    row = get_next_row(board, col)
                    place(board, row, col, 1)
                    if winning(board, 1):
                        label = font.render("Player 1 wins!", 1, RED_COLOUR)
                        window.blit(label, (40, 10))
                        game_over = True


            # Player 2 Input
            else:
                pos_x = event.pos[0]
                col = int(math.floor(pos_x / square_size))

                if is_valid(board, col):
                    row = get_next_row(board, col)
                    place(board, row, col, 2)
                    if winning(board, 2):
                        label = font.render("Player 2 wins!", 1, YELLOW_COLOUR)
                        window.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
