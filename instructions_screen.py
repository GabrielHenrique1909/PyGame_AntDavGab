import pygame
import os 
from config import WIDTH, HEIGHT, FPS, GAME, QUIT, INSTRUCTIONS, BLACK, WHITE, YELLOW, FNT_DIR
from assets import load_assets, INSTRUCTIONS_IMG, TIME_FONT 

def instructions_screen(screen):

    clock = pygame.time.Clock()
    assets = load_assets()

    instructions_background = assets[INSTRUCTIONS_IMG]

    instructions_lines = [
        # ("COMO JOGAR:", YELLOW), # O título será desenhado separadamente
        # ("", WHITE), 
        ("MOVIMENTO:", YELLOW),
        ("Seta Esquerda: Mover para Esquerda", WHITE),
        ("Seta Direita: Mover para Direita", WHITE),
        ("Seta Cima: Pular", WHITE),
        ("", WHITE),
        ("ACOES:", YELLOW),
        ("Barra de Espaco: Atirar (como Diamante)", WHITE),
        ("", WHITE),
        ("TRANSFORMACOES (Ben 10):", YELLOW),
        ("Tecla W: Transformar em Diamante", WHITE),
        ("Tecla A: Transformar em XLR8 (Mais Rapido)", WHITE),
        ("Tecla D: Transformar em Fantasmagorico (Atravessa Blocos)", WHITE),
        ("Transformacoes duram 3s e tem 3s de recarga.", WHITE),
        ("", WHITE),
        ("OBJETIVO:", YELLOW),
        ("Alcance o portal no final da fase para vencer!", WHITE),
    ]

    title_text = "INSTRUCOES"
    prompt_text_continue = "Pressione ESPACO para comecar!"
    prompt_text_quit = "(Ou ESC para Sair)"

    running = True
    current_state = INSTRUCTIONS 

    # Som de clique (se implementado em assets.py)
    btn_click_sound = assets.get('btn_click_sound') # Usando .get para evitar KeyError

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if btn_click_sound and hasattr(btn_click_sound, 'play'): btn_click_sound.play()
                    current_state = GAME 
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    if btn_click_sound and hasattr(btn_click_sound, 'play'): btn_click_sound.play()
                    current_state = QUIT 
                    running = False

        screen.blit(instructions_background, (0, 0))
        
    return current_state
