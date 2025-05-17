import pygame
from config import WIDTH, HEIGHT, BEN_WIDTH, BEN_HEIGHT, TILE_SIZE
from assets import BEN_IMG, IDLE_RIGHT

STILL = 0
JUMPING = 1
FALLING = 2
ACELERACAO = 2
JUMP_SIZE = 30

class Ben(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.state = STILL

        self.image = assets[BEN_IMG]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speedy = 0
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        self.blocks = groups['blocks']
    
    def update(self):
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
            elif self.speedy < 0:
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
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left + 20
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right - 20

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
    
class Idle_Right(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.idle_right = assets[IDLE_RIGHT]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.idle_right[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.idle_right):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.idle_right[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Botao(pygame.sprite.Sprite):
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