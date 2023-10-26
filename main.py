from random import randint
from pygame.locals import *
import pygame
import sys


class MyGroup(pygame.sprite.Group):
    def draw(self, surface):
        for sprite in self.sprites():
            if sprite.rect.collidepoint(pygame.mouse.get_pos()) and iv:
                sprite.fl_open = True
            if sprite.fl_open:
                surface.blit(sprite.image, sprite.rect)
            else:
                surface.blit(sprite.imag, sprite.rect)


class Cell(pygame.sprite.Sprite):
    def __init__(self, around_mines, mine):
        super().__init__()
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
        self.x = 0
        self.y = 0
        self.imag = empty
        self.surface = pygame.Surface((60, 60))
        self.text = font.render(str(self.around_mines), True, 'black')
        self.surface.fill('black')
        self.surface.blit(self.text, (10, 10))
        self.image = self.surface
        self.rect = 0


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.init()

    def init(self):
        pole = [[Cell(0, False) for j in range(self.N)] for i in range(self.N)]
        m = self.M
        list_mina_pole = []
        while True:
            i, j = randint(0, self.N-1), randint(0, self.N-1)
            if pole[i][j].mine:
                continue
            else:
                pole[i][j].mine = True
                pole[i][j].image = bomb
                list_mina_pole += [(i, j,)]
                m -= 1
                if m == 0:
                    break
        for i in range(self.N):
            for j in range(self.N):
                if pole[i][j].mine:
                    pole[i][j].rect = pygame.Rect((i*60, j*60, 60, 60))
                    all_sprites.add(pole[i][j])
                    continue
                sp_round = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j), (i, j + 1),
                            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
                pole[i][j].around_mines = len(list(filter(lambda x: x in sp_round, list_mina_pole)))
                pole[i][j].surface.fill('white')
                sp = ['green', 'blue', 'pink', 'red', 'yellow']
                pole[i][j].text = font.render(str(pole[i][j].around_mines), True, sp[pole[i][j].around_mines])
                pole[i][j].surface.blit(pole[i][j].text, (10, 10))
                pole[i][j].image = pole[i][j].surface
                pole[i][j].x = i * 60
                pole[i][j].y = j * 60
                pole[i][j].rect = pygame.Rect((i*60, j*60, 60, 60))
                all_sprites.add(pole[i][j])
        return pole

    def show(self):
        for i in self.pole:
            print()
            for j in i:
                print(j, end=' ')




bomb = pygame.image.load('bomb.png')
empty = pygame.image.load('empty.png')
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame window 600x600")
all_sprites = MyGroup()
font = pygame.font.Font("sh.ttf", 50)
pole_game = GamePole(10, 12)

while True:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            iv = True
        else:
            iv = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    all_sprites.draw(screen)
    pygame.display.flip()
