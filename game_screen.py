import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, QUIT, OVER
from assets import load_assets, BACKGROUND
from sprites import Ben, Idle_Right

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

     # Criando o jogador
    player = Ben(groups, assets)
    all_sprites.add(player)

    PLAYING = 1
    state = PLAYING

    keys_down = {}

    while state == PLAYING:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 5
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 5
                    if event.key == pygame.K_SPACE:
                        state = OVER

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 5
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 5

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state