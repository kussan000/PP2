import pygame 
import time
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("MICKEY MOUSE CLOCK") 

left = pygame.image.load("W3/Lab7/01.images/leftarm.png")
right = pygame.image.load("W3/Lab7/01.images/rightarm.png")
main = pygame.transform.scale(pygame.image.load("W3/Lab7/01.images/clock.png"), (800, 600))

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime()  # Получаем текущее время
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # Углы для минутной и секундной стрелки
    minute_angle = minute * 6 + (second / 60) * 6  
    second_angle = second * 6  
    
    screen.blit(main, (0, 0))  # Фон часов
    
    # Минутная стрелка (правая рука)
    rotated_rightarm = pygame.transform.rotate(
        pygame.transform.scale(right, (800, 600)), -minute_angle
    )
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2 - 30, 600 // 2 - 15))
    screen.blit(rotated_rightarm, rightarmrect)

    # Секундная стрелка (левая рука) — ИСПРАВЛЕНО масштабирование
    rotated_leftarm = pygame.transform.rotate(
        pygame.transform.scale(left, (41, 683)), -second_angle
    )
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2 + 20, 600 // 2 - 18))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(60) 
    
pygame.quit()
