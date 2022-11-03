import sys
import pygame as py

url = "/Users/gimdong-yun/Desktop/SynologyDrive/F/ShortCut/Uni/2022/2학기/알고리즘과게임콘텐츠/팀플/code/image/"
# url = "F:/ShortCut/Uni/2022/2학기/알고리즘과게임콘텐츠/팀플/code/image/"


class Background(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)


class Character(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "snoopy_spoon.png").convert_alpha()
        self.image = py.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = round(SCREEN_WIDTH / 2)
        self.rect.y = round(SCREEN_HEIGHT / 2)


class Circle(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "circle_red.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.c = True

    def update(self, speed, maxx, minx, maxy, miny):
        if self.c:
            self.rect.y += speed
            if self.rect.y > maxy:
                self.c = False
            else:
                self.c = True
        else:
            self.rect.y -= speed
            if self.rect.y < miny:
                self.c = True
            else:
                self.c = False


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

white = (0xff, 0xff, 0xff)
black = (0, 0, 0)

py.init()
py.display.set_caption("1")
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

character = Character()
background = Background()
circle01 = Circle(300, 100)
circle02 = Circle(500, 565)
circle03 = Circle(700, 100)
circles = [circle01, circle02, circle03]

clock = py.time.Clock()

while True:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

    key_event = py.key.get_pressed()
    if not py.sprite.collide_mask(background, character):
        if key_event[py.K_LEFT]:
            character.rect.x -= 5
            if py.sprite.collide_mask(background, character):
                character.rect.x += 5
        if key_event[py.K_RIGHT]:
            character.rect.x += 5
            if py.sprite.collide_mask(background, character):
                character.rect.x -= 5
        if key_event[py.K_UP]:
            character.rect.y -= 5
            if py.sprite.collide_mask(background, character):
                character.rect.y += 5
        if key_event[py.K_DOWN]:
            character.rect.y += 5
            if py.sprite.collide_mask(background, character):
                character.rect.y -= 5
    for i in circles:
        i.update(5, 0, 0, 565, 100)

        if py.sprite.collide_mask(i, character):
            character.rect.x = round(SCREEN_WIDTH / 2)
            character.rect.y = round(SCREEN_HEIGHT / 2)

    screen.fill(white)
    screen.blit(background.image, (0, 0))
    screen.blit(character.image, character.rect)
    for i in circles:
        screen.blit(i.image, i.rect)
    py.display.update()
