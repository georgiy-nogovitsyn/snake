import pygame
from pygame.math import Vector2
from sys import exit
from random import randint


class Fruit:
    def __init__(self):
        self.position = Vector2(randint(0, CELL_NUMBER) * CELL_SIZE, randint(0, CELL_NUMBER) * CELL_SIZE)

    def draw(self):
        fruit_rect = pygame.Rect(int(self.position.x), int(self.position.y), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 144), fruit_rect)


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.start_position = Vector2(randint(0, CELL_NUMBER) * CELL_SIZE, randint(0, CELL_NUMBER) * CELL_SIZE)

    def draw(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x) * CELL_SIZE, int(block.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (133, 111, 122), snake_rect)


pygame.init()

FPS = 60
CELL_SIZE = 30
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('Lightblue')
    snake.draw()
    fruit.draw()
    pygame.display.update()
    clock.tick(FPS)
