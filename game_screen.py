import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, QUIT, OVER, EMPTY, BLOCK
from assets import load_assets, BACKGROUND, BLOCO, TIME_FONT
from sprites import Player, Diamante, Tile, Enemy, Xlr8

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    assets = load_assets()
    world_sprites = pygame.sprite.Group()
    MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    ]
    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group() 
    allenemy = pygame.sprite.Group() #Pra impedir a colisão
    all_bullets = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['blocks']=blocks
    groups['enemy'] = allenemy

    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[BLOCO], row, column)
                all_sprites.add(tile)
                blocks.add(tile)
                world_sprites.add(tile)
    
    for i in range(7):
        enemy = Enemy(groups,assets)
        if i == 0:
            enemy.rect.x = 600  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário
        if i == 1:
            enemy.rect.x = 650  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário 
        if i ==2:
            enemy.rect.x = 700  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário 
        if i ==3:
            enemy.rect.x = 750  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário 
        if i ==4:
            enemy.rect.x = 1400  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário 
        if i ==5:
            enemy.rect.x = 1600  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário 
        if i == 6:
            enemy.rect.x = 1000  # Ajuste para longe do player
            enemy.rect.y = 300  # Ajuste conforme necessário                       
        all_sprites.add(enemy)            
        allenemy.add(enemy)            
                
     # Criando o jogador
    player = Player(groups, assets)
    player.rect.x = 100  # Longe do inimigo
    player.rect.y = 300  # Ajuste conforme necessário
    all_sprites.add(player)
    

    PLAYING = 1
    state = PLAYING

    ACELERACAO = 2

    keys_down = {}

    while state == PLAYING:
        clock.tick(FPS)

        colisoes  =  pygame.sprite.spritecollide(player, allenemy, False, pygame.sprite.collide_mask)  
        if len(colisoes)>0:
            state = OVER
        for bullet in all_bullets:   
            #verifica se a bala bateu na parede 
            hits = pygame.sprite.spritecollide(bullet, groups['blocks'], False, pygame.sprite.collide_mask) 
            for colision in hits:
                bullet.kill() 
            #verfica se matou o inimigo    
            hits = pygame.sprite.spritecollide(bullet, groups['enemy'], True, pygame.sprite.collide_mask) 
            for colision in hits:
                bullet.kill()         
        if player.rect.y>700:
            state = OVER        
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
                        if isinstance(player.current_form, Xlr8):
                            player.speedx = -7
                        else:
                            player.speedx -= 2.05
                        player.last_dir = -1
                    if event.key == pygame.K_RIGHT:
                        if isinstance(player.current_form, Xlr8):
                            player.speedx = 7
                        else:
                            player.speedx += 2.05
                        player.last_dir = 1
                    if event.key == pygame.K_UP:
                        player.jump()
                    if event.key == pygame.K_ESCAPE:
                        state = OVER
                    if event.key == pygame.K_SPACE:
                        if isinstance(player.current_form, Diamante):
                            player.current_form.shoot(player, all_sprites, all_bullets, assets)


                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            if player.speedx < 0:
                                player.speedx = 0
                        if event.key == pygame.K_RIGHT:
                            if player.speedx > 0:
                                player.speedx = 0
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros

        player.handle_keys(groups, assets)
        for block in world_sprites:
            block.speedx = -player.speedx

        player.handle_keys(groups, assets)
        player.update()



        background_img = assets[BACKGROUND]
        background_width = background_img.get_width()
  

        offset_x = player.rect.centerx - WIDTH // 2
        offset_y = 0
        
        scroll_x = player.worldx % background_width
        for x in range(-background_width, WIDTH + background_width, background_width):
            window.blit(background_img, (x - scroll_x, 0))

        for sprite in world_sprites:
            sprite.rect.x -= offset_x
        for enemy in allenemy:
            enemy.rect.x -= offset_x
        for bullet in all_bullets:
            bullet.rect.x -= offset_x

        player.rect.centerx = WIDTH // 2

        all_sprites.update()
        
        all_sprites.draw(window)

        # Cronômetro no topo da tela
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        minutes = seconds // 60
        if minutes < 10:
            minutes = '0' + str(int(minutes))
        else:
            minutes = int(minutes)
        seconds = seconds % 60
        if seconds < 10:
            seconds = '0' + str(int(seconds))
        else:
            seconds = int(seconds)
        text_surface = assets[TIME_FONT].render(f"{minutes}:{seconds}", True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state