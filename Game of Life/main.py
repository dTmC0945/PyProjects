import sys
import pygame
import numpy as np


class GameOfLife:
    def __init__(self, surface, width=640, height=480, scale=10, offset=1, active_color=(255, 255, 255),
                 inactive_color=(50, 50, 50)):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color


pygame.init()
pygame.display.set_caption("Conway's Game of Life")

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

conway = GameOfLife(screen, scale=13)

clock = pygame.time.Clock()
fps = 60

while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
