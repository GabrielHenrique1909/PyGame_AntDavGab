import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, QUIT, OVER, EMPTY, BLOCK
from assets import load_assets, BACKGROUND, BLOCO
from sprites import Ben, Idle_Right, Tile

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    ]
    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()  #Pra impedir a colisão
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['blocks']=blocks

    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[BLOCO], row, column)
                all_sprites.add(tile)
                blocks.add(tile)
     # Criando o jogador
    player = Ben(groups, assets)
    all_sprites.add(player)

    PLAYING = 1
    state = PLAYING

    ACELERACAO = 2

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
                    if event.key == pygame.K_UP:
                        player.jump()
                    if event.key == pygame.K_ESCAPE:
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