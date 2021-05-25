'''creating basic window'''
import pygame
# initialize pygame
pygame.init()
# create game window with 800x600 dimension
screen=pygame.display.set_mode((800,800))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:   # only exit the window while press close button
            running=False



