import pygame
import random
from os import path
from sprites import BotaoPlay2
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT
from assets import load_assets

def instructions_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Criando botoes
    all_buttons = pygame.sprite.Group()
    x = WIDTH-230
    y = HEIGHT-85
    # Criando o botão play
    botaoplay2 = BotaoPlay2(assets)
    botaoplay2.rect.x = x
    botaoplay2.rect.centery = y
    all_buttons.add(botaoplay2)

    # Carrega o fundo da tela inicial
    instructions_img = pygame.image.load(path.join(IMG_DIR, 'instrucoes.jpg')).convert()
    instructions_img = pygame.transform.scale(instructions_img, (WIDTH, HEIGHT))
    instructions_img_rect = instructions_img.get_rect()

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
                for play in all_buttons:
                    if play.rect.collidepoint(event.pos):
                        play.mouse_over(True)
                    else:
                        play.mouse_over(False)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for play in all_buttons:
                    if play.rect.collidepoint(event.pos):
                        state = GAME
                        running = False                

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(instructions_img, instructions_img_rect)
        all_buttons.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state