import pygame
import time
from config import WIDTH, HEIGHT, TILE_SIZE
# Importando as imagens
from assets import BEN_IMG, DIAM_IMG, XLR8_IMG, FANT_IMG, DIAM_BULLET, ENEMY_IMG
# Importando as animações
from assets import HURT_BEN, IDLE_BEN, RUN_BEN, JUMP_BEN, DIAM_IDLE, DIAM_SHOOT, DIAM_TRANSFORM, DIAM_JUMP, DIAM_RUN, XLR8_IDLE, XLR8_JUMP, XLR8_RUN, XLR8_TRANSFORM, FANT_IDLE, FANT_JUMP, FANT_RUN, FANT_TRANSFORM

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
        now = time.time()
        # This line was problematic: self.animation = [self.state]
        # It was setting self.animation to a list containing only the state ID, not the animation frames.
        # It should be:
        self.state = SHOOTING
        self.animation = self.animations[self.state] # Ensure animation is set correctly here
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

        self.state = self.base_form.state
        self.animations = self.base_form.animations
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        # Detalhes sobre o posicionamento.

        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 100 # Changed to a faster tick for smoother animation


    def handle_keys(self,groups, assets):
        keys = pygame.key.get_pressed()
        # Reset speedx and state for new key presses
        self.speedx = 0
        if self.state != JUMPING and self.state != FALLING: # Only set to IDLE if not jumping/falling
            self.state = IDLE

        if self.colided == False:
            if keys[pygame.K_RIGHT]:
                if isinstance(self.current_form, Xlr8):
                    self.speedx = 7
                    self.worldx += self.speedx
                else:
                    self.speedx = 2.05  # Adjusted for consistency with current code
                    self.worldx += self.speedx
                self.last_dir = 1
                self.state = RUNNING # Set state to RUNNING
            if keys[pygame.K_LEFT]:
                if isinstance(self.current_form, Xlr8):
                    self.speedx = -7
                    self.worldx += self.speedx
                else:
                    self.speedx = -2.05 # Adjusted for consistency with current code
                    self.worldx += self.speedx
                self.last_dir = -1
                self.state = RUNNING # Set state to RUNNING

        if keys[pygame.K_UP] and self.state == IDLE:
            self.jump()

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
        # When transforming, immediately update the image, state, and animations
        self.state = TRANSFORMING # Set state to TRANSFORMING
        self.animations = self.current_form.animations
        self.animation = self.animations[self.state]
        self.frame = 0 # Reset frame for new animation
        self.image = self.animation[self.frame]


    def update(self):
        # Handle transformation cooldown and revert
        if self.current_form != self.base_form and self.transform_time:
            if time.time() - self.transform_time >= 3:
                self.current_form = self.base_form
                self.transform_time = None
                self.last_transform_time = time.time()  # Start the cooldown for the base form
                # When reverting, reset to IDLE and update animations
                self.state = IDLE
                self.animations = self.current_form.animations
                self.animation = self.animations[self.state]
                self.frame = 0 # Reset frame for new animation
                self.image = self.animation[self.frame]


        # Gravity and vertical movement
        self.speedy += ACELERACAO
        if self.speedy > 0 and self.state != FALLING:
            self.state = FALLING # Set state to FALLING when moving downwards
        self.rect.y += self.speedy

        # Collision with blocks (vertical)
        colisoes = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        for collision in colisoes:
            if self.speedy > 0:  # Falling
                self.rect.bottom = collision.rect.top + 2
                self.speedy = 0
                if self.state == FALLING or self.state == JUMPING: # Only set to IDLE if coming from jump/fall
                    self.state = IDLE
            elif self.speedy < 0 and not isinstance(self.current_form, Fantasmagorico): # Jumping
                self.rect.top = collision.rect.bottom - 12
                self.speedy = 0
                self.state = FALLING # After hitting head on block, start falling

        # Keep player within vertical bounds
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            if self.state == FALLING or self.state == JUMPING:
                self.state = IDLE
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = 0 # Stop upward movement

        # Horizontal movement
        self.rect.x += self.speedx

        # Collision with blocks (horizontal)
        collisions = pygame.sprite.spritecollide(self, self.blocks, False, pygame.sprite.collide_mask)
        self.colided = False
        for collision in collisions:
            if not isinstance(self.current_form, Fantasmagorico):
                if self.speedx > 0:  # Moving right
                    self.rect.right = collision.rect.left +20
                    self.colided = True
                elif self.speedx < 0:  # Moving left
                    self.rect.left = collision.rect.right -20
                    self.colided = True
                self.worldx -= self.speedx    
                self.speedx = 0 # Stop horizontal movement on collision
                

        # Keep player within horizontal bounds
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 0

        # Animation Update
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        # Update current animation based on form and state
        # This is crucial: self.animation needs to be updated *before* checking frame length
        self.animation = self.current_form.animations[self.state]


        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            # Check if animation is finished (especially for non-looping animations like SHOOTING or TRANSFORMING)
            if self.frame >= len(self.animation):
                self.frame = 0 # Loop animation

                # For one-shot animations like SHOOTING or TRANSFORMING, revert to IDLE or RUNNING
                if self.state == SHOOTING and isinstance(self.current_form, Diamante):
                    self.state = IDLE # Or RUNNING, depending on movement
                    self.animation = self.current_form.animations[self.state] # Update animation immediately
                elif self.state == TRANSFORMING:
                    # After transforming animation, transition to idle/run of the new form
                    self.state = IDLE # Or RUNNING
                    self.animation = self.current_form.animations[self.state]


            center = self.rect.center
            # Flip image if last direction was left
            self.image = self.animation[self.frame]
            if self.last_dir == -1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.center = center


    def jump(self):
        # Only allow jump if on the ground or falling
        if self.speedy == 0: # This means the player is on solid ground
            self.speedy = -JUMP_SIZE
            self.state = JUMPING # Set state to JUMPING


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