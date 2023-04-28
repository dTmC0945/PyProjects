"""
This class is responsible for storing all the information about the current state of a chess game.
It will also be responsible for determining the valid moves of the current state. It will also keep a move log.
"""

class GameState():
    def __int__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ]