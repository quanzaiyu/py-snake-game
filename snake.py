import pygame
from constants import GREEN, BLUE, SNAKE_BLOCK, WIDTH, HEIGHT

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.body = []
        self.length = 1

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # 处理边界穿越
        if self.x >= WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH - SNAKE_BLOCK
        if self.y >= HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT - SNAKE_BLOCK

        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, window):
        for i, segment in enumerate(self.body):
            if i == len(self.body) - 1:  # 蛇头
                pygame.draw.rect(window, BLUE, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])
            else:  # 蛇身
                pygame.draw.rect(window, GREEN, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def grow(self):
        self.length += 1

    def check_collision(self):
        return any(segment == [self.x, self.y] for segment in self.body[:-1])
