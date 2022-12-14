import sys
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()