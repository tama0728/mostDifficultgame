import sys
import pygame as py
import math

url = "/Users/gimdong-yun/Desktop/SynologyDrive/F/ShortCut/Uni/2022/2학기/알고리즘과게임콘텐츠/팀플/code/image/"

# url = "F:/ShortCut/Uni/2022/2학기/알고리즘과게임콘텐츠/팀플/code/image/"


class Character(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "sumong.png").convert_alpha()
        self.image = py.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = round(SCREEN_WIDTH / 2)
        self.rect.y = round(SCREEN_HEIGHT / 2)
        self.startx = 0
        self.starty = 0
        self.death = 0


class Obstacle(py.sprite.Sprite):
    def __init__(self, x, y, speed, degrees=0, r=0, maxx=1280, minx=0, maxy = 720, miny = 0):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "circle_red.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.centerx = x
        self.centery = y
        self.speed = speed
        self.degrees = degrees
        self.r = r
        self.k = 0
        self.maxx = maxx
        self.maxy = maxy
        self.minx = minx
        self.miny = miny
        self.goal = 0

    def updateLinear(self, back):
        if self.degrees == 0:
            self.rect.x += self.speed
        elif self.degrees >= 100:
            self.rect.y += self.speed
        else:
            self.rect.x += self.speed
            self.rect.y += self.speed * self.degrees
        if py.sprite.collide_mask(self, back):
            self.speed *= -1
        if self.rect.x > self.maxx or self.rect.x < self.minx or self.rect.y > self.maxy or self.rect.y < self.miny:
            self.speed *= -1

    def updateCircle(self):
        self.rect.x = self.r * math.sin(math.radians(self.k)) + self.centerx
        self.rect.y = self.r * math.cos(math.radians(self.k)) + self.centery
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
        self.color = py.image.load(url + "map01c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        obs01 = Obstacle(250, 380, -8, 100, 0, 1280, 0, 450, 310)
        obs02 = Obstacle(170, 380, -8, 100, 0, 1280, 0, 450, 310)
        obs03 = Obstacle(290, 380,  8, 100, 0, 1280, 0, 450, 310)
        obs04 = Obstacle(210, 380,  8, 100, 0, 1280, 0, 450, 310)
        obs05 = Obstacle(330, 380, -8, 100, 0, 1280, 0, 450, 310)
        obs06 = Obstacle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, -2, 0, 0, 200)
        obs07 = Obstacle(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2, 2, 0, 0, 100)
        obs08 = Obstacle(250, 565, 3, -2, 0, 400, 250)
        self.obs = [obs01, obs02, obs03, obs04, obs05]
        self.obsC = []
        self.size = (110, 110)
        self.loc = (1080, 255)
        character.startx = 100
        character.starty = 360
        character.rect.x = 100
        character.rect.y = 360

    def round02(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map02.png").convert_alpha()
        self.color = py.image.load(url + "map02c.png").convert_alpha()
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
        self.loc = (100, 250)

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

        for i in self.obs + self.obsC:
            if py.sprite.collide_mask(i, character):
                character.rect.x = character.startx
                character.rect.y = character.starty
                character.death += 1

        screen.fill(white)
        screen.blit(self.image, (0, 0))
        screen.blit(self.color, (0, 0))

        for i in self.obs + self.obsC:
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
font = py.font.SysFont("arial", 30)
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

        elif stage.step == 3:
            stage.round03()
            endpoint = Endpoint(stage.size, stage.loc)
            stage.bool = False

        elif stage.step == 4:
            stage.round04()
            endpoint = Endpoint(stage.size, stage.loc)
            stage.bool = False

    if py.sprite.collide_mask(character, endpoint):
        character.rect.x = SCREEN_WIDTH / 2
        character.rect.y = SCREEN_HEIGHT / 2
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
    death = font.render(f"Death : {character.death:,}", True, True)
    screen.blit(death, (50, 20))
    py.display.update()
