import pygame
import time
from config import WIDTH, HEIGHT, TILE_SIZE
# Importando as imagens
from assets import BEN_IMG, DIAM_IMG, XLR8_IMG, FANT_IMG, DIAM_BULLET, ENEMY_IMG
# Importando as animações
from assets import HURT_BEN, IDLE_BEN, RUN_BEN, JUMP_BEN, DIAM_IDLE, DIAM_SHOOT, DIAM_TRANSFORM, DIAM_JUMP, DIAM_RUN, XLR8_IDLE, XLR8_JUMP, XLR8_RUN, XLR8_TRANSFORM, FANT_IDLE, FANT_JUMP, FANT_RUN, FANT_TRANSFORM
# Importando os sons
from assets import TRANSFORM_SOUND, DETRANSFORM_SOUND, SHOOT_SOUND

# Definindo os estados dos personagens
IDLE = 0
JUMPING = 1
FALLING = 2
RUNNING = 3
SHOOTING = 4
TRANSFORMING = 5
DYING = 6

class Ben:
    def __init__(self, assets):
        '''
        Classe que representa o personagem Ben Tennyson
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        self.image = assets[BEN_IMG]
        self.state = IDLE
        self.animations = {
            IDLE: assets[IDLE_BEN],
            JUMPING: assets[JUMP_BEN],
            FALLING: assets[JUMP_BEN],
            RUNNING: assets[RUN_BEN],
            DYING: assets[HURT_BEN]
        }
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]

class Diamante:
    def __init__(self, groups ,assets):
        '''
        Classe que representa o personagem Diamante
        groups: Dicionário de grupos do jogo, incluindo blocos e inimigos
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        self.image = assets[DIAM_IMG]
        self.last_shot_time = 0
        self.shot_cooldown = 0.5
        self.blocks = groups['blocks']
        self.state = IDLE
        self.animations = {
            IDLE: assets[DIAM_IDLE],
            JUMPING: assets[DIAM_JUMP],
            FALLING: assets[DIAM_JUMP],
            RUNNING: assets[DIAM_RUN],
            SHOOTING: assets[DIAM_SHOOT],
            TRANSFORMING: assets[DIAM_TRANSFORM]
        }
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]

    def shoot(self, player, all_sprites, all_bullets, assets):
        '''
        Método para disparar um projétil (pequenos diamantes)
        player: O jogador que está disparando
        all_sprites: Grupo de todos os sprites do jogo
        all_bullets: Grupo de todos os projéteis do jogo
        assets: Dicionário de recursos do jogo, incluindo sons
        '''
        now = time.time()
        # Não permite disparar se o tempo desde o último disparo for menor que o cooldown
        if now - self.last_shot_time < self.shot_cooldown:
            return

        assets[SHOOT_SOUND].play() # Toca o som de disparo

        self.state = SHOOTING
        self.animation = self.animations[self.state]
        x = player.rect.centerx
        y = player.rect.centery
        direction = player.last_dir
        bullet_img = assets[DIAM_BULLET]
        if direction == -1:
            bullet_img = pygame.transform.flip(bullet_img, True, False)
        bullet = Projectile(x, y, direction, bullet_img)
        all_sprites.add(bullet)
        all_bullets.add(bullet)
        self.last_shot_time = now  # Registra o tempo do último disparo



class Xlr8:
    def __init__(self, assets):
        '''
        Classe que representa o personagem Xlr8
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        self.image = assets[XLR8_IMG]
        self.state = IDLE
        self.animations = {
            IDLE: assets[XLR8_IDLE],
            JUMPING: assets[XLR8_JUMP],
            FALLING: assets[XLR8_JUMP],
            RUNNING: assets[XLR8_RUN],
            TRANSFORMING: assets[XLR8_TRANSFORM]
        }
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]

class Fantasmagorico:
    def __init__(self, assets):
        '''
        Classe que representa o personagem Fantasmagorico
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        self.image = assets[FANT_IMG]
        self.state = IDLE
        self.animations = {
            IDLE: assets[FANT_IDLE],
            JUMPING: assets[FANT_JUMP],
            FALLING: assets[FANT_JUMP],
            RUNNING: assets[FANT_RUN],
            TRANSFORMING: assets[FANT_TRANSFORM]
        }
        self.animation = self.animations[self.state]
        self.frame = 0
        self.image = self.animation[self.frame]

