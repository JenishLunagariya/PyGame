'''Score showing on screen'''
import pygame
import random
import math
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
'''belpw list and appeanding is important'''
enemyimg2 = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg = pygame.image.load('alien.png').convert_alpha()
    enemyimg2.append(pygame.transform.scale(enemyimg,(40,40)))
    enemyX.append(random.randint(0,757))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(20)

# Player
playerimg=pygame.image.load('space-invaders.png').convert_alpha()
playerimg=pygame.transform.scale(playerimg,(40,40))
playerX = 370
playerY = 480
player_change=0

# Bullet
bulletimg = pygame.image.load('bullet.png').convert_alpha()
bulletimg = pygame.transform.scale(bulletimg,(20,20))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)  # 32 is size
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg2[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+10,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2) + math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    else:
        return False

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
            if event.key == pygame.K_UP:
                if bullet_state == 'ready':
                    bulletX = playerX  # This line will stop movemnt of bullet with spaceship movement
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0


    # Boundaries for spaceship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 757.2990:
        playerX = 757.2990
    playerX+=player_change



    '''we put enemy movement and collison inside of for loop to control 6 different enemy '''
    for i in range(num_of_enemies):
        # Boundaries for enemy
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 757.2990:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 757)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i],enemyY[i],i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()


