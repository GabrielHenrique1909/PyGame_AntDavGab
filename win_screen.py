import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, INSTRUCTIONS
from assets import load_assets

def win_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Criando botoes
    all_buttons = pygame.sprite.Group()
    x = 30
    y = 90

    # Carrega o fundo da tela inicial
    tela_de_inicio = pygame.image.load(path.join(IMG_DIR, 'victory.png')).convert()
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
                        state = INSTRUCTIONS
                        running = False                

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_de_inicio, tela_de_inicio_rect)
        all_buttons.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state