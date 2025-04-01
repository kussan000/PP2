import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
ROAD_LEFT, ROAD_RIGHT = 250, 550 
COIN_SIZE = 30
CAR_WIDTH, CAR_HEIGHT = 50, 80
SPEED = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Racer with Coins")

car_img = pygame.image.load("W3/Lab8/01.car_and_coins/car.webp")
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

font = pygame.font.Font(None, 36)

player_x, player_y = WIDTH // 2, HEIGHT - 100

coins = []
coin_spawn_timer = 0
coins_collected = 0

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

    coin_spawn_timer += 1
    if coin_spawn_timer > 50: 
        coin_x = random.randint(ROAD_LEFT, ROAD_RIGHT - COIN_SIZE)
        coins.append([coin_x, 0])
        coin_spawn_timer = 0

    new_coins = []
    for coin in coins:
        coin[1] += SPEED
        if coin[1] > HEIGHT:
            continue  
        
        if (player_x < coin[0] < player_x + CAR_WIDTH) and (player_y < coin[1] < player_y + CAR_HEIGHT):
            coins_collected += 1
            continue 
        
        new_coins.append(coin)
    coins = new_coins


    screen.blit(car_img, (player_x, player_y))

    for coin in coins:
        pygame.draw.circle(screen, GOLD, (coin[0] + COIN_SIZE // 2, coin[1] + COIN_SIZE // 2), COIN_SIZE // 2)

    score_text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(score_text, (WIDTH - 120, 20))

    pygame.display.update()

pygame.quit()
