import pygame

pygame.init()  # initiate game
clock = pygame.time.Clock()  # set up the clock
screenSize = (1920, 1020)
win = pygame.display.set_mode((screenSize[0], screenSize[1]))
pygame.display.set_caption("Lum-Bear-Jack")

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
background = pygame.image.load('images/background.png')

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 14:
            self.walkCount = 0

        if left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(player_image, (self.x, self.y))


def redraw_game_window():
    win.blit(background, (0, 0))
    Bear.draw(win)
    pygame.display.update()


Bear = player(60, 60, 60, 60)
game_run = True
while game_run:
    clock.tick(60)  # maintain 60 fps
    redraw_game_window()
    for event in pygame.event.get():  # check all events
        if event.type == pygame.QUIT:
            game_run = False

    keys = pygame.key.get_pressed()  # moving keys
    if keys[pygame.K_a] and Bear.x > Bear.vel:
        Bear.x -= Bear.vel
        left = True
        right = False
    elif keys[pygame.K_d] and Bear.x < screenSize[0] - Bear.width - Bear.vel:
        Bear.x += Bear.vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if keys[pygame.K_w] and Bear.y > Bear.vel:
        Bear.y -= Bear.vel
    if keys[pygame.K_s] and Bear.y < screenSize[0] - Bear.height - Bear.vel:
        Bear.y += Bear.vel

pygame.quit()
