import pygame
from sys import exit
from random import randint


FPS = 5
WIDTH, HEIGHT = 400, 400
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

snake_surf = pygame.Surface((WIDTH/10, HEIGHT/10))
snake_surf.fill('Yellow')
snake_rect = snake_surf.get_rect(bottomright = (80,80))

direction = 9
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: direction = 0
            elif event.key == pygame.K_a: direction = 1
            elif event.key == pygame.K_w: direction = 2
            elif event.key == pygame.K_s: direction = 3

    if direction == 9:
        pass
    elif direction == 0:
        snake_rect.x += 40
    elif direction == 1:
        snake_rect.x -= 40
    elif direction == 2:
        snake_rect.y -= 40
    elif direction == 3:
        snake_rect.y += 40

    if snake_rect.x > WIDTH:
        snake_rect.x = 0
    elif snake_rect.x < 0:
        snake_rect.x = WIDTH
    if snake_rect.y > HEIGHT:
        snake_rect.y = 0
    elif snake_rect.y < 0:
        snake_rect.y = HEIGHT



    screen.fill('Lightblue')
    screen.blit(snake_surf, snake_rect)






    pygame.display.update()
    clock.tick(FPS)


