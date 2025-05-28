import pygame
import os
from config import WIDTH, HEIGHT, BEN_WIDTH, BEN_HEIGHT, IMG_DIR, BEN_DIR, FNT_DIR, SND_DIR, TILE_SIZE, DIAM_DIR, ENEMY_DIR, XLR8_DIR, FANT_DIR

# Imagens
BACKGROUND = 'background'
INICIO = 'inicio'
FIM = 'fim'
TELA_DE_INICIO = 'tela_de_inicio'
BLOCO = 'block'
DIAM_BULLET = 'diamante_bullet'
TIME_FONT = 'time_font'
INSTRUCTIONS_IMG = 'instructions_img' 
WIN_SCREEN_IMG = 'win_screen_img'     
WIN_BLOCK_IMG = 'win_block_img'

# Botões
RESTART = 'restart'
RESTART_CLICADO = 'restart_clicado'
PLAY = 'play'
PLAY_CLICADO = 'play_clicado'
PLAY2 = 'play2'
PLAY_CLICADO2 = 'play_clicado2'
BOTAO_RESTART = 'botao_restart'
BOTAO_RESTART_CLICADO = 'botao_restart_clicado'

# Animações do Ben
BEN_IMG = 'ben_image'
HURT_BEN = 'hurt_anim'
IDLE_BEN = 'idle_anim'
JUMP_BEN = 'jump_anim'
RUN_BEN = 'run_anim'

# Animações Diamante
DIAM_IMG = 'diamante_image'
DIAM_IDLE = 'diam_idle_anim'
DIAM_JUMP = 'diam_jump_anim'
DIAM_RUN = 'diam_run_anim'
DIAM_SHOOT = 'diam_shoot_anim'
DIAM_TRANSFORM = 'diam_transform_anim'

# Animações XLR8
XLR8_IMG = 'xlr8_image'
XLR8_IDLE = 'xlr8_idle_anim'
XLR8_JUMP = 'xlr8_jump_anim'
XLR8_RUN = 'xlr8_run_anim'
XLR8_TRANSFORM = 'xlr8_transform_anim'

# Animações Fantasma
FANT_IMG = 'fantasmagórico_image'
FANT_IDLE = 'fant_idle_anim'
FANT_JUMP = 'fant_jump_anim'
FANT_RUN = 'fant_run_anim'
FANT_TRANSFORM = 'fant_transform_anim'

# Animação do inimigo
ENEMY_IMG = 'enemy_image'
ENEMY_ANIM = 'enemy_anim'
STILL_ENEMY = 'still_enemy'

# Sons
JUMP_SOUND = 'jump_sound'
SHOOT_SOUND = 'shoot_sound'
TRANSFORM_SOUND = 'transform_sound'
DETRANSFORM_SOUND = 'detransform_sound'
ENEMY_HIT_SOUND = 'enemy_hit_sound'
LOSE_SOUND = 'lose_sound'
WIN_SOUND = 'win_sound'
BACKGROUND_MUSIC = 'background_music'
BTN_CLICK_SOUND = 'btn_click_sound'
MENU_MUSIC = 'menu_music'

