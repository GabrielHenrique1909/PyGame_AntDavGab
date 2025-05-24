import pygame
import os
from config import WIDTH, HEIGHT, BEN_WIDTH, BEN_HEIGHT, IMG_DIR, BEN_DIR, FNT_DIR

# Imagens
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
RESTART = 'restart'
RESTART_CLICADO = 'restart_clicado'
TELA_DE_INICIO = 'tela_de_inicio'
PLAY = 'play'
PLAY_CLICADO = 'play_clicado'
BLOCO = 'block'
DIAM_BULLET = 'diamante_bullet'
ENEMY = 'enemy'
TIME_FONT = 'time_font'
INSTRUCTIONS_IMG = 'instructions_img' 
WIN_SCREEN_IMG = 'win_screen_img'     
WIN_BLOCK_IMG = 'win_block_img'       

# Sons
JUMP_SOUND = 'jump_sound'
SHOOT_SOUND = 'shoot_sound'
TRANSFORM_SOUND = 'transform_sound'
ENEMY_HIT_SOUND = 'enemy_hit_sound'
PLAYER_DIE_SOUND = 'player_die_sound'
WIN_SOUND = 'win_sound'             # Som para quando o jogador vence
BACKGROUND_MUSIC = 'background_music'
BTN_CLICK_SOUND = 'btn_click_sound'   # Som para cliques em botões

def load_assets():
    assets = {}
    assets[PLAY] = pygame.image.load(os.path.join(IMG_DIR, 'Play.png')).convert()
    largura = assets['play'].get_rect().width * .35
    altura = assets['play'].get_rect().height * .35
    assets[PLAY] = pygame.transform.scale(assets[PLAY], (largura, altura))
    assets[PLAY_CLICADO] = pygame.image.load(os.path.join(IMG_DIR, 'Play_clicado.png')).convert()
    largura = assets['play_clicado'].get_rect().width * .35
    altura = assets['play_clicado'].get_rect().height * .35
    assets[PLAY_CLICADO] = pygame.transform.scale(assets[PLAY_CLICADO], (largura, altura))
    assets[TELA_DE_INICIO] = pygame.image.load(os.path.join(IMG_DIR, 'teladeinicio.jpg')).convert()
    assets[TELA_DE_INICIO] = pygame.transform.scale(assets[TELA_DE_INICIO], (WIDTH, HEIGHT))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'planodefundo.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[FIM] = pygame.image.load(os.path.join(IMG_DIR, 'gameover.png')).convert()
    assets[FIM] = pygame.transform.scale(assets[FIM], (WIDTH, HEIGHT))
    assets[RESTART_CLICADO] = pygame.image.load(os.path.join(IMG_DIR, 'restartclicado.png')).convert()
    largura = assets['restart_clicado'].get_rect().width * .82
    altura = assets['restart_clicado'].get_rect().height * .82
    assets[RESTART_CLICADO] = pygame.transform.scale(assets[RESTART_CLICADO], (largura, altura))
    assets[RESTART] = pygame.image.load(os.path.join(IMG_DIR, 'restart.png')).convert()
    largura = assets['restart'].get_rect().width * .82
    altura = assets['restart'].get_rect().height * .82
    assets[RESTART] = pygame.transform.scale(assets[RESTART], (largura, altura))
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
    assets[INSTRUCTIONS_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'instrucoes.jpg')).convert()
    assets[INSTRUCTIONS_IMG] = pygame.transform.scale(assets[INSTRUCTIONS_IMG], (WIDTH, HEIGHT))
    assets[WIN_SCREEN_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'win_background.png')).convert()
    assets[WIN_SCREEN_IMG] = pygame.transform.scale(assets[WIN_SCREEN_IMG], (WIDTH, HEIGHT))
    assets[WIN_BLOCK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'win_block.png')).convert_alpha() 
    assets[WIN_BLOCK_IMG] = pygame.transform.scale(assets[WIN_BLOCK_IMG], (TILE_SIZE, TILE_SIZE * 2))

    # Carregar novas imagens com fallback
    font_fallback_path = os.path.join(FNT_DIR, 'PressStart2P.ttf') # Caminho para a fonte de fallback
    # Carregar sons (com fallback para DummySound)
    class DummySound:
        def play(self): pass
        def stop(self): pass # Adicionado para consistência com pygame.mixer.music
        def fadeout(self, time): pass # Adicionado para consistência
    sound_files = {
        JUMP_SOUND: 'jump.wav',
        SHOOT_SOUND: 'shoot.wav',
        TRANSFORM_SOUND: 'transform.wav',
        ENEMY_HIT_SOUND: 'enemy_hit.wav',
        PLAYER_DIE_SOUND: 'player_die.wav',
        WIN_SOUND: 'win.wav',
        BTN_CLICK_SOUND: 'btn_click.wav'
    }
    for sound_key, file_name in sound_files.items():
        assets[sound_key] = pygame.mixer.Sound(os.path.join(SND_DIR, file_name))
    # Música de fundo (carregada como path, tocada com pygame.mixer.music)
    assets[BACKGROUND_MUSIC] = os.path.join(SND_DIR, 'background_music.ogg')
    
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
    assets[TIME_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    return assets