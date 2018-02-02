import sys
import pygame
import time
from packages.ball.ball import Ball, vector, point
from packages.env_var.env_var import *

# pygame.init()
# font = pygame.font.SysFont('Consolas', 50)
# screen = pygame.display.set_mode(screen_size, 0)
# pygame.display.set_caption('Game')
# screen.fill(background)
# pygame.display.update()
# still_playing = True

# while still_playing:
#     last_frame_time = time.time()
#     ball = Ball ()
#     session = True
#     while session:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         else:
#             this_time = time.time()
#             if this_time - last_frame_time >= frame_delay:
#                 screen.fill(background)
#                 for id in range (len(balls) - 1, -1, -1):
#                     a = balls[id].fall ()
#                     a
#             if this_time - last_spawn_time >= spawn_delay:
a = vector (randspeed = 20)
print (a)
pygame.quit()
sys.exit()