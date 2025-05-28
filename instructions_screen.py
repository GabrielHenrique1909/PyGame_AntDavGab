import pygame
from sprites import BotaoPlay2
from config import BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT
from assets import BTN_CLICK_SOUND, MENU_MUSIC, INSTRUCTIONS_IMG

def instructions_screen(screen, assets):
    """
    Tela de instruções do jogo.
    Exibe as instruções e um botão para voltar ao jogo.
    Args:
        screen (pygame.Surface): A superfície onde a tela será desenhada.
        assets (dict): Dicionário contendo os recursos do jogo, como sons e imagens.
    Returns:
        int: O estado do jogo após a interação do usuário.
    """
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(assets[MENU_MUSIC])
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

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
    instructions_img = assets[INSTRUCTIONS_IMG]
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
                        assets[BTN_CLICK_SOUND].play()
                        pygame.mixer.music.stop()
                        state = GAME
                        running = False                

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(instructions_img, instructions_img_rect)
        all_buttons.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state