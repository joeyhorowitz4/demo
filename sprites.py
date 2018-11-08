# sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.vx = 0
        self.vy = 0
    def update(self):
        # gravity
        self.vx = 0
        # self.vy = 0
        self.gravity()
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -200
        if keys[pg.K_RIGHT]:
            self.vx = 200
        if keys[pg.K_UP]:
            self.vy = -200
        if keys[pg.K_DOWN]:
            self.vy = 200
        if keys[pg.K_SPACE] and self.falling == False:
            self.jump = 5
        self.rect.x += self.vx
        self.rect.y += self.vy
    def gravity(self):
        if self.rect.y < HEIGHT-40:
            self.falling = True
            print("gravity is happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
            self.vy += 10
        elif self.rect.y >= HEIGHT:
            self.falling = False
            self.vy = 0
            self.rect.y = HEIGHT-40
            print("gravity is NOT happening! " + str(self.rect.y))
            print("falling " + str(self.falling))
    def jump(self):
        # decelerate exponentially
        self.vy = -75
        print("jump called")