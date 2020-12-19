import pygame

pygame.init()  # initiate game
clock = pygame.time.Clock()  # set up the clock
screenSize = (1920, 1020)
win = pygame.display.set_mode((screenSize[0], screenSize[1]))
pygame.display.set_caption("Lum-Bear-Jack")

# bg = pygame.image.load()
player_image = pygame.image.load('images/Bear_walks_right/1.png')
bg = pygame.image.load('images/background.png')


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2.7
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = [pygame.image.load('images/Bear_walks_right/2.png'),
                          pygame.image.load('images/Bear_walks_right/3.png'),
                          pygame.image.load('images/Bear_walks_right/4.png'),
                          pygame.image.load('images/Bear_walks_right/5.png'),
                          pygame.image.load('images/Bear_walks_right/6.png'),
                          pygame.image.load('images/Bear_walks_right/7.png'),
                          pygame.image.load('images/Bear_walks_right/8.png'),
                          pygame.image.load('images/Bear_walks_right/9.png'),
                          pygame.image.load('images/Bear_walks_right/10.png'),
                          pygame.image.load('images/Bear_walks_right/11.png'),
                          pygame.image.load('images/Bear_walks_right/12.png'),
                          pygame.image.load('images/Bear_walks_right/13.png'),
                          pygame.image.load('images/Bear_walks_right/14.png'),
                          pygame.image.load('images/Bear_walks_right/15.png')]
        self.walkLeft = [pygame.image.load('images/Bear_walks_left/2.png'),
                         pygame.image.load('images/Bear_walks_left/3.png'),
                         pygame.image.load('images/Bear_walks_left/4.png'),
                         pygame.image.load('images/Bear_walks_left/5.png'),
                         pygame.image.load('images/Bear_walks_left/6.png'),
                         pygame.image.load('images/Bear_walks_left/7.png'),
                         pygame.image.load('images/Bear_walks_left/8.png'),
                         pygame.image.load('images/Bear_walks_left/9.png'),
                         pygame.image.load('images/Bear_walks_left/10.png'),
                         pygame.image.load('images/Bear_walks_left/11.png'),
                         pygame.image.load('images/Bear_walks_left/12.png'),
                         pygame.image.load('images/Bear_walks_left/13.png'),
                         pygame.image.load('images/Bear_walks_left/14.png'),
                         pygame.image.load('images/Bear_walks_left/15.png')]

    def draw(self, window):
        if self.walkCount + 1 >= 14:
            self.walkCount = 0

        if self.left:
            window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(player_image, (self.x, self.y))


def redraw_game_window():
    win.blit(bg, (0, 0))
    Bear.draw(win)
    pygame.display.update()


Bear = Player(750, 450, 60, 60)
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
        Bear.left = True
        Bear.right = False
    elif keys[pygame.K_d] and Bear.x < screenSize[0] - Bear.width - Bear.vel:
        Bear.x += Bear.vel
        Bear.right = True
        Bear.left = False
    else:
        Bear.right = False
        Bear.left = False
        walkCount = 0
    if keys[pygame.K_w] and Bear.y > Bear.vel:
        Bear.y -= Bear.vel
    if keys[pygame.K_s] and Bear.y < screenSize[0] - Bear.height - Bear.vel:
        Bear.y += Bear.vel

pygame.quit()
