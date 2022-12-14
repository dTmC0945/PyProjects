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

    screen.fill((255,255,255))

    pygame.draw.rect(screen, (25, 25, 112), [(640/2) - 50, (480/2) - 50, 100, 100])
    pygame.display.update()