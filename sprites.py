import pygame
import time
from config import WIDTH, HEIGHT, BEN_WIDTH, BEN_HEIGHT, TILE_SIZE, OVER
from assets import BEN_IMG, DIAM_IMG, XLR8_IMG, FANT_IMG, DIAM_BULLET, ENEMY_IMG


class Ben:
    def __init__(self, assets):
        self.image = assets[BEN_IMG]

class Diamante:
    def __init__(self, groups ,assets):
        self.image = assets[DIAM_IMG]
        self.last_shot_time = 0
        self.shot_cooldown = 0.5
        self.blocks = groups['blocks']

    def shoot(self, player, all_sprites, all_bullets, assets):
        now = time.time()
        if now - self.last_shot_time < self.shot_cooldown:
            return  # ainda em cooldown, não atira

        x = player.rect.centerx
        y = player.rect.centery
        direction = player.last_dir
        bullet_img = assets[DIAM_BULLET]
        if direction == -1:
            bullet_img = pygame.transform.flip(bullet_img, True, False)
        bullet = Projectile(x, y, direction, bullet_img)
        all_sprites.add(bullet)
        all_bullets.add(bullet)
        self.last_shot_time = now  # registra o último tiro



class Xlr8:
    def __init__(self, assets):
        self.image = assets[XLR8_IMG]

class Fantasmagorico:
    def __init__(self, assets):
        self.image = assets[FANT_IMG]

STILL = 0
JUMPING = 1
FALLING = 2
ACELERACAO = 0.5
JUMP_SIZE = 15

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        self.colided = False
        self.last_dir = 1  # Começa olhando para a direita
        self.last_transform_time = 0  # tempo da última transformação revertida
        self.transform_cooldown = 3  # segundos de espera após transformação
        self.base_form = Ben(assets)
        self.current_form = self.base_form
        self.transform_time = None
        self.image = self.base_form.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.worldx = 0
        self.speedy = 0
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.blocks = groups['blocks']
        self.enemy = groups['enemy']
    
    def handle_keys(self,groups, assets):
        keys = pygame.key.get_pressed()
        if self.colided == False:
            if keys[pygame.K_RIGHT]:
                self.worldx += self.speedx
            if keys[pygame.K_LEFT]:
                self.worldx += self.speedx     
        # Transformações com W, A, D
        if keys[pygame.K_w]:
            self.transform(Diamante(groups, assets))
        elif keys[pygame.K_a]:
            self.transform(Xlr8(assets))
        elif keys[pygame.K_d]:
            self.transform(Fantasmagorico(assets))


    def transform(self, new_form):
        now = time.time()
        # Já está transformado OU ainda está no cooldown
        if self.current_form != self.base_form or now - self.last_transform_time < self.transform_cooldown:
            return  # Bloqueia nova transformação

        self.current_form = new_form
        self.transform_time = now
        self.image = self.current_form.image

    
    def update(self):
        # Reverte após 3 segundo
        if self.current_form != self.base_form and self.transform_time:
            if time.time() - self.transform_time >= 3:
                self.current_form = self.base_form
                self.transform_time = None
                self.image = self.current_form.image
                self.last_transform_time = time.time()  # Começa o cooldown

        self.speedy += ACELERACAO
        if self.speedy > 0:
            self.state = FALLING
            if self.rect.bottom == HEIGHT:
                self.speedy = 0
                self.state = STILL
        self.rect.y += self.speedy

        colisoes = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        for collision in colisoes:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top + 2
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL   
            # Estava indo para cima
            elif self.speedy < 0 and not isinstance(self.current_form, Fantasmagorico):
                self.rect.top = collision.rect.bottom - 12
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

        self.rect.x += self.speedx

        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        # Corrige a posição do personagem para antes da colisão
        self.colided = False
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0 and not isinstance(self.current_form, Fantasmagorico):
                self.rect.right = collision.rect.left + 20
                self.colided = True
            # Estava indo para a esquerda
            elif self.speedx < 0 and not isinstance(self.current_form, Fantasmagorico):
                self.rect.left = collision.rect.right - 20
                self.colided = True

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        
        
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    
# class Idle_Right(pygame.sprite.Sprite):
#     # Construtor da classe.
#     def __init__(self, center, assets):
#         # Construtor da classe mãe (Sprite).
#         pygame.sprite.Sprite.__init__(self)

#         # Armazena a animação de explosão
#         self.idle_right = assets[IDLE_RIGHT]

#         # Inicia o processo de animação colocando a primeira imagem na tela.
#         self.frame = 0  # Armazena o índice atual na animação
#         self.image = self.idle_right[self.frame]  # Pega a primeira imagem
#         self.rect = self.image.get_rect()
#         self.rect.center = center  # Posiciona o centro da imagem

#         # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
#         self.last_update = pygame.time.get_ticks()

#         # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
#         # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
#         # próxima imagem da animação será mostrada
#         self.frame_ticks = 50

#     def update(self):
#         # Verifica o tick atual.
#         now = pygame.time.get_ticks()
#         # Verifica quantos ticks se passaram desde a ultima mudança de frame.
#         elapsed_ticks = now - self.last_update

#         # Se já está na hora de mudar de imagem...
#         if elapsed_ticks > self.frame_ticks:
#             # Marca o tick da nova imagem.
#             self.last_update = now

#             # Avança um quadro.
#             self.frame += 1

#             # Verifica se já chegou no final da animação.
#             if self.frame == len(self.idle_right):
#                 # Se sim, tchau explosão!
#                 self.kill()
#             else:
#                 # Se ainda não chegou ao fim da explosão, troca de imagem.
#                 center = self.rect.center
#                 self.image = self.idle_right[self.frame]
#                 self.rect = self.image.get_rect()
#                 self.rect.center = center

class BotaoPlay(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['play'] # assets é um dicionário de imagens, sons e fontes 
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['play_clicado']
        else:
            self.image = self.assets['play']

class BotaoPlay2(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['play2'] # assets é um dicionário de imagens, sons e fontes 
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['play_clicado2']
        else:
            self.image = self.assets['play2']

class BotaoRestart(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['restart'] # assets é um dicionário de imagens, sons e fontes 
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['restart_clicado']
        else:
            self.image = self.assets['restart']

class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

        self.speedx = 0

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 10 * direction

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,groups ,assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ENEMY_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.speedx = 2
        self.speedy = 0
        self.blocks = groups['blocks']

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        self.speedy += ACELERACAO
        if self.speedy > 0:
            self.state = FALLING
            if self.rect.bottom == HEIGHT:
                self.speedy = 0
                self.state = STILL
        colisoes = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        for collision in colisoes:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top 
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
                  
        if self.rect.right > 900:
            self.speedx = -2
        if self.rect.left < 400:
            self.speedx = 2          
        collisions = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx < 0:
                self.rect.right = collision.rect.left + 20
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right - 20         