import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT


def over_screen(screen):

    background = pygame.image.load(path.join(IMG_DIR, 'Fim.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    pygame.mixer.music.stop()

    running = True
    while running:

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                state = QUIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
