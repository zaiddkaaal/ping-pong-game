import pygame 
from random import *
pygame.init()

Game = pygame.display.set_mode((600, 480))
pygame.display.set_caption("pingpong game")

bg_img = pygame.image.load("bg.png").convert()
player1_img = pygame.image.load("player.png")
player2_img = pygame.image.load("player.png")
ball_img = pygame.image.load("ball.png")

player1_x = 0
player1_y = 240
player1_speed = 5
player1_score = 0


player2_x = 540
player2_y = 240
player2_speed = 5 
player2_score = 0

ball_speed = 3
ball_x = 300
ball_y = 240
ball_dx = 0
ball_dy = 0

waiting = True 
timer_start = pygame.time.get_ticks() 

runing = True
clock = pygame.time.Clock()

score_font = pygame.font.SysFont("Arial", 32, bold=True)
white = (255, 255, 255)

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    
    current_time = pygame.time.get_ticks()

    if not waiting:
        ball_x += ball_dx
        ball_y += ball_dy
    else:
        if current_time - timer_start >= 2000:
            waiting = False
            ball_dx = ball_speed * choice([1, -1])
            ball_dy = ball_speed * choice([1, -1])

    if ball_y <= 0 or ball_y >= 425:
        ball_dy *= -1

    player1_rect = pygame.Rect(player1_x, player1_y, 20, 100)
    player2_rect = pygame.Rect(player2_x, player2_y, 20, 100)
    ball_rect = pygame.Rect(ball_x, ball_y, 20, 20)

    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
        ball_dx *= -1

    if ball_x < 0 :
        ball_x, ball_y = 300, 240
        ball_dx, ball_dy = 0, 0
        waiting = True
        timer_start = pygame.time.get_ticks()
        player1_score += 1
    if ball_x > 600:
        ball_x, ball_y = 300, 240
        ball_dx, ball_dy = 0, 0
        waiting = True
        timer_start = pygame.time.get_ticks()
        player2_score += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player1_y >= 0:
            player1_y -= player1_speed
    if keys[pygame.K_s]:
        if player1_y <= 400:
            player1_y += player1_speed
            
    if keys[pygame.K_UP]:
        if player2_y > 0:
            player2_y -= player2_speed
    if keys[pygame.K_DOWN]:
        if player2_y < 400:
            player2_y += player2_speed

    Game.blit(bg_img, (0, 0))
    Game.blit(player1_img, (player1_x, player1_y))
    Game.blit(player2_img, (player2_x, player2_y))
    Game.blit(ball_img, (ball_x, ball_y)) 
    p1_text = score_font.render(f"Score: {player1_score}", True, white)
    p2_text = score_font.render(f"Score: {player2_score}", True, white)
    Game.blit(p1_text, (450, 20))
    Game.blit(p2_text, (50, 20))
    pygame.display.update()
    clock.tick(60)

pygame.quit()