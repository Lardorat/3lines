import pygame
import time
import random
import sys

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption('3 in a row')

widht = heigth = 50
red = (255, 0, 0)
start = True
while start:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    pygame.draw.rect(window, red, (0, 0, widht, heigth))
    pygame.display.update()
pygame.quit()