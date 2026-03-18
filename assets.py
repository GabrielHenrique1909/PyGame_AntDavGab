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
def carregar_animacao(diretorio, prefixo, num_frames, largura, altura):
    """
    Função auxiliar que abstrai o carregamento e redimensionamento de sprites.
    """
    animacao = []
    for i in range(num_frames):
        filename = os.path.join(diretorio, f'{prefixo}0{i}.png')
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (largura, altura))
        animacao.append(img)
    return animacao

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
    assets[ENEMY_IMG] = pygame.transform.scale(assets[ENEMY_IMG], (BEN_WIDTH, BEN_HEIGHT))
    assets[ENEMY_ANIM] = carregar_animacao(ENEMY_DIR, 'run', 8, BEN_WIDTH, BEN_HEIGHT)
    assets[STILL_ENEMY] = pygame.image.load(os.path.join(ENEMY_DIR, 'still_enemy.png')).convert_alpha()
    assets[STILL_ENEMY] = pygame.transform.scale(assets[STILL_ENEMY], (24*(3/2), 32*(3/2)))

    # Ben
    assets[BEN_IMG] = pygame.image.load(os.path.join(BEN_DIR, 'idle00.png')).convert_alpha()
    assets[BEN_IMG] = pygame.transform.scale(assets[BEN_IMG], (BEN_WIDTH, BEN_HEIGHT))

    assets[HURT_BEN] = carregar_animacao(BEN_DIR, 'hurt', 6, BEN_WIDTH, BEN_HEIGHT)
    assets[IDLE_BEN] = carregar_animacao(BEN_DIR, 'idle', 3, BEN_WIDTH, BEN_HEIGHT)
    assets[JUMP_BEN] = carregar_animacao(BEN_DIR, 'jump', 5, BEN_WIDTH, BEN_HEIGHT)
    assets[RUN_BEN] = carregar_animacao(BEN_DIR, 'run', 8, BEN_WIDTH, BEN_HEIGHT)

    # Diamante
    assets[DIAM_IMG] = pygame.image.load(os.path.join(DIAM_DIR, 'idle00.png')).convert_alpha()
    assets[DIAM_IMG] = pygame.transform.scale(assets[DIAM_IMG], (BEN_WIDTH, BEN_HEIGHT))

    assets[DIAM_IDLE] = carregar_animacao(DIAM_DIR, 'idle', 3, BEN_WIDTH, BEN_HEIGHT)
    assets[DIAM_JUMP] = carregar_animacao(DIAM_DIR, 'jump', 2, BEN_WIDTH, BEN_HEIGHT)
    assets[DIAM_RUN] = carregar_animacao(DIAM_DIR, 'run', 6, BEN_WIDTH, BEN_HEIGHT)
    assets[DIAM_SHOOT] = carregar_animacao(DIAM_DIR, 'shoot', 3, BEN_WIDTH, BEN_HEIGHT)
    assets[DIAM_TRANSFORM] = carregar_animacao(DIAM_DIR, 'transform', 3, BEN_WIDTH, BEN_HEIGHT)

    assets[DIAM_BULLET] = pygame.image.load(os.path.join(IMG_DIR, 'diamante_bullet.png')).convert_alpha()
    assets[DIAM_BULLET] = pygame.transform.scale(assets[DIAM_BULLET], (20, 20))

    # XLR8
    assets[XLR8_IMG] = pygame.image.load(os.path.join(XLR8_DIR, 'idle00.png')).convert_alpha()
    assets[XLR8_IMG] = pygame.transform.scale(assets[XLR8_IMG], (BEN_WIDTH, BEN_HEIGHT))

    assets[XLR8_IDLE] = carregar_animacao(XLR8_DIR, 'idle', 3, BEN_WIDTH, BEN_HEIGHT)
    assets[XLR8_JUMP] = carregar_animacao(XLR8_DIR, 'jump', 2, BEN_WIDTH, BEN_HEIGHT)
    assets[XLR8_RUN] = carregar_animacao(XLR8_DIR, 'run', 4, BEN_WIDTH, BEN_HEIGHT)
    assets[XLR8_TRANSFORM] = carregar_animacao(XLR8_DIR, 'transform', 3, BEN_WIDTH, BEN_HEIGHT)

    # Fantasma
    assets[FANT_IMG] = pygame.image.load(os.path.join(FANT_DIR, 'idle00.png')).convert_alpha()
    assets[FANT_IMG] = pygame.transform.scale(assets[FANT_IMG], (BEN_WIDTH, BEN_HEIGHT))

    assets[FANT_IDLE] = carregar_animacao(FANT_DIR, 'idle', 3, BEN_WIDTH, BEN_HEIGHT)
    assets[FANT_JUMP] = carregar_animacao(FANT_DIR, 'jump', 2, BEN_WIDTH, BEN_HEIGHT)
    assets[FANT_RUN] = carregar_animacao(FANT_DIR, 'run', 2, BEN_WIDTH, BEN_HEIGHT)
    assets[FANT_TRANSFORM] = carregar_animacao(FANT_DIR, 'transform', 3, BEN_WIDTH, BEN_HEIGHT)

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