import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Paint Program')

brush_color = (0, 0, 0)
background_color = (255, 255, 255)
brush_size = 5
clock = pygame.time.Clock()
drawing = False
mode = 'draw'

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

canvas = pygame.Surface((600, 400))
canvas.fill(background_color)

def draw_shape(surface, mode, pos1, pos2):
    if mode == 'rect':
        pygame.draw.rect(surface, brush_color, (pos1[0], pos1[1], pos2[0] - pos1[0], pos2[1] - pos1[1]), brush_size)
    elif mode == 'circle':
        radius = int(((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)**0.5)
        pygame.draw.circle(surface, brush_color, pos1, radius, brush_size)

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
            if mode == 'draw':
                pygame.draw.circle(canvas, brush_color, start_pos, brush_size)
            elif mode == 'eraser':
                pygame.draw.circle(canvas, background_color, start_pos, brush_size)
            elif mode in ['rect', 'circle']:
                draw_shape(canvas, mode, start_pos, end_pos)

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'draw':
                pygame.draw.circle(canvas, brush_color, pygame.mouse.get_pos(), brush_size)
            elif mode == 'eraser':
                pygame.draw.circle(canvas, background_color, pygame.mouse.get_pos(), brush_size)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rect'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_d:
                mode = 'draw'

    button_width = 50
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (i * (button_width + 5), 0, button_width, 30))
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] in range(i * (button_width + 5), (i + 1) * (button_width + 5)):
            brush_color = color

    pygame.display.update()
    clock.tick(60)
