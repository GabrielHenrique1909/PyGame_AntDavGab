# game_screen.py
import pygame
import os
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, SND_DIR, QUIT, OVER, EMPTY, BLOCK, WIN_BLOCK_TYPE, WIN
from assets import BACKGROUND, BLOCO, TIME_FONT, WIN_BLOCK_IMG, BACKGROUND_MUSIC, JUMP_SOUND, ENEMY_HIT_SOUND, LOSE_SOUND, WIN_SOUND, TRANSFORM_SOUND, DETRANSFORM_SOUND
from sprites import Player, Diamante, Tile, Enemy, Xlr8, Fantasmagorico, StillEnemy
# Importa os estados do player
from sprites import STILL, RUNNING, JUMPING, FALLING, SHOOTING, TRANSFORMING, DYING, IDLE

def game_screen(window, assets):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    pygame.mixer.music.load(os.path.join(SND_DIR, 'background_music.wav'))
    pygame.mixer.music.set_volume(0.65)
    pygame.mixer.music.play(-1)

    world_sprites = pygame.sprite.Group()
    
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
                win_group.add(tile) 
                world_sprites.add(tile)

    #Criação do inimigo que se move            
    enemy = Enemy(groups ,assets)
    enemy.rect.x = 700  # Ajuste para longe do player
    enemy.rect.y = 300  # Ajuste conforme necessário                   
    all_sprites.add(enemy)            
    allenemy.add(enemy)            

    #Criação de todos inimigos parados 
    coordenadasstill = [[780,100],[1140,400],[1540,100],[2000,100],[2300,100],[2610,100],[2950,100],[3230,100],[3500,100],[4000,100]]
    for coordenada in coordenadasstill:
        x = coordenada[0]
        y = coordenada[1]
        still = StillEnemy(x,y,groups,assets)
        all_sprites.add(still)            
        allenemy.add(still)
                
     # Criando o jogador
    player = Player(groups, assets) #
    player.rect.x = 100  # Longe do inimigo
    player.rect.y = 300  # Ajuste conforme necessário
    all_sprites.add(player)
    
    PLAYING = 1 # Estado local para o jogo em andamento
    state = PLAYING
    current_total_seconds = 0 # Para armazenar o tempo total em segundos

    keys_down = {}

    while state == PLAYING:
        clock.tick(FPS)

        #Criação de inimigos atrás do personagem de 5 em 5 segundos a partir de 10s corridos
        time_in_seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
        if time_in_seconds % 5 == 0 and time_in_seconds >= 10 and newenemy == False:
            enemy = Enemy(groups ,assets)
            enemy.rect.x = 600  # Ajuste para perto do player
            enemy.rect.y = 300  # Ajuste conforme necessário               
            all_sprites.add(enemy)            
            allenemy.add(enemy) 
            newenemy = True
        if (time_in_seconds + 1) % 5 == 0:
            newenemy = False    

        #Morte se o personagem encostar num inimigo     
        colisoes  =  pygame.sprite.spritecollide(player, allenemy, False, pygame.sprite.collide_mask)  
        if len(colisoes)>0:
            assets[LOSE_SOUND].play()
            state = OVER

        #Analise se o tiro do diamante acertou um inimigo ou um bloco     
        for bullet in all_bullets:   
            hits = pygame.sprite.spritecollide(bullet, groups['blocks'], False, pygame.sprite.collide_mask) 
            if len(hits)>0:
                bullet.kill() 
            hits = pygame.sprite.spritecollide(bullet, groups['enemy'], True, pygame.sprite.collide_mask) 
            if len(hits)>0:
                assets[ENEMY_HIT_SOUND].play()
                bullet.kill()         

        #Morte caso o personagem caia        
        if player.rect.y>700:
            assets[LOSE_SOUND].play()
            state = OVER        
        
        #Vitoria caso o personagem encoste no bloco de win
        colisoes_win  =  pygame.sprite.spritecollide(player, win_group, False, pygame.sprite.collide_mask) # Usar win_group
        if len(colisoes_win)>0:
            assets[WIN_SOUND].play()
            state = WIN

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
                    elif event.key == pygame.K_RIGHT:
                        player.state = RUNNING
                        if isinstance(player.current_form, Xlr8):
                            player.speedx = 7
                        else:
                            player.speedx += 2.05
                        player.last_dir = 1
                    elif event.key == pygame.K_UP:
                        player.jump()
                        assets[JUMP_SOUND].play()
                        player.state = JUMPING
                    elif event.key == pygame.K_ESCAPE:
                        assets[LOSE_SOUND].play()
                        state = OVER
                        player.state = DYING
                    elif event.key == pygame.K_SPACE:
                        if isinstance(player.current_form, Diamante):
                            player.current_form.shoot(player, all_sprites, all_bullets, assets)
                            player.state = SHOOTING
                    elif event.key == pygame.K_w:
                        player.transform(Diamante(groups, assets))
                    elif event.key == pygame.K_a:
                        player.transform(Xlr8(assets))
                    elif event.key == pygame.K_d:
                        player.transform(Fantasmagorico(assets))
                        
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            if player.speedx < 0:
                                player.speedx = 0
                                player.state = IDLE
                        elif event.key == pygame.K_RIGHT:
                            if player.speedx > 0:
                                player.speedx = 0
                                player.state = IDLE
        
        player.handle_keys(groups)
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
    pygame.mixer.music.stop()
    # Agora, FORA do loop, verificamos o estado final e retornamos
    if state == WIN:
        # current_total_seconds foi atualizado no último frame do loop PLAYING
        return state, current_total_seconds
    else: # Para OVER, QUIT, ou qualquer outro estado que encerrou o loop PLAYING
        return state, None