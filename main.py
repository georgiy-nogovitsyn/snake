import pygame
from pygame.math import Vector2
from sys import exit
from random import randint


class Fruit:
    def __init__(self):
        self.position = Vector2(randint(0, CELL_NUMBER - 1), randint(0, CELL_NUMBER - 1))

    def draw(self):
        fruit_rect = pygame.Rect(int(self.position.x) * CELL_SIZE, int(self.position.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 144), fruit_rect)



class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 1)

    def draw(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x) * CELL_SIZE, int(block.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (133, 100, 122), snake_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy.copy()



class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move()
        self.collision()
        self.teleport()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()

    def collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.snake.body.insert(-1, self.snake.body[-1])
            self.fruit = Fruit()
        if self.snake.body[0] in self.snake.body[1:]:
            print('game over')
            exit()

    def teleport(self):
        if self.snake.body[0].x < 0:
            self.snake.body[0].x = CELL_NUMBER - 1
        elif self.snake.body[0].x > CELL_NUMBER:
            self.snake.body[0].x = 0
        if self.snake.body[0].y < 0:
            self.snake.body[0].y = CELL_NUMBER - 1
        elif self.snake.body[0].y > CELL_NUMBER:
            self.snake.body[0].y = 0



pygame.init()

FPS = 60
CELL_SIZE = 30
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# directions
move_up, move_down, move_left, move_right = Vector2(0, -1), Vector2(0, 1), Vector2(-1, 0), Vector2(1, 0)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_d and main_game.snake.direction != move_left:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            elif event.key == pygame.K_w and main_game.snake.direction != move_down:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_s and main_game.snake.direction != move_up:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

    screen.fill('Lightblue')
    main_game.draw()

    pygame.display.update()
    clock.tick(FPS)
