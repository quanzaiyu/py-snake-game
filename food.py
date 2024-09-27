import pygame
import random
from constants import RED, SNAKE_BLOCK, WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.position()

    def position(self):
        self.x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
        self.y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

    def draw(self, window):
        pygame.draw.rect(window, RED, [self.x, self.y, SNAKE_BLOCK, SNAKE_BLOCK])
