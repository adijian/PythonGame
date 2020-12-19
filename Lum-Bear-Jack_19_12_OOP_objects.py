import pygame

pygame.init()  # initiate game
clock = pygame.time.Clock()  # set up the clock
screenSize = (1920, 1020)
win = pygame.display.set_mode((screenSize[0], screenSize[1]))
pygame.display.set_caption("Lum-Bear-Jack")

player_image = pygame.image.load('images/Bear_walks_right/1.png')
bg = pygame.image.load('images/background.png')


class Player:  # init player
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
        self.box = pygame.Rect(self.x, self.y, player_image.get_width(), player_image.get_height())
        self.up = False
        self.down = False
        self.movement = [0, 0]
        self.tiles = [pygame.Rect(800, 800, 100, 100), pygame.Rect(100, 100, 100, 100)]

    def keys(self):  # basic walking keys of character
        keys = pygame.key.get_pressed()  # moving keys
        if keys[pygame.K_a] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
        elif keys[pygame.K_d] and self.x < screenSize[0] - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0
        if keys[pygame.K_w] and self.y > self.vel:
            self.y -= self.vel
            self.up = True
            self.down = False
        if keys[pygame.K_s] and self.y < screenSize[0] - self.height - self.vel:
            self.y += self.vel
            self.down = True
            self.up = False

    def walking_animation(self, window):  # show walking animations
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

    def collision_test(self):
        collisions = []  # number of collisions
        for tile in self.tiles:
            if self.box.colliderect(tile):
                collisions.append(tile)
        return collisions

    def move_collision(self):  # player movement collision
        self.box.x += self.movement[0]
        collisions = self.collision_test()
        for tile in collisions:
            if self.movement[0] > 0:
                self.box.right = tile.left
            if self.movement[0] < 0:
                self.box.left = tile.right
        self.box.y += self.movement[0]
        collisions = self.collision_test()
        for tile in collisions:
            if self.movement[1] > 0:
                self.box.bottom = tile.top
            if self.movement[1] < 0:
                self.box.top = tile.bottom
        return self.box

    def movement(self):
        if self.right:
            self.movement[0] += 5
        if self.left:
            self.movement[0] -= 5
        if self.up:
            self.movement[1] -= 5
        if self.down:
            self.movement[1] += 5

    def redraw_game_window(self):
        win.blit(bg, (0, 0))
        self.box = self.move_collision()
        self.box.x = self.x
        self.box.y = self.y
        for tile in self.tiles:
            pygame.draw.rect(win, (255, 255, 255), tile)
        pygame.draw.rect(win, (255, 255, 255), self.box)
        self.walking_animation(win)
        pygame.display.update()


# GAME vars -----------------------------------------------
Bear = Player(750, 450, 60, 60)
global tiles
# tiles = [pygame.Rect(800, 800, 100, 100), pygame.Rect(100, 100, 100, 100)]
down = False
up = False
game_run = True
# GAME ----------------------------------------------------
while game_run:
    clock.tick(60)  # maintain 60 fps
    Bear.redraw_game_window()
    for event in pygame.event.get():  # check all events
        if event.type == pygame.QUIT:
            game_run = False
    Bear.keys()

pygame.quit()
