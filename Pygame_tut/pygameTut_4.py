''' KeyBoard Input, its identification and its affects on player object'''
import pygame
# initialize pygame
pygame.init()
# create game window with 800x600 dimension
screen=pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Player
playerimg=pygame.image.load('space-invaders.png').convert_alpha()
playerimg=pygame.transform.scale(playerimg,(40,40))
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerimg,(x,y)) # blit=draw , require two value:(player image, its cordinate)

# Infinite loop
running=True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN: # KEYDOWN checks whether any key pressed from keyboard or not
            print('Other key is pressed!')
            if event.key == pygame.K_LEFT:
                print('Left key is pressed!')
            if event.key == pygame.K_RIGHT:
                print('Right key is pressed!')
        if event.type == pygame.KEYUP: # KEYUP checks whether key is released or not
            print('Other key released!')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('Key released!')

    player(playerX,playerY)
    pygame.display.update()


