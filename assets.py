import pygame
import os
from config import WIDTH, HEIGHT, BEN_WIDTH, BEN_HEIGHT, IMG_DIR, BEN_DIR

BEN_IMG = 'ben_image'
DIAM_IMG = 'diamante_image'
XLR8_IMG = 'xlr8_immage'
FANT_IMG = 'fantasmagórico_image'
HURT_ANIM = 'hurt_anim'
IDLE_LEFT = 'idle_left'
IDLE_RIGHT = 'idle_right'
JUMP_LEFT = 'jump_left'
JUMP_RIGHT = 'jump_right'
RUN_LEFT = 'run_left'
RUN_RIGHT = 'run_right'
TRANS_LEFT = 'trans_left'
TRANS_RIGHT = 'trans_right'
BACKGROUND = 'background'
INICIO = 'inicio'
FIM = 'fim'
TELA_DE_INICIO = 'tela_de_inicio'
PLAY = 'play'
PLAY_CLICADO = 'play_clicado'
BLOCO = 'block'
DIAM_BULLET = 'diamante_bullet'
ENEMY = 'enemy'

def load_assets():
    assets = {}
    assets[PLAY] = pygame.image.load(os.path.join(IMG_DIR, 'Play.png')).convert()
    #mudando tamanho das imagens
    largura = assets['play'].get_rect().width * .20
    altura = assets['play'].get_rect().height * .20
    assets[PLAY] = pygame.transform.scale(assets[PLAY], (largura, altura))
    assets[PLAY_CLICADO] = pygame.image.load(os.path.join(IMG_DIR, 'Play_clicado.png')).convert()
    #mudando tamanho das imagens
    largura = assets['play_clicado'].get_rect().width * .20
    altura = assets['play_clicado'].get_rect().height * .20
    assets[PLAY_CLICADO] = pygame.transform.scale(assets[PLAY_CLICADO], (largura, altura))
    assets[TELA_DE_INICIO] = pygame.image.load(os.path.join(IMG_DIR, 'teladeinicio.jpg')).convert()
    assets[TELA_DE_INICIO] = pygame.transform.scale(assets[TELA_DE_INICIO], (WIDTH, HEIGHT))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'planodefundo.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[FIM] = pygame.image.load(os.path.join(IMG_DIR, 'Fim.png')).convert()
    assets[FIM] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BEN_IMG] = pygame.image.load(os.path.join(BEN_DIR, 'facing_right.png')).convert_alpha()
    assets[BEN_IMG] = pygame.transform.scale(assets['ben_image'], (BEN_WIDTH, BEN_HEIGHT))
    assets[DIAM_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'char01.png')).convert_alpha()
    assets[DIAM_IMG] = pygame.transform.scale(assets['diamante_image'], (BEN_WIDTH, BEN_HEIGHT))
    assets[XLR8_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'char02.png')).convert_alpha()
    assets[XLR8_IMG] = pygame.transform.scale(assets['xlr8_immage'], (BEN_WIDTH, BEN_HEIGHT))
    assets[FANT_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'char03.png')).convert_alpha()
    assets[FANT_IMG] = pygame.transform.scale(assets['fantasmagórico_image'], (BEN_WIDTH, BEN_HEIGHT))
    assets[BLOCO] = pygame.image.load(os.path.join(IMG_DIR, 'leavesBlock.png')).convert()
    assets[ENEMY] = pygame.image.load(os.path.join(IMG_DIR, 'enemy.png')).convert_alpha()
    assets[ENEMY] = pygame.transform.scale(assets['enemy'], (BEN_WIDTH, BEN_HEIGHT))
    hurt_anim = []
    for i in range(6):
        # Os arquivos de animação são numerados de 00 a 05
        filename = os.path.join(BEN_DIR, 'hurt0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        hurt_anim.append(img)
    assets[HURT_ANIM] = hurt_anim
    idle_left = []
    for i in range(3):
        # Os arquivos de animação são numerados de 00 a 02
        filename = os.path.join(BEN_DIR, 'idle_left0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        idle_left.append(img)
    assets[IDLE_LEFT] = idle_left
    idle_right = []
    for i in range(3):
        # Os arquivos de animação são numerados de 00 a 02
        filename = os.path.join(BEN_DIR, 'idle_right0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        idle_right.append(img)
    assets[IDLE_RIGHT] = idle_right
    jump_left = []
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = os.path.join(BEN_DIR, 'jump_left0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        jump_left.append(img)
    assets[JUMP_LEFT] = jump_left
    jump_right = []
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = os.path.join(BEN_DIR, 'jump_right0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        jump_right.append(img)
    assets[JUMP_RIGHT] = jump_right
    run_left = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 07
        filename = os.path.join(BEN_DIR, 'run_left0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        run_left.append(img)
    assets[RUN_LEFT] = run_left
    run_right = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 07
        filename = os.path.join(BEN_DIR, 'run_right0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        run_right.append(img)
    assets[RUN_RIGHT] = run_right
    trans_left = []
    for i in range(7):
        # Os arquivos de animação são numerados de 00 a 06
        filename = os.path.join(BEN_DIR, 'transformation_left0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        trans_left.append(img)
    assets[TRANS_LEFT] = trans_left
    trans_right = []
    for i in range(7):
        # Os arquivos de animação são numerados de 00 a 06
        filename = os.path.join(BEN_DIR, 'transformation_right0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (64, 64))
        trans_right.append(img)
    assets[TRANS_RIGHT] = trans_right
    assets[DIAM_BULLET] = pygame.image.load(os.path.join(IMG_DIR, 'diamante_bullet.png')).convert_alpha()
    assets[DIAM_BULLET] = pygame.transform.scale(assets[DIAM_BULLET], (20, 20))
    return assets