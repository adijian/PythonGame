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
moving_down = False
moving_up = False
player_location = [50, 50]
player_y_momentum = 0
player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

while True:  # game-loop
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_location)

    if moving_right == True:
        player_location[0] += 3
    if moving_left == True:
        player_location[0] -= 3
    if moving_down == True:
        player_location[1] += 1.5
    if moving_up == True:
        player_location[1] -= 3

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:  # check for window quit
            print("Bye! \nMade by Adi Jian @2021")
            pygame.quit()  # stop pygame
            sys.exit()  # stop script
        if event.type == KEYDOWN:
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
            if event.key == K_w:
                moving_up = True
            if event.key == K_s:
                moving_down = True
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
            if event.key == K_w:
                moving_up = False
            if event.key == K_s:
                moving_down = False

    pygame.display.update()
    clock.tick(60)  # maintain 60 fps
