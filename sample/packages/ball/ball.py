import pygame
import sys
import random
from ..env_var.env_var import *
from pygame.locals import *
from ..geometry import vector

class Ball (object):
    def __init__(self):
        random.seed()
        self.text = chr(random.randrange(ord('A'), ord('Z')))
        pygame.init()
        self.color = ball_color
        self.font = pygame.font.SysFont('Consolas', text_size)

    def randomize_step(self, speed):
        move_vector = vector.vector(randspeed=speed)
        self.step = move_vector

    def rebound(self, screen):
        h, w = screen.get_height(), screen.get_width()
        if self.pos.x >= w + rebound_range or self.pos.x <= -rebound_range or self.pos.y >= h + rebound_range or self.pos.y <= -rebound_range:
            self.pos = vector.vector(w // 2, h // 2)

    def move(self, screen):
        self.pos += self.step
        self.rebound (screen)
        pygame.draw.circle(screen, self.color, self.pos.getpos(), radius)
        text_box = self.font.render(self.text, True, text_color)
        tw, th = text_box.get_size()
        cx, cy = self.pos.getpos()
        screen.blit(text_box, (cx - tw // 2, cy - th // 2))
        pygame.display.update()
        test = self.hit_the_wall(screen)
        x, y = self.step.getpos()
        if test != 'none':
            if test == 'hit_both':
                self.step = vector.vector(-y, -x)
            elif test == 'hit_w':
                self.step = vector.vector(-x, y)
            elif test == 'hit_h':
                self.step = vector.vector(x, -y)

    def create(self, screen, x=-1, y=-1, step=vector.vector(0, 0)):
        random.seed()
        h, w = screen.get_height(), screen.get_width()
        if x == -1:
            x = random.randrange(radius + 1, w - radius)
        if y == -1:
            y = random.randrange(radius + 1, h - radius)
        self.pos = vector.point(x, y)
        self.step = vector.vector(0, 0)
        self.move(screen)
        self.step = step

    def hit_the_wall(self, screen):
        w, h = screen.get_width(), screen.get_height()
        x, y = self.pos.getpos()
        hit_h, hit_w = False, False
        if x <= radius + 2 or x >= w - radius - 2:
            hit_w = True
        if y <= radius + 2 or y >= h - radius - 2:
            hit_h = True
        if hit_h and hit_w:
            return 'hit_both'
        elif hit_h:
            return 'hit_h'
        elif hit_w:
            return 'hit_w'
        else:
            return 'none'
