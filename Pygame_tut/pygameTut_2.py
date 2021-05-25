'''Filling the colors in the screen, Adding title and icon to the window '''
import pygame
# initialize pygame
pygame.init()
# create game window with 800x600 dimension
screen=pygame.display.set_mode((800,800))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

#Infinite loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:   # only exit the window while press close button
            running=False
    # anything we we want to run continuously, that goes into while Loop
    screen.fill((0,175,240)) #screen.fill((Red,Grren,Blue)) value from 0 to 255
    pygame.display.update() # continuously updating screen before running loop again


