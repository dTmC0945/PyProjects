"""
This is our main driver file, It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 # Chessboard is an 8 by 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # For animation use.
IMAGES = {}