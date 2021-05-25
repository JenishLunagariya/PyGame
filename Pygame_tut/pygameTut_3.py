'''defining the player object as image and its position in window'''
import pygame
# initialize pygame
pygame.init()
# create game window with 800x600 dimension
screen=pygame.display.set_mode((800,600)) #width x height

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Player
playerimg=pygame.image.load('space-invaders.png').convert_alpha() # convert_alpha needed to use transform operation
playerimg=pygame.transform.scale(playerimg,(40,40))  # transform.scale changes size of the image and then display
'''playerX and playerY define where should player appear on the display'''
playerX=370
playerY=480

def player():
    screen.blit(playerimg,(playerX,playerY)) # blit=draw , require two value:(player image, its cordinate)


# Infinite loop
running=True
while running:
    # screen.fill((Red,Grren,Blue)) value from 0 to 255
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:   # only exit the window while press close button
            running=False
    # anything we we want to run continuously, that goes into while Loop
    player()
    pygame.display.update() # continuously updating screen before running loop again


