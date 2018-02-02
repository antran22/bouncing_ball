import pygame
import sys
import random
from ..env_var.env_var import *
from pygame.locals import *
from ..vector.vector import *

def text_pos(pos):
    x, y = text_recal
    return (pos - vector(x, y)).getpos()


class Ball (object):
    def __init__(self):
        random.seed()
        self.text = chr(random.randrange(ord('A'), ord('Z')))
        pygame.init()
        self.color = colors['blue']
        self.font = pygame.font.SysFont('Consolas', 20)

    def move(self, screen):
        self.pos += self.step
        pygame.draw.circle(screen, self.color, self.pos.getpos(), radius)
        text_box = self.font.render(self.text, True, colors['red'])
        screen.blit(text_box, text_pos(self.pos))
        pygame.display.update()
        return True

    def create(self, screen, x = -1, y = -1, step=vector(0, 0)):
        random.seed()
        h, w = screen.get_height(), screen.get_width()
        if x == -1:
            x = random.randrange(radius + 1, w - radius)
        if y == -1:
            y = random.randrange(radius + 1, h - radius)
        self.pos = point(x, y)
        self.step = vector(0, 0)
        self.move(screen)
        self.step = step
