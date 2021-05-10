import pygame
import os
import random
import time
import sys
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("shootingstar")
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            sys.exit()
            playing = False
    pygame.display.update()