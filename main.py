import pygame
from sys import exit

pygame.init()
pygame.display.set_caption('Snake')
game_active = True
FPS = 60
SCREEN = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
chars_words = pygame.font.Font('font/Pixeltype.ttf', 28)
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))
snail_words = ''
snail_says = chars_words.render('Fuck you!', False, 'Black')

snake_surf = pygame.Surface((10,10))
snake_surf.fill('Red')
snake_rect = snake_surf.get_rect(midbottom = (15,15))
scr = 0
counter = 0
counter_t = 0

text_surf = font.render('Learn', True, 'Black')
text_rect = text_surf.get_rect(center = (400, 50))


while True:
    direction = 1
    score = font.render(str(scr), False, (64, 64, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -20

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(mouse_pos):
                player_gravity = -20

        if player_rect.colliderect(snail_rect):
            game_active = False

    if game_active:

        SCREEN.blit(sky_surf, (0, 0))
        SCREEN.blit(ground_surf, (0, 300))
        SCREEN.blit(snail_surf, (snail_rect))

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        SCREEN.blit(player_surf, (player_rect))



        SCREEN.blit(snake_surf, (snake_rect))
        SCREEN.blit(score, (10,10))
        SCREEN.blit(snail_says, (snail_rect.x-30, snail_rect.y-50))

        pygame.draw.rect(SCREEN, '#c0e8ec', text_rect)
        pygame.draw.rect(SCREEN, '#c0e8ec', text_rect, 10)
        snail_rect.x -= 7
        if counter < 13:
            snail_rect.y -= 2
            counter += 1

        elif counter >= 13:
            snail_rect.y += 2
            counter += 1
            if counter >= 26:
                counter = 0
        if snail_rect.left < 0:
            snail_rect.left = 800

        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            scr += 1

        counter_t += 1
        if counter_t == 20:
            player_words = ''
            counter_t = 0



        SCREEN.blit(text_surf, (text_rect))


    else:
        SCREEN.fill('Yellow')

    pygame.display.update()
    clock.tick(FPS)