STILL = 0
JUMPING = 1
FALLING = 2
ACELERACAO = 0.5
JUMP_SIZE = 15

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        '''
        Classe que representa o jogador
        groups: Dicionário de grupos do jogo, incluindo blocos e inimigos
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.state = STILL
        self.colided = False
        self.last_dir = 1  # Começa olhando para a direita
        self.last_transform_time = 0  # tempo da última transformação revertida
        self.transform_cooldown = 3  # segundos de espera após transformação
        self.base_form = Ben(self.assets)
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
        self.blocks = groups['blocks']
        self.enemy = groups['enemy']

        self.state = self.base_form.state
        self.animations = self.base_form.animations
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]

        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 100


    def handle_keys(self,groups):
        '''
        Método para lidar com as teclas pressionadas
        groups: Dicionário de grupos do jogo, incluindo blocos e inimigos
        '''
        keys = pygame.key.get_pressed()
        # Reseta a velocidade horizontal
        self.speedx = 0
        if self.state != JUMPING and self.state != FALLING and self.state != SHOOTING:
            self.state = IDLE

        if self.colided == False:
            if keys[pygame.K_RIGHT]:
                if isinstance(self.current_form, Xlr8):
                    self.speedx = 7
                    self.worldx += self.speedx
                else:
                    self.speedx = 2.05
                    self.worldx += self.speedx
                self.last_dir = 1
                self.state = RUNNING
            if keys[pygame.K_LEFT]:
                if isinstance(self.current_form, Xlr8):
                    self.speedx = -7
                    self.worldx += self.speedx
                else:
                    self.speedx = -2.05
                    self.worldx += self.speedx
                self.last_dir = -1
                self.state = RUNNING

        if keys[pygame.K_UP] and self.state == IDLE:
            self.jump()

        # Transformações com W, A, D
        if keys[pygame.K_w]:
            self.transform(Diamante(groups, self.assets))
        elif keys[pygame.K_a]:
            self.transform(Xlr8(self.assets))
        elif keys[pygame.K_d]:
            self.transform(Fantasmagorico(self.assets))


    def transform(self, new_form):
        '''
        Método para transformar o jogador em um novo personagem
        new_form: A nova forma para a qual o jogador deseja se transformar
        '''
        now = time.time()

        # Condition 1: Prevent transformation if currently an alien and trying to transform into the same alien type.
        # This explicitly checks if the *object itself* is the same or if the *type* is the same.
        if self.current_form is new_form: # Check if it's literally the same object instance (unlikely for new_form)
            return
        if type(self.current_form) is type(new_form): # Check if they are of the exact same class type
            return

        # Condition 2: Allow transformation if currently Ben.
        # Condition 3: If already transformed (not Ben), require reverting to Ben first.
        # Condition 4: Respect the cooldown after reverting to Ben.
        if self.current_form != self.base_form: # If currently an alien (not Ben)
            # You can only transform to another alien if you first revert to Ben.
            # So, if current_form is an alien, and new_form is also an alien (and not Ben), block it.
            # The previous logic "now - self.last_transform_time < self.transform_cooldown" handles cooldown after detransform.
            # So if current_form is alien, and new_form is different alien, we should block directly unless specifically allowed.
            # The intention here is usually: Ben -> Alien1, Alien1 -> Ben, Ben -> Alien2. Not Alien1 -> Alien2 directly.
            # Your current setup already prevents Alien1 -> Alien2 because 'now - self.last_transform_time < self.transform_cooldown'
            # will be true if you are already an alien and haven't detransformed.

            # Let's simplify this: if already an alien, and the new form is also an alien, and you haven't detransformed, don't allow.
            # The cooldown on 'last_transform_time' only applies *after* returning to base_form.
            # So, if current_form is not base_form, and you are trying to transform to *any* new_form (even a different alien),
            # this means you haven't reverted to Ben yet, which is typically a design choice.
            if self.transform_time is not None: # If you are currently in a transformation phase (non-Ben)
                # And you haven't reverted yet, then you cannot transform again.
                return

        # Handle cooldown specifically for when returning *from* a transformation
        # This check is for transforming *into* an alien from Ben, after a previous detransformation.
        if now - self.last_transform_time < self.transform_cooldown:
            return  # Blocks transformation if still on cooldown after a previous detransformation

        # If all checks pass, then a valid transformation is occurring. Play the sound.
        self.assets[TRANSFORM_SOUND].play()

        self.current_form = new_form
        self.transform_time = now # Grava o tempo da transformação atual
        self.state = TRANSFORMING
        self.animations = self.current_form.animations
        self.animation = self.animations[self.state]
        self.frame = 0 # Reseta o quadro da animação
        self.image = self.animation[self.frame]


    def update(self):
        '''
        Método para atualizar o estado do jogador
        '''
        # Cuida do cooldown de transformação
        if self.current_form != self.base_form and self.transform_time:
            if time.time() - self.transform_time >= 5:  # 5 segundos de transformação
                # Se passou o tempo de transformação, volta para a forma base
                self.current_form = self.base_form
                self.transform_time = None
                self.last_transform_time = time.time()
                self.assets[DETRANSFORM_SOUND].play()
                # Quando volta para a forma base, reseta o estado e animações
                self.state = IDLE
                self.animations = self.current_form.animations
                self.animation = self.animations[self.state]
                self.frame = 0 # Reseta o quadro da animação
                self.image = self.animation[self.frame]


        # Gravidade e movimento vertical
        self.speedy += ACELERACAO
        if self.speedy > ACELERACAO and self.state != FALLING:
            self.state = FALLING # Define estado como FALLING se a velocidade vertical for maior que a aceleração
        self.rect.y += self.speedy

        # Colisão com blocos (vertical)
        colisoes = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        for collision in colisoes:
            if self.speedy > 0:  # Caindo
                self.rect.bottom = collision.rect.top + 2
                self.speedy = 0
                if self.state == FALLING or self.state == JUMPING:
                    self.state = IDLE
            elif self.speedy < 0 and not isinstance(self.current_form, Fantasmagorico):
                self.rect.top = collision.rect.bottom - 12
                self.speedy = 0
                self.state = FALLING # Quando colide para cima, assume que está caindo
        # Mantém o jogador dentro dos limites verticais
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            if self.state == FALLING or self.state == JUMPING:
                self.state = IDLE
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = 0 # Para movimento vertical se colidir com o topo da tela

        # Movimento horizontal
        self.rect.x += self.speedx

        # Colisões horizontais com blocos
        collisions = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        self.colided = False
        for collision in collisions:
            if not isinstance(self.current_form, Fantasmagorico):
                if self.speedx > 0:
                    self.rect.right = collision.rect.left +20
                    self.colided = True
                elif self.speedx < 0:
                    self.rect.left = collision.rect.right -20
                    self.colided = True
                self.worldx -= self.speedx    
                self.speedx = 0 # Para movimento horizontal se colidir com um bloco
                

        # Mantém o jogador dentro dos limites horizontais
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 0

        # Animation Update
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        self.animation = self.current_form.animations[self.state]


        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            # Checa se a animação atual está completa
            if self.frame >= len(self.animation):
                self.frame = 0 # Loopa a animação

                if self.state == SHOOTING and isinstance(self.current_form, Diamante):
                    self.state = IDLE
                    self.animation = self.current_form.animations[self.state]
                elif self.state == TRANSFORMING:
                    self.state = IDLE
                    self.animation = self.current_form.animations[self.state]


            center = self.rect.center
            # Vira a imagem se necessário
            self.image = self.animation[self.frame]
            if self.last_dir == -1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.center = center


    def jump(self):
        '''
        Método para fazer o jogador pular
        '''
        # Apenas pula se estiver no estado IDLE ou se estiver caindo
        if self.speedy == 0:
            self.speedy = -JUMP_SIZE
            self.state = JUMPING


class BotaoPlay(pygame.sprite.Sprite):
    def __init__(self, assets):
        '''
        Classe que representa o botão de Play
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['play']
        self.mask = pygame.mask.from_surface(self.image)
        # todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        '''
        Método para lidar com o mouse sobre o botão
        over: Booleano que indica se o mouse está sobre o botão
        '''
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['play_clicado']
        else:
            self.image = self.assets['play']

class BotaoPlay2(pygame.sprite.Sprite):
    def __init__(self, assets):
        '''
        Classe que representa o botão de Play (versão 2)
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['play2'] # assets é um dicionário de imagens, sons e fontes
        self.mask = pygame.mask.from_surface(self.image)
        # todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        '''
        Método para lidar com o mouse sobre o botão (versão 2)
        over: Booleano que indica se o mouse está sobre o botão
        '''
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['play_clicado2']
        else:
            self.image = self.assets['play2']

class BotaoRestart(pygame.sprite.Sprite):
    def __init__(self, assets):
        '''
        Classe que representa o botão de Restart
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['restart'] # assets é um dicionário de imagens, sons e fontes
        self.mask = pygame.mask.from_surface(self.image)
        # todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        '''
        Método para lidar com o mouse sobre o botão de Restart
        over: Booleano que indica se o mouse está sobre o botão
        '''
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['restart_clicado']
        else:
            self.image = self.assets['restart']

class BotaoRestartWin(pygame.sprite.Sprite):
    def __init__(self, assets):
        '''
        Classe que representa o botão de Restart na tela de vitória
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['botao_restart'] # assets é um dicionário de imagens, sons e fontes
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 20
        self.rect.y = 70

    def mouse_over(self, over):
        '''
        Método para lidar com o mouse sobre o botão de Restart na tela de vitória
        over: Booleano que indica se o mouse está sobre o botão
        '''
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['botao_restart_clicado']
        else:
            self.image = self.assets['botao_restart']

