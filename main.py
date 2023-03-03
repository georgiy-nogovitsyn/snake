import pygame
from pygame.math import Vector2
from sys import exit
from random import randint

class Fruit:
    def __init__(self):
        self.position = Vector2(randint(0, CELL_NUMBER - 1) * CELL_SIZE, randint(0, CELL_NUMBER - 1) * CELL_SIZE)


    def draw(self):
        fruit_rect = pygame.Rect(int(self.position.x), int(self.position.y), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 144), fruit_rect)


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.start_position = Vector2(randint(0, CELL_NUMBER) * CELL_SIZE, randint(0, CELL_NUMBER) * CELL_SIZE)
        self.direction = Vector2(0, 1)
        
    def draw(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x) * CELL_SIZE, int(block.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (133, 100, 122), snake_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

pygame.init()

FPS = 60
CELL_SIZE = 30
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == SCREEN_UPDATE:
            snake.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and snake.body[1] + Vector2(1, 0) != snake.body[0]:
                snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_d and snake.body[1] + Vector2(-1, 0) != snake.body[0]:
                snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_w and snake.body[1] + Vector2(0, 1) != snake.body[0]:
                snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_s and snake.body[1] + Vector2(0, -1) != snake.body[0]:
                snake.direction = Vector2(0, 1)

    screen.fill('Lightblue')
    snake.draw()
    fruit.draw()
    pygame.display.update()
    clock.tick(FPS)
