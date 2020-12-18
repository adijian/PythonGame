import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()  # set up the clock

pygame.init()  # initiates pygame

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate the window
player_image = pygame.image.load('bear.png')
moving_right = False
moving_left = False

while True:  # game-loop

    screen.blit(player_image, (50, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            print("Bye! \nMade by Adi Jian @2021")
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(60)  # maintain 60 fps
