import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    tela_de_inicio = pygame.image.load(path.join(IMG_DIR, 'teladeinicio.jpg')).convert()
    tela_de_inicio = pygame.transform.scale(tela_de_inicio, (WIDTH, HEIGHT))
    tela_de_inicio_rect = tela_de_inicio.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_de_inicio, tela_de_inicio_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state