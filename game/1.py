import pygame
import time
import random
import sys

pygame.init()
window = pygame.display.set_mode((610, 610))
pygame.display.set_caption('3 in a row')

width = heigth = 50
blue = (0, 0, 255)
red = (255, 0, 0)
yello = (255, 255, 0)
list_1 = [red, ]
margin = 5
start = True
while start:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    for col in range(11):
        for row in range (11):
            x = col * width + (col + 1) * margin
            y = row * heigth + (row + 1) * margin
            pygame.draw.rect(window, red, (x, y, width, heigth))
    pygame.display.update()
pygame.quit()