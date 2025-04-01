import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
ROAD_LEFT, ROAD_RIGHT = 250, 550  
CAR_WIDTH, CAR_HEIGHT = 50, 80
SPEED = 5
ENEMY_SPEED = 3 
COIN_SPEED_BOOST_THRESHOLD = 10  
COIN_SPEED_REDUCTION = 2 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Racer with Coins")

car_img = pygame.image.load("W3/Lab9/01.car_and_coins/car.webp")
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))
enemy_img = pygame.image.load("W3/Lab9/01.car_and_coins/enemy.jpg")
enemy_img = pygame.transform.scale(enemy_img, (CAR_WIDTH, CAR_HEIGHT))

font = pygame.font.Font(None, 36)

player_x, player_y = WIDTH // 2, HEIGHT - 100

coins = []
coin_spawn_timer = 0
coins_collected = 0

enemy_x, enemy_y = random.randint(ROAD_LEFT, ROAD_RIGHT - CAR_WIDTH), -100

running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > ROAD_LEFT:
        player_x -= SPEED
    if keys[pygame.K_RIGHT] and player_x < ROAD_RIGHT - CAR_WIDTH:
        player_x += SPEED

    ENEMY_SPEED = 3 + (coins_collected // COIN_SPEED_BOOST_THRESHOLD)
    SPEED = max(3, 5 - (coins_collected // 40) * COIN_SPEED_REDUCTION)
    
    enemy_y += ENEMY_SPEED
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(ROAD_LEFT, ROAD_RIGHT - CAR_WIDTH)

    if (player_x < enemy_x + CAR_WIDTH and player_x + CAR_WIDTH > enemy_x and
        player_y < enemy_y + CAR_HEIGHT and player_y + CAR_HEIGHT > enemy_y):
        screen.fill(RED)
        game_over_text = font.render("YOU LOST! Restarting...", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        coins_collected = 0
        player_x, player_y = WIDTH // 2, HEIGHT - 100
        enemy_x, enemy_y = random.randint(ROAD_LEFT, ROAD_RIGHT - CAR_WIDTH), -100
        coins = []

    coin_spawn_timer += 1
    if coin_spawn_timer > 50:
        coin_x = random.randint(ROAD_LEFT, ROAD_RIGHT - 30)
        coin_weight = random.choice([1, 2, 5])
        coin_radius = 5 + coin_weight * 5
        coins.append([coin_x, 0, coin_weight, coin_radius])
        coin_spawn_timer = 0

    new_coins = []
    for coin in coins:
        coin[1] += SPEED
        if coin[1] > HEIGHT:
            continue
        
        if (player_x < coin[0] < player_x + CAR_WIDTH) and (player_y < coin[1] < player_y + CAR_HEIGHT):
            coins_collected += coin[2]  
            continue
        
        new_coins.append(coin)
    coins = new_coins

    screen.blit(car_img, (player_x, player_y))

    for coin in coins:
        pygame.draw.circle(screen, GOLD, (coin[0] + coin[3], coin[1] + coin[3]), coin[3])
    
    screen.blit(enemy_img, (enemy_x, enemy_y))

    score_text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(score_text, (WIDTH - 120, 20))

    pygame.display.update()

pygame.quit()
