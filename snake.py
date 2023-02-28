import pygame
from pygame.math import Vector2
from sys import exit
from random import randint

class Fruit:
    def __init__(self):
        self.fruit_position = Vector2(randint(1, CELL_NUMBER), randint(1, CELL_NUMBER))

    def draw_fruit(self):
        self.fruit_rect = pygame.Rect(self.fruit_position, CELL_SIZE, CELL_SIZE, pygame.Color('Green'))

pygame.init()

FPS = 60
CELL_SIZE = 30
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()
fruit = Fruit()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('Lightblue')

    screen.blit(fruit.)


    pygame.display.update()
    clock.tick(FPS)


