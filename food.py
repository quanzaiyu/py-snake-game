import pygame
import random
from constants import RED, SNAKE_BLOCK, WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position()

    def position(self, wall=None):
        self.x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
        self.y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
        if wall and wall.check_collision(self.x, self.y):
            self.position(wall)  # 递归调用，直到找到不在墙上的位置

    def draw(self, window):
        pygame.draw.rect(window, RED, [self.x, self.y, SNAKE_BLOCK, SNAKE_BLOCK])
