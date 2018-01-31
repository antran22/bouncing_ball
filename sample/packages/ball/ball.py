import pygame
import sys
import random
from ..env_var.env_var import *
from pygame.locals import *
def text_pos (pos):
    return [pos[0] - text_recal[0], pos[1] - text_recal[1]]
class Ball (object):
    def __init__(self):
        random.seed()
        self.text = chr(random.randrange(ord('A'), ord('Z')))
        pygame.init()
        self.color = colors['blue']
        self.font = pygame.font.SysFont('Consolas', 20)

    def fall(self, screen):
        pre_pos = self.pos
        self.pos[1] += self.step
        if self.pos[1] + radius >= screen.get_height():
        	return False
        else:
            pygame.draw.circle(screen, self.color, self.pos, radius)
            text_box = self.font.render (self.text, True, colors['red'])
            screen.blit (text_box, text_pos (self.pos))
            pygame.display.update()
            return True

    def create(self, screen, x, step):
        self.pos = [x, radius - step]
        self.step = step
        self.fall(screen)
