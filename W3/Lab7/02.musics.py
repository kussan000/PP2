import pygame
import os

pygame.init()
pygame.mixer.init()

music_files = [
    "W3/Lab7/02.musics/Ernar Amandyq - Meni kut.mp3",
    "W3/Lab7/02.musics/HammAli & Navai - Ты Позвонишь Ночью.mp3",
    "W3/Lab7/02.musics/Rvmvn_Tvoya_dusha-new.mp3"
]

icons = {
    "play": "W3/Lab7/02.music_elements/play.png",
    "pause": "W3/Lab7/02.music_elements/pause.png",
    "next": "W3/Lab7/02.music_elements/next.png",
    "back": "W3/Lab7/02.music_elements/back.png"
}

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

def load_scaled_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)

ICON_SIZE = (80, 80)

images = {key: load_scaled_image(path, ICON_SIZE) for key, path in icons.items()}

current_track = 0
playing = False

def play_music():
    global playing
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()
    playing = True

running = True
while running:
    screen.fill((50, 50, 50))
    
    if playing:
        screen.blit(images["pause"], (160, 100))
    else:
        screen.blit(images["play"], (160, 100))
    
    screen.blit(images["back"], (50, 100))
    screen.blit(images["next"], (270, 100))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT: 
                current_track = (current_track + 1) % len(music_files)
                play_music()
            elif event.key == pygame.K_LEFT: 
                current_track = (current_track - 1) % len(music_files)
                play_music()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                playing = False

pygame.quit()
