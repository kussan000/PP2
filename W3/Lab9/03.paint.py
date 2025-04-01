import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Paint Program')

brush_color = (0, 0, 0)
background_color = (255, 255, 255)
brush_size = 3
clock = pygame.time.Clock()
drawing = False
mode = 'draw'
canvas = pygame.Surface((600, 400))
canvas.fill(background_color)

def draw_shape(surface, mode, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    if mode == 'square':
        side = min(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, brush_color, (x1, y1, side, side), brush_size)
    elif mode == 'right_triangle':
        pygame.draw.polygon(surface, brush_color, [(x1, y1), (x2, y2), (x1, y2)], brush_size)
    elif mode == 'equilateral_triangle':
        height = abs(y2 - y1)
        width = height * (3 ** 0.5) / 2
        pygame.draw.polygon(surface, brush_color, [(x1, y2), (x1 + width, y1), (x1 - width, y1)], brush_size)
    elif mode == 'rhombus':
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        pygame.draw.polygon(surface, brush_color, [(x1, y1 - height // 2), (x1 + width // 2, y1),
                                                   (x1, y1 + height // 2), (x1 - width // 2, y1)], brush_size)

while True:
    screen.fill(background_color)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            draw_shape(canvas, mode, start_pos, end_pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_t:
                mode = 'right_triangle'
            elif event.key == pygame.K_e:
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_r:
                mode = 'rhombus'
    
    pygame.display.update()
    clock.tick(60)
