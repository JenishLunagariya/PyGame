''' creating Bullet and adding key action to fire bullet(ONLY ONE TIME)
     PROBLEM: bulletX is changing with playerX_change'''
import pygame
import random
# initialize pygame
pygame.init()
screen=pygame.display.set_mode((800,600))

# Background
background=pygame.image.load('spaceBG.png').convert_alpha()
background=pygame.transform.scale(background,(800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)


# Enemy
enemyimg=pygame.image.load('alien.png').convert_alpha()
enemyimg=pygame.transform.scale(enemyimg,(40,40))
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change=0.3
enemyY_change=20

# Player
playerimg=pygame.image.load('space-invaders.png').convert_alpha()
playerimg=pygame.transform.scale(playerimg,(40,40))
playerX = 370
playerY = 480
player_change=0

# Bullet
# bullet_state : ready means we can't see bullet
# bullet_state : fire means bullet is already moving
bulletimg = pygame.image.load('bullet.png').convert_alpha()
bulletimg = pygame.transform.scale(bulletimg,(20,20))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = 'ready'

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemyimg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+10,y+10))

# Infinite Game loop
running=True
while running:
    screen.fill((0, 0, 0))
    # Background image infinite loop
    '''After adding background in while loop, movement of player and enemy might get slower due to load on while loop.
        In that case, You acn increase the speed of both player_change and enemy_change'''
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change -= 0.3
            if event.key == pygame.K_RIGHT:
                player_change += 0.3
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0


    # Boundaries for spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 757.2990:
        playerX = 757.2990
    playerX+=player_change
    player(playerX,playerY)

    # Boundaries for enemy
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 757.2990:
        enemyX_change = -0.3
        enemyY += enemyY_change
    enemyX+=enemyX_change
    enemy(enemyX,enemyY)

    # Bullet movement
    if bullet_state == 'fire':
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

    pygame.display.update()


