import pygame

pygame.init()  # initiate game

screenSize = (1920, 1020)
win = pygame.display.set_mode((screenSize[0], screenSize[1]))
pygame.display.set_caption("Lum-Bear-Jack")
clock = pygame.time.Clock()  # set up the clock

walkRight = [pygame.image.load('images/Bear walks right/2.png'), pygame.image.load('images/Bear walks right/3.png'),
             pygame.image.load('images/Bear walks right/4.png'), pygame.image.load('images/Bear walks right/5.png'), pygame.image.load('images/Bear walks right/6.png'),
             pygame.image.load('images/Bear walks right/7.png'), pygame.image.load('images/Bear walks right/8.png'), pygame.image.load('images/Bear walks right/9.png'),
             pygame.image.load('images/Bear walks right/10.png'), pygame.image.load('images/Bear walks right/11.png'), pygame.image.load('images/Bear walks right/12.png'),
             pygame.image.load('images/Bear walks right/13.png'), pygame.image.load('images/Bear walks right/14.png'), pygame.image.load('images/Bear walks right/15.png')]
walkLeft = [pygame.image.load('images/Bear walks left/2.png'), pygame.image.load('images/Bear walks left/3.png'),
            pygame.image.load('images/Bear walks left/4.png'), pygame.image.load('images/Bear walks left/5.png'), pygame.image.load('images/Bear walks left/6.png'),
            pygame.image.load('images/Bear walks left/7.png'), pygame.image.load('images/Bear walks left/8.png'), pygame.image.load('images/Bear walks left/9.png'),
            pygame.image.load('images/Bear walks left/10.png'), pygame.image.load('images/Bear walks left/11.png'), pygame.image.load('images/Bear walks left/12.png'),
            pygame.image.load('images/Bear walks left/13.png'), pygame.image.load('images/Bear walks left/14.png'), pygame.image.load('images/Bear walks left/15.png')]
# bg = pygame.image.load()
player_image = pygame.image.load('images/Bear walks right/1.png')
# vars:
player_x = 50
player_y = 50
player_width = 40
player_height = 60
player_velocity = 5
left = False
right = False
walkCount = 0


def redraw_game_window():
    global walkCount
    win.fill((0, 0, 0))

    if walkCount + 1 >= 14:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (player_x, player_y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (player_x, player_y))
        walkCount += 1
    else:
        win.blit(player_image, (player_x, player_y))

    pygame.display.update()

game_run = True
while game_run:
    clock.tick(60)  # maintain 60 fps
    for event in pygame.event.get():  # check all events
        if event.type == pygame.QUIT:
            game_run = False

    keys = pygame.key.get_pressed()  # moving keys
    if keys[pygame.K_a] and player_x > player_velocity:
        player_x -= player_velocity
        left = True
        right = False
    elif keys[pygame.K_d] and player_x < screenSize[0] - player_width - player_velocity:
        player_x += player_velocity
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if keys[pygame.K_w] and player_y > player_velocity:
        player_y -= player_velocity
    if keys[pygame.K_s] and player_y < screenSize[0] - player_height - player_velocity:
        player_y += player_velocity

    redraw_game_window()

pygame.quit()
