import pygame
import sys
import random
import math
from ..env_var.env_var import *
from pygame.locals import *


def text_pos(pos):
    return [pos[0] - text_recal[0], pos[1] - text_recal[1]]


class vector (object):
    def __init__(self, x = 0, y = 0, randspeed = 0):
        if randspeed:
            self.randomize (randspeed)
        else:
            self.x, self.y = x, y

    def __add__(self, a):
        rx, ry = self.x + a.x, self.y + a.y
        return vector(rx, ry)

    def __radd__(self, a):
        rx, ry = self.x + a.x, self.y + a.y
        return vector(rx, ry)

    def __str__(self):
        return ('({} ; {})'.format(self.x, self.y))

    def getpos(self):
        return (self.x, self.y)

    def randomize(self, speed):
        self.x = random.randrange (0, speed + 1)
        self.y = round(math.sqrt (speed * speed - self.x * self.x))


class point (vector):
    pass


class Ball (object):
    def __init__(self):
        random.seed()
        self.text = chr(random.randrange(ord('A'), ord('Z')))
        pygame.init()
        self.color = colors['blue']
        self.font = pygame.font.SysFont('Consolas', 20)

    def move(self, screen):
        self.pos += self.step
        if self.pos[1] + radius >= screen.get_height():
            return False
        else:
            pygame.draw.circle(screen, self.color, self.pos, radius)
            text_box = self.font.render(self.text, True, colors['red'])
            screen.blit(text_box, text_pos(self.pos))
            pygame.display.update()
            return True

    def create(self, screen, step):
        random.seed()
        h, w = screen.get_height(), screen.get_width()
        x = random.randrange (radius + 1, w - radius)
        y = random.randrange (radius + 1, h - radius)
        self.pos = point (x, y)
        self.step = step
        self.fall(screen)
