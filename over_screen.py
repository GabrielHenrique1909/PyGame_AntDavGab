import pygame
import random
from os import path
from sprites import BotaoRestart
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT
from assets import load_assets

def over_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Criando botoes
    all_buttons = pygame.sprite.Group()
    x = 396
    y = 218
    # Criando o botão restart
    botaorestart = BotaoRestart(assets)
    botaorestart.rect.x = x
    botaorestart.rect.centery = y
    all_buttons.add(botaorestart)
    # Carrega o fundo da tela final
    gameover = pygame.image.load(path.join(IMG_DIR, 'gameover.png')).convert()
    gameover = pygame.transform.scale(gameover, (WIDTH, HEIGHT))
    gameover_rect = gameover.get_rect()
    pygame.mixer.music.stop()

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
            
            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for restart in all_buttons:
                    if restart.rect.collidepoint(event.pos):
                        restart.mouse_over(True)
                    else:
                        restart.mouse_over(False)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for restart in all_buttons:
                    if restart.rect.collidepoint(event.pos):
                        state = GAME
                        running = False    

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(gameover, gameover_rect)
        all_buttons.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
