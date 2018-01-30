import pygame
import sys
from pygame.locals import *
black = (0, 0, 0)
white = (255, 255, 255)


class Pane (object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Consolas', 14)
        pygame.display.set_caption('Game')
        self.screen = pygame.display.set_mode((600, 400), 0, 32)
        self.screen.fill(black)
        pygame.display.update()

    def addRect(self, a, b, c, d):
        self.screen.fill(black)
        self.rect = pygame.draw.rect(self.screen, (white), (a, b, c, d), 10)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render(
            'Hello!', True, (255, 0, 0)), (200, 100))
        pygame.display.update()


if __name__ == '__main__':
    pass