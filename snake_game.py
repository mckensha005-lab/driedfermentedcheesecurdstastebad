import pygame
import time
import random

# Initialize pygame
game_speed = 10  # Initial game speed
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0) 

# Game window size
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Snake parameters
snake_block = 10
snake_speed = game_speed
snake_list = []
snake_length = 1

# Initial position
snake_x = width // 2
snake_y = height // 2

def game_loop():
    global snake_length, snake_x, snake_y
    game_over = False
    game_close = False

    # Initial movement direction
    x_change = 0
    y_change = 0

    while not game_over:
        while game_close:
            screen.fill(black)
            font = pygame.font.SysFont(None, 35)
            msg = font.render('You Lost! Press Q-Quit or C-Play Again', True, red)
            screen.blit(msg, (width / 6, height / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()  # Restart game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Update snake position
        snake_x += x_change
        snake_y += y_change

        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            game_close = True

        # Drawing the snake
        screen.fill(black)
        pygame.draw.rect(screen, green, [snake_x, snake_y, snake_block, snake_block])
        snake_list.append((snake_x, snake_y))
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Draw the complete snake
        for x in snake_list[:-1]:
            pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])

        pygame.display.update()
        time.sleep(1 / snake_speed)  # Control game speed

    pygame.quit()

game_loop()