import pygame
from pygame.math import Vector2
from sys import exit
from random import randint


class Fruit:
    def __init__(self):
        self.position = Vector2(randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1))

    def draw(self):
        fruit_rect = pygame.Rect(int(self.position.x) * CELL_SIZE, int(self.position.y) * CELL_SIZE, CELL_SIZE,
                                 CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 144), fruit_rect)

    def randomize(self):
        while True:
            position = Vector2(randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1))
            if position not in main_game.snake.body:
                self.position = position
                break


class Snake:
    def __init__(self):
        self.body = [Vector2(CELL_NUM // 3, CELL_NUM // 2), Vector2(CELL_NUM // 3 - 1, CELL_NUM // 2),
                     Vector2(CELL_NUM // 3 - 2, CELL_NUM // 2)]
        self.direction = Vector2(1, 0)

    def draw(self):
        for block in self.body:
            snake_rect = pygame.Rect(int(block.x) * CELL_SIZE, int(block.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (133, 100, 122), snake_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy.copy()

    def change_direction(self, direct):
        if direct == MOVE_LEFT:
            if self.direction.x != 1:
                self.direction = MOVE_LEFT
        elif direct == MOVE_RIGHT:
            if self.direction.x != -1:
                self.direction = MOVE_RIGHT
        elif direct == MOVE_UP:
            if self.direction.y != 1:
                self.direction = MOVE_UP
        elif direct == MOVE_DOWN:
            if self.direction.y != -1:
                self.direction = MOVE_DOWN


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.fruit_counter = 0

    def update(self):
        self.snake.change_direction(direction)
        self.snake.move()
        self.teleport()
        self.collision()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()

    def collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.snake.body.insert(-1, self.snake.body[-1])
            self.fruit.randomize()
            self.fruit_counter += 1
        if self.snake.body[0] in self.snake.body[1:]:
            print('game over')
            exit()

    def teleport(self):
        if self.snake.body[0].x < 0:
            self.snake.body[0].x = CELL_NUM - 1
        elif self.snake.body[0].x >= CELL_NUM:
            self.snake.body[0].x = 0
        if self.snake.body[0].y < 0:
            self.snake.body[0].y = CELL_NUM - 1
        elif self.snake.body[0].y >= CELL_NUM:
            self.snake.body[0].y = 0


pygame.init()

FPS = 60
CELL_SIZE = 30
CELL_NUM = 20
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUM, CELL_SIZE * CELL_NUM))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# directions
MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT = Vector2(0, -1), Vector2(0, 1), Vector2(-1, 0), Vector2(1, 0)

main_game = Main()
direction = main_game.snake.direction
pause = False
while True:
    pygame.display.set_caption(str(main_game.fruit_counter))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not pause:
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = MOVE_LEFT
                elif event.key == pygame.K_d:
                    direction = MOVE_RIGHT
                elif event.key == pygame.K_w:
                    direction = MOVE_UP
                elif event.key == pygame.K_s:
                    direction = MOVE_DOWN
                if event.key == pygame.K_p:
                    pause = True
        if pause is True and event.type == pygame.KEYDOWN: #not working
            if event.key == pygame.K_p:
                pause = False


    screen.fill('Lightblue')
    main_game.draw()

    pygame.display.update()
    clock.tick(FPS)
