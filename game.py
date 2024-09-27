import pygame
from constants import *
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(u"贪吃蛇游戏")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("simhei", 50)  # 使用中文字体
        self.difficulty = None
        self.select_difficulty()

    def select_difficulty(self):
        selecting = True
        while selecting:
            self.window.fill(BLACK)
            title = self.font.render(u"选择难度", True, WHITE)
            easy = self.font.render(u"1. 简单", True, WHITE)
            medium = self.font.render(u"2. 中等", True, WHITE)
            hard = self.font.render(u"3. 困难", True, WHITE)
            
            self.window.blit(title, [WIDTH/2 - 100, HEIGHT/4])
            self.window.blit(easy, [WIDTH/2 - 100, HEIGHT/2 - 50])
            self.window.blit(medium, [WIDTH/2 - 100, HEIGHT/2])
            self.window.blit(hard, [WIDTH/2 - 100, HEIGHT/2 + 50])
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.difficulty = EASY
                        selecting = False
                    elif event.key == pygame.K_2:
                        self.difficulty = MEDIUM
                        selecting = False
                    elif event.key == pygame.K_3:
                        self.difficulty = HARD
                        selecting = False
        
        self.reset_game()

    def reset_game(self):
        self.snake = Snake(WIDTH / 2, HEIGHT / 2)
        self.food = Food()
        self.game_over = False
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.dx = -SNAKE_BLOCK
                    self.snake.dy = 0
                elif event.key == pygame.K_RIGHT:
                    self.snake.dx = SNAKE_BLOCK
                    self.snake.dy = 0
                elif event.key == pygame.K_UP:
                    self.snake.dy = -SNAKE_BLOCK
                    self.snake.dx = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.dy = SNAKE_BLOCK
                    self.snake.dx = 0
        return True

    def update(self):
        self.snake.move()
        if self.snake.x >= WIDTH or self.snake.x < 0 or self.snake.y >= HEIGHT or self.snake.y < 0:
            self.game_over = True
        if self.snake.check_collision():
            self.game_over = True
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.grow()
            self.food.position()
            self.score += 1

    def draw(self):
        self.window.fill(BLACK)
        self.snake.draw(self.window)
        self.food.draw(self.window)
        score_text = self.font.render(u"得分: {}".format(self.score), True, WHITE)
        self.window.blit(score_text, [10, 10])
        pygame.display.update()

    def show_game_over(self):
        self.window.fill(BLACK)
        game_over_text = self.font.render(u"游戏结束!", True, RED)
        score_text = self.font.render(u"最终得分: {}".format(self.score), True, WHITE)
        restart_text = self.font.render(u"按R重新开始，按Q退出", True, WHITE)
        self.window.blit(game_over_text, [WIDTH/2 - 100, HEIGHT/3])
        self.window.blit(score_text, [WIDTH/2 - 100, HEIGHT/2])
        self.window.blit(restart_text, [WIDTH/2 - 150, HEIGHT*2/3])
        pygame.display.update()

    def run(self):
        running = True
        while running:
            if not self.game_over:
                running = self.handle_events()
                self.update()
                self.draw()
            else:
                self.show_game_over()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                        if event.key == pygame.K_r:
                            self.select_difficulty()  # 重新选择难度
            self.clock.tick(self.difficulty)
        pygame.quit()
