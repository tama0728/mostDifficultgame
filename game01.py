import sys
import os
import pygame as py
import math

url = (os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1]))


class Character(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/sumong.png").convert_alpha()
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
        self.image = py.image.load(url + "/image/coin.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class Obstacle(py.sprite.Sprite):
    def __init__(self, x, y, speed, degrees=0, r=0, k=0, maxx=1280, minx=0, maxy=720, miny=0):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/circle_red.png").convert_alpha()
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
        self.get_coin = 0

    def round01(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/map01.png").convert_alpha()
        self.color = py.image.load(url + "/image/map01c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        self.obs = []
        self.obsC = []
        self.coinl = []
        for i in range(0, 5, 1):
            self.obs.append(Obstacle(170 + i * 40, 380, 8 * (-1) ** i, 100, 0, 0, 1280, 0, 450, 310))

        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                self.obsC.append(Obstacle(480, 170 + i * 140, 3, 0, 50, j * 90))

        for i in range(0, 4, 1):
            for j in range(0, 2, 1):
                self.obsC.append(Obstacle(750, 375, 3, 0, 40 + j * 50, i * 90))

        self.obs.append(Obstacle(900, 120, 5, 1, 0, 0, 1280, 0, 330, 120))
        self.obs.append(Obstacle(1030, 330, -5, 1, 0, 0, 1280, 0, 330, 120))
        self.obs.append(Obstacle(770, 120, 5, 1, 0, 0, 1280, 0, 330, 120))

        self.obs.append(Obstacle(990, 400, 5, -1, 0, 0, 1280, 0, 600, 400))
        self.obs.append(Obstacle(900, 600, -5, -1, 0, 0, 1280, 0, 600, 400))

        for i in range(0, 5, 1):
            self.coinl.append(Coin(170 + i * 40, 310))
        for i in range(0, 5, 1):
            self.coinl.append(Coin(170 + i * 40, 450))
        for i in range(0, 4, 1):
            self.coinl.append(Coin(480, 170 + i * 140))
        for i in range(0, 2, 1):
            self.coinl.append(Coin(750, 295 + i * 170))

        self.coinl.append(Coin(820, 100))
        self.coinl.append(Coin(820, 600))

        character.rect.x = 100
        character.rect.y = 360
        self.coin = 18
        self.get_coin = 0
        # self.coin = 1

    def round02(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/map02.png").convert_alpha()
        self.color = py.image.load(url + "/image/map02c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        self.obs = []
        self.obsC = []
        self.coinl = []

        for i in range(0, 4, 1):
            for j in range(0, 4, 1):
                self.obsC.append(Obstacle(825, 355, 3, 0, 40 + j * 50, i * 90))

        for i in range(0, 2):
            self.obs.append(Obstacle(190, 120 + i * 80, 8, 0, 0, 0, 510, 190))
        for i in range(0, 2):
            self.obs.append(Obstacle(510, 160 + i * 80, 8, 0, 0, 0, 510, 190))
        for i in range(0, 2):
            self.obs.append(Obstacle(190, 445 + i * 80, 8, 0, 0, 0, 510, 190))
        for i in range(0, 2):
            self.obs.append(Obstacle(510, 485 + i * 80, 8, 0, 0, 0, 510, 190))

        for i in range(0, 2):
            self.obs.append(Obstacle(110 + i * 70, 220, 7, 100, 0, 0, 1280, 0, 500, 220))
        for i in range(0, 2):
            self.obs.append(Obstacle(145 + i * 70, 500, 7, 100, 0, 0, 1280, 0, 500, 220))

        self.coinl.append(Coin(1000, 360))
        self.coinl.append(Coin(850, 140))
        self.coinl.append(Coin(810, 600))
        self.coinl.append(Coin(150, 150))
        self.coinl.append(Coin(150, 500))

        self.coin = 5
        self.get_coin = 0
        character.rect.x = 1150
        character.rect.y = 360
        # self.coin = 1


    def round03(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/map03.png").convert_alpha()
        self.color = py.image.load(url + "/image/map03c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        self.coin = 0
        self.obs = []
        self.obsC = []
        self.coinl = []
        self.obs.append(Obstacle(430, 170,  7, 0, 0, 0, 500, 430))
        self.obs.append(Obstacle(850, 170, -7, 0, 0, 0, 850, 780))
        for i in range(0, 2):
            self.obs.append(Obstacle(500, 100 + i * 100, -10, 0, 0, 0, 780, 500))
            self.coinl.append(Coin(500, 100 + i * 100))
            self.coinl.append(Coin(780, 100 + i * 100))
            self.coin += 2
        for i in range(0, 2):
            self.obs.append(Obstacle(780, 150 + i * 100,  10, 0, 0, 0, 780, 500))
            self.coinl.append(Coin(500, 150 + i * 100))
            self.coinl.append(Coin(780, 150 + i * 100))
            self.coin += 2

        for i in range(0, 4):
            for j in range(0, 4, 1):
                self.obsC.append(Obstacle(410 + i * 150, 330, -6, 0, 50, j * 90))
            self.coinl.append(Coin(410 + i * 150, 330))
            self.coin += 1

        for i in range(0, 3):
            self.obs.append(Obstacle(440 + i * 200, 400,  10, 100, 0, 0, 1280, 0, 600, 400))
            self.coinl.append(Coin(440 + i * 200, 400))
            self.coinl.append(Coin(440 + i * 200, 600))
            self.coin += 2

        for i in range(0, 2):
            self.obs.append(Obstacle(540 + i * 200, 600, -10, 100, 0, 0, 1280, 0, 600, 400))
            self.coinl.append(Coin(540 + i * 200, 400))
            self.coinl.append(Coin(540 + i * 200, 600))
            self.coin += 2

        self.coinl.append(Coin(640, 250))
        self.coinl.append(Coin(640, 150))
        self.coin += 2
        self.get_coin = 0
        character.rect.x = 355
        character.rect.y = 170
        # self.coin = 1


    def round04(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/map04.png").convert_alpha()
        self.color = py.image.load(url + "/image/map04c.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        self.obs = []
        self.obsC = []
        self.coinl = []
        self.coin = 0
        for i in range(0, 3):
            for j in range(0, 6):
                self.obsC.append(Obstacle(640, 320, -2, 0, 80 + i * 50, j * 60))
        self.coinl.append(Coin(640, 160))
        self.coinl.append(Coin(640, 480))
        self.coin += 2
        for i in range(0, 5):
            self.obs.append(Obstacle(260, 140 + i * 120,  10, 0, 0, 0, 480, 260))
            self.obs.append(Obstacle(1000, 140 + i * 120, -10, 0, 0, 0, 1000, 780))
            self.coinl.append(Coin(280, 140 + i * 120))
            self.coinl.append(Coin(480, 140 + i * 120))
            self.coinl.append(Coin(980, 140 + i * 120))
            self.coinl.append(Coin(780, 140 + i * 120))
            self.coin += 4
        for i in range(0, 4):
            self.obs.append(Obstacle(480, 200 + i * 120, -10, 0, 0, 0, 480, 260))
            self.obs.append(Obstacle(780, 200 + i * 120,  10, 0, 0, 0, 1000, 780))
            self.coinl.append(Coin(480, 200 + i * 120))
            self.coinl.append(Coin(280, 200 + i * 120))
            self.coinl.append(Coin(780, 200 + i * 120))
            self.coinl.append(Coin(980, 200 + i * 120))
            self.coin += 4

        self.coinl.append(Coin(640, 320))
        # self.coin = 1
        self.get_coin = 0
        character.rect.x = 155
        character.rect.y = 270

    def clear(self):
        py.sprite.Sprite.__init__(self)
        clearm = py.mixer.Sound(url + "/music/clear.mp3")
        self.image = py.image.load(url + "/image/end.png").convert_alpha()
        self.restart = py.image.load(url + "/image/restart.png").convert_alpha()
        self.restarts = py.transform.scale(self.restart, (1216, 684))
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        screen.fill(white)
        screen.blit(self.image, (0, 0))
        screen.blit(self.restart, (430, 70))
        clearm.play()
        main = True
        while main:
            clock.tick(60)
            for event in py.event.get():
                if event.type == py.QUIT:
                    sys.exit()

                if event.type == py.MOUSEBUTTONDOWN:
                    pos = py.mouse.get_pos()
                    if 474 + 430 <= pos[0] <= 474 + 430 + 332 and 490 + 70 <= pos[1] <= 490 + 70 + 88:
                        down.play()
                        screen.blit(self.image, (0, 0))
                        screen.blit(self.restarts, (462, 102))

                if event.type == py.MOUSEBUTTONUP:
                    screen.blit(self.image, (0, 0))
                    screen.blit(self.restart, (430, 70))
                    if 474 + 430 <= event.pos[0] <= 474 + 430 + 332 and 490 + 70 <= event.pos[1] <= 490 + 70 + 88:
                        up.play()
                        clearm.stop()
                        main = False

            py.display.update()

    def update(self, map):

        for i in self.obs:
            i.updateLinear(map)

        for i in self.obsC:
            i.updateCircle()

        for i in self.obs + self.obsC:
            if py.sprite.collide_mask(i, character):
                die.play()
                stage.bool = True
                character.death += 1

        for i in self.coinl:
            if py.sprite.collide_mask(i, character):
                coin_sound.play()
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
        self.image = py.image.load(url + "/image/map01end.png").convert_alpha()
        self.rect = self.image.get_rect()

    def round02(self):
        self.image = py.image.load(url + "/image/map02end.png").convert_alpha()
        self.rect = self.image.get_rect()

    def round03(self):
        self.image = py.image.load(url + "/image/map03end.png").convert_alpha()
        self.rect = self.image.get_rect()

    def round04(self):
        self.image = py.image.load(url + "/image/map04end.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        screen.blit(self.image, (0, 0))


class Start(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "/image/start.png").convert_alpha()
        self.images = py.transform.scale(self.image, (1216, 684))
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)
        screen.blit(self.image, (0, 0))


def display_death():
    death = font.render(f"Death : {character.death:,}", True, True)
    screen.blit(death, (5, 5))


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

white = (0xff, 0xff, 0xff)
black = (0, 0, 0)
k = 0

py.init()
icon = py.image.load(url + "/image/sumong.png")
py.display.set_icon(icon)
clock = py.time.Clock()
font = py.font.SysFont("arial", 25)
py.display.set_caption("???(?????????)????????? ??????")
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
main_image = py.image.load(url + "/image/main.png").convert_alpha()
coin_sound = py.mixer.Sound(url + "/music/coin.mp3")
bgm = py.mixer.Sound(url + "/music/bgm.mp3")
clear = py.mixer.Sound(url + "/music/next.mp3")
die = py.mixer.Sound(url + "/music/die.mp3")
down = py.mixer.Sound(url + "/music/down.mp3")
up = py.mixer.Sound(url + "/music/up.mp3")
mainm = py.mixer.Sound(url + "/music/main.mp3")

while True:
    screen.blit(main_image, (0, 0))
    character = Character()
    stage = Round()
    start = Start()
    py.display.update()

    main = True

    mainm.play(-1)

    while main:
        clock.tick(30)
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()

            if event.type == py.MOUSEBUTTONDOWN:
                pos = py.mouse.get_pos()
                if 474 <= pos[0] <= 474 + 332 and 490 <= pos[1] <= 490 + 88:
                    down.play()
                    screen.blit(main_image, (0, 0))
                    screen.blit(start.images, (32, 32))

            if event.type == py.MOUSEBUTTONUP:
                screen.blit(main_image, (0, 0))
                screen.blit(start.image, (0, 0))
                if 474 <= event.pos[0] <= 474 + 332 and 490 <= event.pos[1] <= 490 + 88:
                    up.play()
                    main = False

        py.display.update()
    mainm.stop()
    bgm.play(-1)

    while True:
        clock.tick(30)
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()

        if stage.bool:
            if stage.step == 1:
                endpoint = Endpoint()
                endpoint.round01()
                stage.round01()
                stage.bool = False

            elif stage.step == 2:
                stage.round02()
                endpoint = Endpoint()
                endpoint.round02()
                stage.bool = False

            elif stage.step == 3:
                stage.round03()
                endpoint = Endpoint()
                endpoint.round03()
                stage.bool = False

            elif stage.step == 4:
                stage.round04()
                endpoint = Endpoint()
                endpoint.round04()
                stage.bool = False

            elif stage.step == 5:
                bgm.stop()
                stage.clear()
                break

        if py.sprite.collide_mask(character, endpoint) and stage.coin <= stage.get_coin:
            clear.play()
            stage.step += 1
            stage.bool = True

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

        stage.update(stage)
        endpoint.update()
        screen.blit(character.image, character.rect)
        display_death()
        py.display.update()

