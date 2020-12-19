import pygame

pygame.init()  # initiate game

screenWidth = 500
win = pygame.display.set_mode((500, screenWidth))
pygame.display.set_caption("Bear Bare")
clock = pygame.time.Clock()  # set up the clock

# vars:
player_x = 50
player_y = 50
player_width = 40
player_height = 60
player_velocity = 5

game_run = True
while game_run:
    clock.tick(60)  # maintain 60 fps
    for event in pygame.event.get():  # check all events
        if event.type == pygame.QUIT:
            game_run = False

    keys = pygame.key.get_pressed()  # moving keys
    if keys[pygame.K_a] and player_x > player_velocity:
        player_x -= player_velocity
    if keys[pygame.K_d] and player_x < screenWidth - player_width - player_velocity:
        player_x += player_velocity
    if keys[pygame.K_w] and player_y > player_velocity:
        player_y -= player_velocity
    if keys[pygame.K_s] and player_y < screenWidth - player_height - player_velocity:
        player_y += player_velocity

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (player_x, player_y, player_width, player_height))
    pygame.display.update()

pygame.quit()
