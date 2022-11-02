import sys
import pygame as py

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


class Circle(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "circle_red.png").convert_alpha()
        self.image = py.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, c) -> bool:
        if c:
            self.rect.y += 5
            if self.rect.y > 575:
                return False
            else:
                return True
        else:
            self.rect.y -= 5
            if self.rect.y < 100:
                return True
            else:
                return False


class Background(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(url + "map01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = round(SCREEN_WIDTH / 2)
        self.rect.centery = round(SCREEN_HEIGHT / 2)


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
c01 = True

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

    c01 = circle01.update(c01)

    if py.sprite.collide_mask(circle01, character):
        character.rect.x = round(SCREEN_WIDTH/2)
        character.rect.y = round(SCREEN_HEIGHT/2)

    screen.fill(white)
    screen.blit(background.image, (0, 0))
    screen.blit(character.image, character.rect)
    screen.blit(circle01.image, circle01.rect)

    py.display.update()
