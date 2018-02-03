import sys
import time
import random

import pygame

from .packages.ball.ball import Ball
from .packages.env_var.env_var import *
from .packages.geometry import vector

pygame.init()
font = pygame.font.SysFont('Consolas', 50)
screen = pygame.display.set_mode(screen_size, 0)
pygame.display.set_caption('Game')
screen.fill(background)
pygame.display.update()
sw, sh = screen.get_width(), screen.get_height()

still_playing = True
speed = 3
delay = 0.001
random_delay = False


def display_score(score):
    screen.fill(background)
    pygame.draw.rect(screen, colors['gray'], (sw // 2 - 150, sh // 2 - 200, 300, 200), 0)
    text = font.render (str(round(score, 3)), False, colors['red'])
    tw, th = text.get_size()
    screen.blit(text, (sw // 2 - tw // 2, sh // 2 - tw // 2 - 50))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return


while still_playing:
    ball1 = Ball()
    move_vector = vector.vector(randspeed=speed)
    ball1.create(screen, sw // 2, sh // 2,  move_vector)
    start_time = last_random_time = last_move_time = time.time()
    session = True
    while session:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                c = event.unicode.upper()
                if (c == ball1.text):
                    session = False
                    time_taken = time.time() - start_time
                    display_score(time_taken)

        else:
            current_time = time.time()
            if current_time - last_move_time >= delay:
                screen.fill(background)
                ball1.move(screen)
                last_move_time = current_time
            if random_delay and current_time - last_random_time >= random_delay:
                last_random_time = current_time
                ball1.randomize_step (speed)

    if speed < 10:
        speed = speed + 1
    else:
        if not random_delay:
            random_delay = 5
        elif random_delay > 2:
            random_delay = random_delay * 0.8
