import pygame
import sys
from copy import deepcopy

WIDTH, HEIGHT = 10, 20;
TILE = 45;
GAME_RES = (WIDTH * TILE, HEIGHT * TILE)

CLOCK = pygame.time.Clock()
GRID = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]

pygame.init()
screen = pygame.display.set_mode(GAME_RES)
pygame.display.set_caption("Tetris")

while True:
    screen.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in GRID]
    pygame.display.update()
    CLOCK.tick(60)