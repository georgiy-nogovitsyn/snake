import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('Snake')

FPS = 60
SCREEN = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
chars_words = pygame.font.Font('font/Pixeltype.ttf', 28)
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_words = ''
player_says = font.render(player_words, False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

snake_surf = pygame.Surface((10,10))
snake_surf.fill('Red')
snake_rect = snake_surf.get_rect(midbottom = (15,15))
scr = 0
counter = 0
counter_t = 0
text_surf = font.render('Snake game', False, 'White')
text_rect = text_surf.get_rect(midright = (player_rect.x, player_rect.y))
while True:

    player_says = font.render(player_words, False, 'Black')

    score = font.render(str(scr), False, 'Black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    SCREEN.blit(sky_surf, (0, 0))
    SCREEN.blit(ground_surf, (0, 300))
    SCREEN.blit(snail_surf, (snail_rect))
    SCREEN.blit(player_surf, (player_rect))
    SCREEN.blit(snake_surf, (snake_rect))
    SCREEN.blit(score, (10,10))
    SCREEN.blit(player_says, (text_rect))
    snake_rect.x += 1
    snail_rect.x -= 4
    if counter < 13:
        snail_rect.y -= 4
        counter += 1

    elif counter >= 13:
        snail_rect.y += 4
        counter += 1
        if counter >= 26:
            counter = 0
    if snail_rect.left < 0:
        snail_rect.left = 800

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        player_words = 'Ouch'
        scr += 1

    counter_t += 1
    if counter_t == 20:
        player_words = ''
        counter_t = 0



    SCREEN.blit(text_surf, (325, 100))
    pygame.display.update()
    clock.tick(FPS)
