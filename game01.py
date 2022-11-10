import sys
import os
import pygame as py
import math

url = os.path.dirname(os.path.abspath(__file__)) + "/image/"


class Character(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "sumong.png").convert_alpha()
        self.image = py.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = round(SCREEN_WIDTH / 2)
        self.rect.y = round(SCREEN_HEIGHT / 2)
        self.startx = 0
        self.starty = 0
        self.death = 0


class Coin(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "coin.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class Obstacle(py.sprite.Sprite):
    def __init__(self, x, y, speed, degrees=0, r=0, k=0, maxx=1280, minx=0, maxy = 720, miny = 0):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "circle_red.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.centerx = x
        self.centery = y
        self.speed = speed
        self.degrees = degrees
        self.r = r
        self.k = k
        self.maxx = maxx
        self.maxy = maxy
        self.minx = minx
        self.miny = miny
        self.goal = 0

    def updateLinear(self, back):
        if self.degrees == 0:
            self.rect.centerx += self.speed
        elif self.degrees >= 100:
            self.rect.centery += self.speed
        else:
            self.rect.centerx += self.speed
            self.rect.centery += self.speed * self.degrees
        if py.sprite.collide_mask(self, back):
            self.speed *= -1
        if self.rect.centerx > self.maxx or self.rect.centerx < self.minx or self.rect.centery > self.maxy or self.rect.centery < self.miny:
            self.speed *= -1

    def updateCircle(self):
        self.rect.centerx = self.r * math.sin(math.radians(self.k)) + self.centerx
        self.rect.centery = self.r * math.cos(math.radians(self.k)) + self.centery
        self.k += self.speed
        if self.k > 360:
            self.k = 0


class Round(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.step = 1
        self.bool = True
        self.coin = 0

    def round01(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map01.png").convert_alpha()
        self.color = py.image.load(url + "map01c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        self.obs = []
        self.obsC = []
        self.coinl = []
        for i in range(0, 5, 1):
            self.obs.append(Obstacle(170+i*40, 380, 8*(-1)**i, 100, 0, 0, 1280, 0, 450, 310))

        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                self.obsC.append(Obstacle(480, 170+i*140, 3, 0, 50, j*90))

        for i in range(0, 4, 1):
            for j in range(0, 2, 1):
                self.obsC.append(Obstacle(750, 375, 3, 0, 40+j*50, i*90))

        self.obs.append(Obstacle(900, 120, 5, 1, 0, 0, 1280, 0, 330, 120))
        self.obs.append(Obstacle(1030, 330, -5, 1, 0, 0, 1280, 0, 330, 120))
        self.obs.append(Obstacle(770, 120, 5, 1, 0, 0, 1280, 0, 330, 120))

        self.obs.append(Obstacle(990, 400, 5, -1, 0, 0, 1280, 0, 600, 400))
        self.obs.append(Obstacle(900, 600, -5, -1, 0, 0, 1280, 0, 600, 400))

        for i in range(0, 5, 1):
            self.coinl.append(Coin(170+i*40, 310))
        for i in range(0, 5, 1):
            self.coinl.append(Coin(170+i*40, 450))
        for i in range(0, 4, 1):
            self.coinl.append(Coin(480, 170+i*140))
        for i in range(0, 2, 1):
            self.coinl.append(Coin(750, 295+i*170))

        self.coinl.append(Coin(820, 100))
        self.coinl.append(Coin(820, 600))

        character.startx = 100
        character.starty = 360
        character.rect.x = 100
        character.rect.y = 360
        self.coin = 18
        self.get_coin = 0

    def round02(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map02.png").convert_alpha()
        self.color = py.image.load(url + "map02c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        self.obs = []
        self.obsC = []
        self.coinl = []
        self.coinl.append(Coin(1000, 360))
        self.coin = 1
        self.get_coin = 0

    def round03(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map03.png").convert_alpha()
        self.color = py.image.load(url + "map03c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        obs01 = Obstacle(700, 100, 5)
        obs02 = Obstacle(500, 565, 5, 100)
        obs05 = Obstacle(250, 200, 5)
        obs06 = Obstacle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -2, 0, 200)
        obs07 = Obstacle(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2, 2, 0, 200)
        self.obs = [obs01, obs02, obs05]
        self.obsC = [obs06, obs07]
        self.size = (110, 110)
        self.loc = (640, 150)

    def round04(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map04.png").convert_alpha()
        self.color = py.image.load(url + "map04c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        obs01 = Obstacle(700, 100, 5)
        obs02 = Obstacle(500, 565, 5, 100)
        obs05 = Obstacle(250, 200, 5)
        obs06 = Obstacle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -2, 0, 200)
        obs07 = Obstacle(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2, 2, 0, 200)
        self.obs = [obs01, obs02, obs05]
        self.obsC = [obs06, obs07]
        self.size = (110, 110)
        self.loc = (640, 150)

    def update(self, map):

        for i in self.obs:
            i.updateLinear(map)

        for i in self.obsC:
            i.updateCircle()

        # for i in self.obs + self.obsC:
        #     if py.sprite.collide_mask(i, character):
        #         stage.bool = True
        #         character.death += 1

        for i in self.coinl:
            if py.sprite.collide_mask(i, character):
                self.coinl.remove(i)
                self.get_coin += 1


        screen.fill(white)
        screen.blit(self.image, (0, 0))
        screen.blit(self.color, (0, 0))
        for i in self.coinl:
            screen.blit(i.image, i.rect)

        for i in self.obs + self.obsC:
            screen.blit(i.image, i.rect)


class Endpoint(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)

    def round01(self):
        self.image = py.image.load(url + "map01end.png").convert_alpha()
        self.rect = self.image.get_rect()

    def round02(self):
        self.image = py.image.load(url + "map02end.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        screen.blit(self.image, (0, 0))


def display_death():
    death = font.render(f"Death : {character.death:,}", True, True)
    screen.blit(death, (5, 5))


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

white = (0xff, 0xff, 0xff)
black = (0, 0, 0)
x = True
y = False
k = 0

py.init()
font = py.font.SysFont("arial", 25)
py.display.set_caption("1")
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
white_image = py.image.load(url+"white.png").convert_alpha()
white_image = py.transform.scale(white_image, (250, 50))

character = Character()
clock = py.time.Clock()
stage = Round()

while True:
    clock.tick(30)
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

    if stage.bool:
        if stage.step == 1:
            stage.round01()
            endpoint = Endpoint()
            endpoint.round01()
            stage.bool = False

        elif stage.step == 2:
            stage.round02()
            endpoint = Endpoint()
            endpoint.round02()
            stage.bool = False

        elif stage.step == 3:
            stage.round03()
            endpoint = Endpoint()
            stage.bool = False

        elif stage.step == 4:
            stage.round04()
            endpoint = Endpoint()
            stage.bool = False

    if py.sprite.collide_mask(character, endpoint) and stage.coin <= stage.get_coin:
        stage.step += 1
        stage.bool = True

    stage.update(stage)
    key_event = py.key.get_pressed()
    if not py.sprite.collide_mask(stage, character):
        if key_event[py.K_LEFT]:
            character.rect.x -= 5
            if py.sprite.collide_mask(stage, character):
                character.rect.x += 5
        if key_event[py.K_RIGHT]:
            character.rect.x += 5
            if py.sprite.collide_mask(stage, character):
                character.rect.x -= 5
        if key_event[py.K_UP]:
            character.rect.y -= 5
            if py.sprite.collide_mask(stage, character):
                character.rect.y += 5
        if key_event[py.K_DOWN]:
            character.rect.y += 5
            if py.sprite.collide_mask(stage, character):
                character.rect.y -= 5

    endpoint.update()
    screen.blit(character.image, character.rect)
    display_death()
    py.display.update()
