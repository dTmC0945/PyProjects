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

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

        def run(self):
            self.draw_grid()

        def draw_grid(self):

            for row in range(self.rows):
                for col in range(self.columns):
                    if self.grid[row, col]:
                        pygame.draw.rect(self.surface, self.active_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
                    else:
                        pygame.draw.rect(self.surface, self.inactive_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])


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
