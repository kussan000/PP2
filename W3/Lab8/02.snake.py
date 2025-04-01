import pygame
import random

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

snake_size = 20
snake_speed = 10
grid_size = 20

font = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()

snake_positions = [(100, 100), (80, 100), (60, 100)]
snake_direction = 'RIGHT'
score = 0
level = 1
speed = 10

def generate_food():
    food_x = random.randrange(0, screen_width, grid_size)
    food_y = random.randrange(0, screen_height, grid_size)
    
    while (food_x, food_y) in snake_positions:
        food_x = random.randrange(0, screen_width, grid_size)
        food_y = random.randrange(0, screen_height, grid_size)
    
    return food_x, food_y

def increase_level():
    global level, speed
    if score >= level * 3:
        level += 1
        speed += 2

def game_over():
    global score
    game_over_text = font.render("Game Over! Press Q to Quit or R to Restart", True, RED)
    screen.blit(game_over_text, (screen_width / 6, screen_height / 3))
    pygame.display.update()

def game_loop():
    global score, level, snake_positions, snake_direction

    food_x, food_y = generate_food()

    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'
                elif event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_q:
                    game_running = False
                elif event.key == pygame.K_r:
                    game_loop()

        head_x, head_y = snake_positions[0]
        if snake_direction == 'LEFT':
            head_x -= grid_size
        elif snake_direction == 'RIGHT':
            head_x += grid_size
        elif snake_direction == 'UP':
            head_y -= grid_size
        elif snake_direction == 'DOWN':
            head_y += grid_size

        if head_x < 0 or head_x >= screen_width or head_y < 0 or head_y >= screen_height:
            game_over()
            break

        snake_positions = [(head_x, head_y)] + snake_positions[:-1]

        if (head_x, head_y) in snake_positions[1:]:
            game_over()
            break

        if head_x == food_x and head_y == food_y:
            food_x, food_y = generate_food()
            snake_positions.append(snake_positions[-1])
            score += 1
            increase_level()

        screen.fill(BLACK)

        for segment in snake_positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_size, snake_size))

        pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, snake_size, snake_size))

        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (screen_width - 150, 10))
        screen.blit(level_text, (screen_width - 150, 40))

        pygame.display.update()

        clock.tick(speed)

    pygame.quit()

game_loop()
