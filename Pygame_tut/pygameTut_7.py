'''creating enemy at random places within limited screen area'''
import pygame
import random
# initialize pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Enemy
enemyimg=pygame.image.load('alien.png').convert_alpha()
enemyimg=pygame.transform.scale(enemyimg,(40,40))
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemy_change=0


# Player
playerimg=pygame.image.load('space-invaders.png').convert_alpha()
playerimg=pygame.transform.scale(playerimg,(40,40))
playerX = 370
playerY = 480
player_change=0

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

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
    if playerX < 0:
        playerX = 0
    elif playerX > 757.2990:
        playerX = 757.2990
    else:
        playerX+=player_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()


