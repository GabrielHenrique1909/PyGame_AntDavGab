import pygame
from sprites import BotaoPlay
from config import BLACK, FPS, QUIT, INSTRUCTIONS
from assets import MENU_MUSIC, BTN_CLICK_SOUND, TELA_DE_INICIO

def init_screen(screen, assets):
    """
    Inicializa a tela de início do jogo.
    Exibe o botão de play e aguarda a interação do usuário.
    Args:
        screen (pygame.Surface): A superfície onde o jogo será desenhado.
        assets (dict): Dicionário contendo os recursos do jogo, como sons e imagens.
    Returns:
        int: O estado do jogo após a interação do usuário.
    """
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    pygame.mixer.music.load(assets[MENU_MUSIC])
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    # Criando botoes
    all_buttons = pygame.sprite.Group()
    x = 30
    y = 90
    
    # Criando o botão play
    botaoplay = BotaoPlay(assets)
    botaoplay.rect.x = x
    botaoplay.rect.centery = y
    all_buttons.add(botaoplay)

    # Carrega o fundo da tela inicial
    tela_de_inicio = assets[TELA_DE_INICIO]
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
                        assets[BTN_CLICK_SOUND].play()
                        pygame.mixer.music.stop()
                        state = INSTRUCTIONS
                        running = False                

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_de_inicio, tela_de_inicio_rect)
        all_buttons.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state