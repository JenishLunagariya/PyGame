''' Adding player_change and its affects on spaceships via keyborad input'''
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
player_change=0

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change -= 0.3     # moves left from original/last position
            if event.key == pygame.K_RIGHT:
                player_change += 0.3     # moves right from original/last position
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    # anything we we want to run continuously, that goes into while Loop
    playerX+=player_change
    player(playerX,playerY)
    pygame.display.update()


