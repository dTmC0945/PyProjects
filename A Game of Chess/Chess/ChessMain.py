"""
This is our main driver file, It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
from ChessEngine import *

WIDTH = HEIGHT = 512
DIMENSION = 8  # Chessboard is an 8 by 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # For animation use.
IMAGES = {}

"""
Initialise a global dictionary of images. This will be called exactly once in the main().
"""


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + "wp.png")
    # NOTE: can access an image by saying "IMAGES["wp"]
