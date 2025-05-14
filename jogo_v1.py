import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from game_screen import game_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Márcio 10')

state = INIT
while state != QUIT:
    if state == INIT:
        state = game_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados