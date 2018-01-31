import sys
import pygame
import time
from packages.ball.ball import Ball
from packages.env_var.env_var import *

def calc_frame_delay(time):
    h = pygame.display.Info().current_h
    x_in_a_sec = h / time
    return 1 / x_in_a_sec

pygame.init()
font = pygame.font.SysFont('Consolas', 50)
screen = pygame.display.set_mode(screen_size, 0)
pygame.display.set_caption('Game')
screen.fill(background)
pygame.display.update()

while still_playing:
    fall_time = 10
    frame_delay = calc_frame_delay(fall_time)
    spawn_delay = 5
    accelerate_delay = 10
    last_spawn_time = last_accelerate_time = last_frame_time = time.time()
    last_spawn_time -= 5
    ball_list = []
    still_playing = True
    session = True
    while session:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        else:
            this_time = time.time()
            if this_time - last_frame_time >= frame_delay:
                screen.fill(background)
                for id in range (len (ball_list)):
                    res = ball_list[id].fall (screen)
                    if not res:
                        del_id
            if this_time - last_spawn_time >= spawn_delay:


                