class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        '''
        Classe que representa um tile no jogo
        tile_img: Imagem do tile
        row: Linha onde o tile será posicionado
        column: Coluna onde o tile será posicionado
        '''
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
        '''
        Classe que representa um projétil disparado pelo jogador
        x: Posição x inicial do projétil
        y: Posição y inicial do projétil
        direction: Direção do projétil (-1 para esquerda, 1 para direita)
        image: Imagem do projétil
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 10 * direction

    def update(self):
        '''
        Método para atualizar a posição do projétil
        '''
        # Atualiza a posição do projétil
        self.rect.x += self.speedx
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,groups ,assets):
        '''
        Classe que representa um inimigo no jogo
        groups: Dicionário de grupos do jogo, incluindo blocos e inimigos
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ENEMY_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedx = 2
        self.speedy = 0
        self.blocks = groups['blocks']

    def update(self):
        '''
        Método para atualizar a posição do inimigo
        '''
        # Atualizando a posição do inimigo 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += ACELERACAO

        #Verifica se tem colisão com o bloco para baixo
        colisoes = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        for colisao in colisoes:
            # Estava indo para baixo
            if self.speedy > 0:
                #Muda a posição do inimigo (faz ele subir blocos tambem)
                self.rect.bottom = colisao.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        #Mata o inimigo se ele cair no void        
        if self.rect.y>700:
            self.kill()

        #Mantém o inimigo se movimentando para um range de 100 pixels ao redor do personagem    
        if self.rect.right > 820:
            self.speedx = -2
        if self.rect.left < 620:
            self.speedx = 2

class StillEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, groups ,assets):
        '''
        Classe que representa um inimigo parado no jogo
        x: Posição x do inimigo
        y: Posição y do inimigo
        groups: Dicionário de grupos do jogo, incluindo blocos e inimigos
        assets: Dicionário de recursos do jogo, incluindo imagens e sons
        '''
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ENEMY_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
        self.blocks = groups['blocks']

    def update(self):
        '''
        Método para atualizar a posição do inimigo parado
        '''
        self.speedy += ACELERACAO
        self.rect.y += self.speedy

        #Cria colisão para baixo, evitando que caia
        colisoes = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        for collision in colisoes:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        #Mata ele se passa da tela        
        if self.rect.x<10:
            self.kill()        