import sys
import pygame as py
import math

url = "/Users/gimdong-yun/Desktop/SynologyDrive/F/ShortCut/Uni/2022/2학기/알고리즘과게임콘텐츠/팀플/code/image/"


# url = "F:/ShortCut/Uni/2022/2학기/알고리즘과게임콘텐츠/팀플/code/image/"


class Character(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "snoopy_spoon.png").convert_alpha()
        self.image = py.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = round(SCREEN_WIDTH / 2)
        self.rect.y = round(SCREEN_HEIGHT / 2)


class Obstacle(py.sprite.Sprite):
    def __init__(self, x, y, speed):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "circle_red.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.centerx = x
        self.centery = y
        self.speed = speed
        self.k = 0

    def updateLinear(self, direct, back):
        if direct:
            self.rect.x += self.speed
            if py.sprite.collide_mask(self, back):
                self.speed *= -1
        else:
            self.rect.y += self.speed
            if py.sprite.collide_mask(self, back):
                self.speed *= -1

    def updateObs(self, r):
        self.rect.x = r * math.sin(math.radians(self.k)) + self.centerx
        self.rect.y = r * math.cos(math.radians(self.k)) + self.centery
        self.k += self.speed
        if self.k > 360:
            self.k = 0


class Round(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.step = 1
        self.bool = True

    def round01(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = character.rect.x
        self.rect.centery = character.rect.y
        obs01 = Obstacle(300, 100, 5)
        obs02 = Obstacle(500, 565, 5)
        obs05 = Obstacle(250, 200, 5)
        obs06 = Obstacle(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2, -2)
        obs07 = Obstacle(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2, 2)
        self.circlesY = [obs01, obs02]
        self.circlesX = [obs05]
        self.circlesC = [obs06, obs07]
        self.size = (110, 110)
        self.loc = (1080, 250)

    def round02(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map02.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        obs01 = Obstacle(700, 100, 5)
        obs02 = Obstacle(500, 565, 5)
        obs05 = Obstacle(250, 200, 5)
        obs06 = Obstacle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -2)
        obs07 = Obstacle(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2, 2)
        self.circlesY = [obs01, obs02]
        self.circlesX = [obs05]
        self.circlesC = [obs06, obs07]
        self.size = (110, 110)
        self.loc = (100, 250)

    def update(self, map):
        for i in self.circlesY:
            i.updateLinear(y, map)

        for i in self.circlesX:
            i.updateLinear(x, map)

        for i in self.circlesC:
            i.updateObs(200)

        for i in self.circlesX + self.circlesY + self.circlesC:
            if py.sprite.collide_mask(i, character):
                character.rect.x = round(SCREEN_WIDTH / 2)
                character.rect.y = round(SCREEN_HEIGHT / 2)

        screen.fill(white)
        screen.blit(self.image, (0, 0))

        for i in self.circlesY + self.circlesX + self.circlesC:
            screen.blit(i.image, i.rect)


class Endpoint(py.sprite.Sprite):
    def __init__(self, size, loc):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "skyblue.png").convert_alpha()
        self.image = py.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = loc[0]
        self.rect.y = loc[1]

    def update(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

white = (0xff, 0xff, 0xff)
black = (0, 0, 0)
x = True
y = False
k = 0

py.init()
py.display.set_caption("1")
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

character = Character()
clock = py.time.Clock()
stage = Round()

while True:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

    if stage.bool:
        if stage.step == 1:
            stage.round01()
            endpoint = Endpoint(stage.size, stage.loc)
            stage.bool = False

        elif stage.step == 2:
            stage.round02()
            endpoint = Endpoint(stage.size, stage.loc)
            stage.bool = False

    if py.sprite.collide_mask(character, endpoint):
        character.rect.x = SCREEN_WIDTH/2
        character.rect.y = SCREEN_HEIGHT/2
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

    py.display.update()
