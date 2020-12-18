import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()  # set up the clock

pygame.init()  # initiates pygame

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window
player_image = pygame.image.load('bear.png')

while True:  # game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Bye!")
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)  # maintain 60 fps
