import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, OVER, INSTRUCTIONS
from init_screen import init_screen
from game_screen import game_screen
from over_screen import over_screen
from instructions_screen import instructions_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Márcio 10')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == INSTRUCTIONS:
        state = instructions_screen(window)
    elif state == OVER:
        state = over_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
