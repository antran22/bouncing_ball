import sys
import time
import random

import pygame

from packages.ball.ball import Ball, point, vector
from packages.env_var.env_var import *
from packages.vector import vector

pygame.init()
font = pygame.font.SysFont('Consolas', 50)
screen = pygame.display.set_mode(screen_size, 0)
pygame.display.set_caption('Game')
screen.fill(background)
pygame.display.update()
still_playing = True
level = 1
while still_playing:
    ball1 = Ball ()
    move_vector = vector.vector (randspeed = level)
    ball1.create (screen, screen.get_width() // 2, screen.get_height() // 2, move_vector)
    last_move_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()
    else:
        current_time = time.time()
        if current_time - last_move_time >= 0.03:
            screen.fill (background)
            ball1.move (screen)
            last_move_time = current_time
