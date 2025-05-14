import pygame
import os
from config import BEN_WIDTH, BEN_HEIGHT, IMG_DIR, BEN_DIR

BEN_IMG = 'ben_image'
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

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'Background.png')).convert()
    assets[BEN_IMG] = pygame.image.load(os.path.join(BEN_DIR, 'facing_right.png')).convert_alpha()
    assets[BEN_IMG] = pygame.transform.scale(assets['ben_image'], (BEN_WIDTH, BEN_HEIGHT))
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
    return assets