def load_assets():
    '''
    Carrega todos os assets do jogo.
    Retorna um dicionário com os assets carregados.
    '''
    assets = {}

    # Botões
    assets[PLAY] = pygame.image.load(os.path.join(IMG_DIR, 'Play.png')).convert()
    largura = assets['play'].get_rect().width * .35
    altura = assets['play'].get_rect().height * .35
    assets[PLAY] = pygame.transform.scale(assets[PLAY], (largura, altura))
    assets[PLAY_CLICADO] = pygame.image.load(os.path.join(IMG_DIR, 'Play_clicado.png')).convert()
    largura = assets['play_clicado'].get_rect().width * .35
    altura = assets['play_clicado'].get_rect().height * .35
    assets[PLAY_CLICADO] = pygame.transform.scale(assets[PLAY_CLICADO], (largura, altura))
    assets[PLAY2] = pygame.image.load(os.path.join(IMG_DIR, 'Play.png')).convert()
    largura = assets['play2'].get_rect().width * .25
    altura = assets['play2'].get_rect().height * .25
    assets[PLAY2] = pygame.transform.scale(assets[PLAY2], (largura, altura))
    assets[PLAY_CLICADO2] = pygame.image.load(os.path.join(IMG_DIR, 'Play_clicado.png')).convert()
    largura = assets['play_clicado2'].get_rect().width * .25
    altura = assets['play_clicado2'].get_rect().height * .25
    assets[PLAY_CLICADO2] = pygame.transform.scale(assets[PLAY_CLICADO2], (largura, altura))
    assets[RESTART_CLICADO] = pygame.image.load(os.path.join(IMG_DIR, 'restartclicado.png')).convert()
    largura = assets['restart_clicado'].get_rect().width * .82
    altura = assets['restart_clicado'].get_rect().height * .82
    assets[RESTART_CLICADO] = pygame.transform.scale(assets[RESTART_CLICADO], (largura, altura))
    assets[RESTART] = pygame.image.load(os.path.join(IMG_DIR, 'restart.png')).convert()
    largura = assets['restart'].get_rect().width * .82
    altura = assets['restart'].get_rect().height * .82
    assets[RESTART] = pygame.transform.scale(assets[RESTART], (largura, altura))
    assets[BOTAO_RESTART_CLICADO] = pygame.image.load(os.path.join(IMG_DIR, 'botaorestartclicado.png')).convert()
    largura = assets['botao_restart_clicado'].get_rect().width * .40
    altura = assets['botao_restart_clicado'].get_rect().height * .40
    assets[BOTAO_RESTART_CLICADO] = pygame.transform.scale(assets[BOTAO_RESTART_CLICADO], (largura, altura))
    assets[BOTAO_RESTART] = pygame.image.load(os.path.join(IMG_DIR, 'botaorestart.png')).convert()
    largura = assets['botao_restart'].get_rect().width * .40
    altura = assets['botao_restart'].get_rect().height * .40
    assets[BOTAO_RESTART] = pygame.transform.scale(assets[BOTAO_RESTART], (largura, altura))

    # Blocos
    assets[BLOCO] = pygame.image.load(os.path.join(IMG_DIR, 'leavesBlock.png')).convert()
    assets[WIN_BLOCK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'winblock.png')).convert_alpha()
    assets[WIN_BLOCK_IMG] = pygame.transform.scale(assets[WIN_BLOCK_IMG], (TILE_SIZE, TILE_SIZE * 2))

    # Telas
    assets[TELA_DE_INICIO] = pygame.image.load(os.path.join(IMG_DIR, 'teladeinicio.jpg')).convert()
    assets[TELA_DE_INICIO] = pygame.transform.scale(assets[TELA_DE_INICIO], (WIDTH, HEIGHT))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'planodefundo.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[FIM] = pygame.image.load(os.path.join(IMG_DIR, 'gameover.png')).convert()
    assets[FIM] = pygame.transform.scale(assets[FIM], (WIDTH, HEIGHT))
    assets[INSTRUCTIONS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'instrucoes.jpg')).convert()
    assets[INSTRUCTIONS_IMG] = pygame.transform.scale(assets[INSTRUCTIONS_IMG], (WIDTH, HEIGHT))
    assets[WIN_SCREEN_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'victory.png')).convert()
    assets[WIN_SCREEN_IMG] = pygame.transform.scale(assets[WIN_SCREEN_IMG], (WIDTH, HEIGHT))

    # Inimigo
    assets[ENEMY_IMG] = pygame.image.load(os.path.join(ENEMY_DIR, 'run00.png')).convert_alpha()
    assets[ENEMY_IMG] = pygame.transform.scale(assets['enemy_image'], (BEN_WIDTH, BEN_HEIGHT))
    enemy_anim = []
    for i in range(8):
        filename = os.path.join(ENEMY_DIR, f'run0{i}.png')
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        enemy_anim.append(img)
    assets[ENEMY_ANIM] = enemy_anim
    assets[STILL_ENEMY] = pygame.image.load(os.path.join(ENEMY_DIR, 'still_enemy.png')).convert_alpha()
    assets[STILL_ENEMY] = pygame.transform.scale(assets[STILL_ENEMY], (BEN_WIDTH*(4/3), BEN_HEIGHT))

    # Ben
    assets[BEN_IMG] = pygame.image.load(os.path.join(BEN_DIR, 'idle00.png')).convert_alpha()
    assets[BEN_IMG] = pygame.transform.scale(assets['ben_image'], (BEN_WIDTH, BEN_HEIGHT))
    hurt_anim = []
    for i in range(6):
        filename = os.path.join(BEN_DIR, 'hurt0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        hurt_anim.append(img)
    assets[HURT_BEN] = hurt_anim
    idle_anim = []
    for i in range(3):
        filename = os.path.join(BEN_DIR, 'idle0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        idle_anim.append(img)
    assets[IDLE_BEN] = idle_anim
    jump_anim = []
    for i in range(5):
        filename = os.path.join(BEN_DIR, 'jump0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        jump_anim.append(img)
    assets[JUMP_BEN] = jump_anim
    run_anim = []
    for i in range(8):
        filename = os.path.join(BEN_DIR, 'run0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        run_anim.append(img)
    assets[RUN_BEN] = run_anim

    # Diamante
    assets[DIAM_IMG] = pygame.image.load(os.path.join(DIAM_DIR, 'idle00.png')).convert_alpha()
    assets[DIAM_IMG] = pygame.transform.scale(assets['diamante_image'], (BEN_WIDTH, BEN_HEIGHT))
    diam_idle_anim = []
    for i in range(3):
        filename = os.path.join(DIAM_DIR, 'idle0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        diam_idle_anim.append(img)
    assets[DIAM_IDLE] = diam_idle_anim
    diam_jump_anim = []
    for i in range(2):
        filename = os.path.join(DIAM_DIR, 'jump0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        diam_jump_anim.append(img)
    assets[DIAM_JUMP] = diam_jump_anim
    diam_run_anim = []
    for i in range(6):
        filename = os.path.join(DIAM_DIR, 'run0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        diam_run_anim.append(img)
    assets[DIAM_RUN] = diam_run_anim
    diam_shoot_anim = []
    for i in range(3):
        filename = os.path.join(DIAM_DIR, 'shoot0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        diam_shoot_anim.append(img)
    assets[DIAM_SHOOT] = diam_shoot_anim
    diam_transform_anim = []
    for i in range(3):
        filename = os.path.join(DIAM_DIR, 'transform0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        diam_transform_anim.append(img)
    assets[DIAM_TRANSFORM] = diam_transform_anim
    assets[DIAM_BULLET] = pygame.image.load(os.path.join(IMG_DIR, 'diamante_bullet.png')).convert_alpha()
    assets[DIAM_BULLET] = pygame.transform.scale(assets[DIAM_BULLET], (20, 20))

    # XLR8
    assets[XLR8_IMG] = pygame.image.load(os.path.join(XLR8_DIR, 'idle00.png')).convert_alpha()
    assets[XLR8_IMG] = pygame.transform.scale(assets[XLR8_IMG], (BEN_WIDTH, BEN_HEIGHT))
    xlr8_idle_anim = []
    for i in range(3):
        filename = os.path.join(XLR8_DIR, 'idle0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        xlr8_idle_anim.append(img)
    assets[XLR8_IDLE] = xlr8_idle_anim
    xlr8_jump_anim = []
    for i in range(2):
        filename = os.path.join(XLR8_DIR, 'jump0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        xlr8_jump_anim.append(img)
    assets[XLR8_JUMP] = xlr8_jump_anim
    xlr8_run_anim = []
    for i in range(4):
        filename = os.path.join(XLR8_DIR, 'run0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        xlr8_run_anim.append(img)
    assets[XLR8_RUN] = xlr8_run_anim
    xlr8_transform_anim = []
    for i in range(3):
        filename = os.path.join(XLR8_DIR, 'transform0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        xlr8_transform_anim.append(img)
    assets[XLR8_TRANSFORM] = xlr8_transform_anim

    # Fantasma
    assets[FANT_IMG] = pygame.image.load(os.path.join(FANT_DIR, 'idle00.png')).convert_alpha()
    assets[FANT_IMG] = pygame.transform.scale(assets[FANT_IMG], (BEN_WIDTH, BEN_HEIGHT))
    fant_idle_anim = []
    for i in range(3):
        filename = os.path.join(FANT_DIR, 'idle0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        fant_idle_anim.append(img)
    assets[FANT_IDLE] = fant_idle_anim
    fant_jump_anim = []
    for i in range(2):
        filename = os.path.join(FANT_DIR, 'jump0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        fant_jump_anim.append(img)
    assets[FANT_JUMP] = fant_jump_anim
    fant_run_anim = []
    for i in range(2):
        filename = os.path.join(FANT_DIR, 'run0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        fant_run_anim.append(img)
    assets[FANT_RUN] = fant_run_anim
    fant_transform_anim = []
    for i in range(3):
        filename = os.path.join(FANT_DIR, 'transform0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (BEN_WIDTH, BEN_HEIGHT))
        fant_transform_anim.append(img)
    assets[FANT_TRANSFORM] = fant_transform_anim

    # Sons
    sound_files = {
        JUMP_SOUND: 'jump_sound.wav',
        SHOOT_SOUND: 'shoot_sound.wav',
        TRANSFORM_SOUND: 'transform_sound.wav',
        DETRANSFORM_SOUND: 'detransform_sound.wav',
        ENEMY_HIT_SOUND: 'enemy_hit_sound.wav',
        LOSE_SOUND: 'lose_sound.wav',
        WIN_SOUND: 'win_sound.wav',
        BTN_CLICK_SOUND: 'btn_click_sound.wav'
    }
    for sound_key, file_name in sound_files.items():
        assets[sound_key] = pygame.mixer.Sound(os.path.join(SND_DIR, file_name))
    assets[MENU_MUSIC] = os.path.join(SND_DIR, 'menu_music.wav')
    assets[BACKGROUND_MUSIC] = os.path.join(SND_DIR, 'background_music.wav')
    
    # Fonte
    assets[TIME_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    return assets