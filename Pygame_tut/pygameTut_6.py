'''Adding boundaries to the spaceship'''
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
                player_change -= 0.3
            if event.key == pygame.K_RIGHT:
                player_change += 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    # anything we we want to run continuously, that goes into while Loop
    # if x < 0 or x > 757.299, then spaceship wont move beyond that limit
    # for x between 0 and 757.299 spaceship will move accordingly given player_change
    if playerX < 0:
        playerX = 0
    elif playerX > 757.2990:
        playerX = 757.2990
    else:
        playerX+=player_change
        print(playerX)
    player(playerX,playerY)
    pygame.display.update()


