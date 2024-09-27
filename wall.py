import pygame
from constants import GRAY, SNAKE_BLOCK

class Wall:
    def __init__(self, positions):
        self.positions = positions

    def draw(self, window):
        for position in self.positions:
            pygame.draw.rect(window, GRAY, [position[0], position[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def check_collision(self, x, y):
        return any(position == [x, y] for position in self.positions)
