import pygame
from paddle import Paddle
from Ball import Ball

pygame.init()

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Window
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption('PONG GAME')

# Paddle A
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
# Paddle B
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
# Ball
ball = Ball(WHITE,15,15)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

# Score
scoreA = 0
scoreB = 0
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Pressing the x Key will quit the game
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # adding AI to paddleA
    if (paddleA.rect.y - ball.rect.y) <= 0:
        paddleA.moveDown(4)
    if (paddleA.rect.y - ball.rect.y) >= 0:
        paddleA.moveUp(4)


    # --- Game logic should go here
    all_sprites_list.update()

    # --- ball bouncing against 4 walls
    if ball.rect.x >= 670:
        scoreA += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity = [6, 0]

        paddleA.rect.x = 20
        paddleA.rect.y = 200
        paddleB.rect.x = 670
        paddleB.rect.y = 200
    if ball.rect.x <= 20:
        scoreB += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity = [6, 0]

        paddleA.rect.x = 20
        paddleA.rect.y = 200
        paddleB.rect.x = 670
        paddleB.rect.y = 200
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <=0:
        ball.velocity[1] = -ball.velocity[1]

    # --- Collision
    if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
        ball.bounce()

    screen.fill(BLACK)
    pygame.draw.line(screen,WHITE,[349,0],[349,500],5)

    all_sprites_list.draw(screen)

    # Display Score:
    font = pygame.font.Font(None,70)
    text = font.render(str(scoreA),True,WHITE)
    screen.blit(text,(250,10))
    text = font.render(str(scoreB),True,WHITE)
    screen.blit(text,(420,10))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()