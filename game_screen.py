# game_screen.py
import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, QUIT, OVER, EMPTY, BLOCK, WIN_BLOCK_TYPE, WIN
from assets import load_assets, BACKGROUND, BLOCO, TIME_FONT, WIN_BLOCK_IMG
from sprites import Player, Diamante, Tile, Enemy, Xlr8
# Importa os estados do player
from sprites import STILL, RUNNING, JUMPING, FALLING, SHOOTING, TRANSFORMING, DYING, IDLE

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    assets = load_assets()
    world_sprites = pygame.sprite.Group()
    a1 = [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK] * 5
    
    MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]+[WIN_BLOCK_TYPE],
    [BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK]+[WIN_BLOCK_TYPE],
    ]
    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group() 
    allenemy = pygame.sprite.Group() #Pra impedir a colisão
    all_bullets = pygame.sprite.Group()
    win_group = pygame.sprite.Group() # Renomeado para evitar conflito com a constante WIN

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['blocks']=blocks
    groups['enemy'] = allenemy
    groups['win'] = win_group #

    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[BLOCO], row, column)
                all_sprites.add(tile)
                blocks.add(tile)
                world_sprites.add(tile)
            if tile_type == WIN_BLOCK_TYPE:
                tile = Tile(assets[WIN_BLOCK_IMG], row, column) #
                all_sprites.add(tile)
                win_group.add(tile) #
                world_sprites.add(tile)
    for i in range(1):
        enemy = Enemy(600, groups ,assets)
        if i == 0:
            enemy.rect.x = 600  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário
        # ... (outras posições de inimigos)                    
        all_sprites.add(enemy)            
        allenemy.add(enemy)            
                
     # Criando o jogador
    player = Player(groups, assets) #
    player.rect.x = 100  # Longe do inimigo
    player.rect.y = 300  # Ajuste conforme necessário
    all_sprites.add(player)
    
    PLAYING = 1 # Estado local para o jogo em andamento
    state = PLAYING
    current_total_seconds = 0 # Para armazenar o tempo total em segundos

    ACELERACAO = 2 # Esta constante estava no seu código original, mas não parecia usada nesta função.
                   # A classe Player e Enemy usam uma ACELERACAO definida em sprites.py

    keys_down = {}

    while state == PLAYING:
        clock.tick(FPS)

        colisoes  =  pygame.sprite.spritecollide(player, allenemy, False, pygame.sprite.collide_mask)  
        if len(colisoes)>0:
            state = OVER
        for bullet in all_bullets:   
            hits = pygame.sprite.spritecollide(bullet, groups['blocks'], False, pygame.sprite.collide_mask) 
            for colision in hits:
                bullet.kill() 
            hits = pygame.sprite.spritecollide(bullet, groups['enemy'], True, pygame.sprite.collide_mask) 
            for colision in hits:
                bullet.kill()         
        if player.rect.y>700: #
            state = OVER        
        
        colisoes_win  =  pygame.sprite.spritecollide(player, win_group, False, pygame.sprite.collide_mask) # Usar win_group
        if len(colisoes_win)>0: #
            state = WIN #

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if state == PLAYING: # Só processa eventos de jogo se ainda estiver jogando
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.state = RUNNING
                        if isinstance(player.current_form, Xlr8):
                            player.speedx = -7
                        else:
                            player.speedx -= 2.05
                        player.last_dir = -1
                    if event.key == pygame.K_RIGHT:
                        player.state = RUNNING
                        if isinstance(player.current_form, Xlr8):
                            player.speedx = 7
                        else:
                            player.speedx += 2.05
                        player.last_dir = 1
                    if event.key == pygame.K_UP:
                        player.jump()
                        player.state = JUMPING
                    if event.key == pygame.K_ESCAPE: # Permite sair para OVER (ou poderia ser QUIT)
                        state = OVER
                        player.state = DYING
                    if event.key == pygame.K_SPACE:
                        if isinstance(player.current_form, Diamante):
                            player.current_form.shoot(player, all_sprites, all_bullets, assets)
                            player.state = SHOOTING
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            if player.speedx < 0:
                                player.speedx = 0
                                player.state = IDLE
                        if event.key == pygame.K_RIGHT:
                            if player.speedx > 0:
                                player.speedx = 0
                                player.state = IDLE
        
        player.handle_keys(groups, assets)
        for block_sprite_item in world_sprites: # Renomeado para evitar conflito
            block_sprite_item.speedx = -player.speedx

        player.update() # player.handle_keys já é chamado dentro de player.update() ou deveria ser. Verificar sprites.py.
                        # No seu sprites.py, handle_keys é separado. Manter as duas chamadas se for intencional.

        background_img = assets[BACKGROUND]
        background_width = background_img.get_width()
  
        offset_x = player.rect.centerx - WIDTH // 2
        
        scroll_x = player.worldx % background_width
        for x_pos_bg in range(-background_width, WIDTH + background_width, background_width): # Renomeado para clareza
            window.blit(background_img, (x_pos_bg - scroll_x, 0))

        for sprite_obj in world_sprites: # Renomeado
            sprite_obj.rect.x -= offset_x
        for enemy_obj in allenemy: # Renomeado
            enemy_obj.rect.x -= offset_x
        for bullet_obj in all_bullets: # Renomeado
            bullet_obj.rect.x -= offset_x

        player.rect.centerx = WIDTH // 2
        all_sprites.update()
        all_sprites.draw(window)

        # Cronômetro no topo da tela
        time_in_seconds = (pygame.time.get_ticks() - start_ticks) / 1000 # Variável para o tempo total em segundos
        current_total_seconds = time_in_seconds # Atualiza o tempo que será retornado

        minutes_val = time_in_seconds // 60
        seconds_val = time_in_seconds % 60
        
        minutes_str = f"{int(minutes_val):02d}"
        seconds_str = f"{int(seconds_val):02d}"
        
        text_surface = assets[TIME_FONT].render(f"{minutes_str}:{seconds_str}", True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.update()

    # ----- FIM DO LOOP while state == PLAYING -----

    # Agora, FORA do loop, verificamos o estado final e retornamos
    if state == WIN:
        # current_total_seconds foi atualizado no último frame do loop PLAYING
        return state, current_total_seconds
    else: # Para OVER, QUIT, ou qualquer outro estado que encerrou o loop PLAYING
        return state, None