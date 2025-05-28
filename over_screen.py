import pygame
from sprites import BotaoRestart
from config import BLACK, FPS, GAME, QUIT
from assets import BTN_CLICK_SOUND, FIM

def over_screen(screen, assets):
    """
    Tela de Game Over do jogo.
    Exibe a tela de Game Over e permite que o jogador reinicie o jogo.
    Args:
        screen (pygame.Surface): A superfície onde a tela será desenhada.
        assets (dict): Dicionário contendo os recursos do jogo, como sons e imagens.
    Returns:
        int: O estado do jogo após a interação do usuário.
    """
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    # Criando botoes
    all_buttons = pygame.sprite.Group()
    x = 592
    y = 322
    # Criando o botão restart
    botaorestart = BotaoRestart(assets)
    botaorestart.rect.x = x
    botaorestart.rect.centery = y
    all_buttons.add(botaorestart)
    # Carrega o fundo da tela final
    gameover = assets[FIM]
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
                        assets[BTN_CLICK_SOUND].play()
                        state = GAME
                        running = False    

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(gameover, gameover_rect)
        all_buttons.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
