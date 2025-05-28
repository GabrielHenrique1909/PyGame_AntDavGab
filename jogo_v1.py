import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, OVER, INSTRUCTIONS, WIN
from init_screen import init_screen
from game_screen import game_screen
from over_screen import over_screen
from win_screen import win_screen
from instructions_screen import instructions_screen
from assets import load_assets

# ===== Inicialização do PyGame =====
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ben 10')

# ----- Carrega os assets
assets = load_assets()

player_final_time = None # Variável para armazenar o tempo do jogador

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window, assets)
        player_final_time = None # Reseta o tempo ao voltar para a tela inicial
    elif state == GAME:
        game_result = game_screen(window, assets) # game_screen agora pode retornar uma tupla
        if isinstance(game_result, tuple) and len(game_result) == 2:
            state, time_val = game_result
            if state == WIN:
                player_final_time = time_val # Armazena o tempo se o jogador venceu
            else:
                player_final_time = None # Garante que não há tempo se não for vitória
        else: 
            state = game_result
            player_final_time = None
    elif state == INSTRUCTIONS:
        state = instructions_screen(window, assets)
        player_final_time = None # Reseta o tempo
    elif state == WIN:
        # Passa o tempo do jogador para a tela de vitória
        state = win_screen(window, player_final_time, assets)     
    elif state == OVER:
        state = over_screen(window, assets)
        player_final_time = None # Reseta o tempo em game over

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
