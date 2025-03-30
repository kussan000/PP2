import pygame
import time
import math

pygame.init()

clock_face = pygame.image.load("W3/Lab7/01.images/clock.png")
left_hand = pygame.image.load("W3/Lab7/01.images/leftarm.png")
right_hand = pygame.image.load("W3/Lab7/01.images/rightarm.png")

WIDTH, HEIGHT = clock_face.get_size()
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=pos).center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = -((minutes % 60) * 6) 
    second_angle = -((seconds % 60) * 6)  
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    blit_rotate_center(screen, right_hand, CENTER, minute_angle)
    blit_rotate_center(screen, left_hand, CENTER, second_angle)
    
    pygame.display.flip()
    
    pygame.time.delay(1000 // 60) 

pygame.quit()
