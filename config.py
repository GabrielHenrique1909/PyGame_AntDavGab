from os import path

# Estabelece a pasta que contém as imagens de cada uma das animações dos personagens
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
BEN_DIR = path.join(path.dirname(__file__), 'assets', 'img', 'ben_sprites')
DIAM_DIR = path.join(path.dirname(__file__), 'assets', 'img', 'diamante_sprites')
ENEMY_DIR = path.join(path.dirname(__file__), 'assets', 'img', 'enemy_sprites')
XLR8_DIR = path.join(path.dirname(__file__), 'assets', 'img', 'xlr8_sprites')
FANT_DIR = path.join(path.dirname(__file__), 'assets', 'img', 'fantasma_sprites')

# Estabelece a pasta que contém as fontes e sons do jogo
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd') # Pasta para sons

# Dados gerais do jogo.
WIDTH = int(1920*0.75) # Largura da tela
HEIGHT = int(1080*0.75) # Altura da tela
FPS = 60 # Frames por segundo
TILE_SIZE = 60 # Tamanho de cada tile (cada tile é um quadrado) 

# Define tamanhos
BEN_WIDTH = 64
BEN_HEIGHT = 64

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
INSTRUCTIONS = 1
GAME = 2
OVER = 3
WIN = 4
QUIT = 5

# Tipos de Tile
BLOCK = 0
EMPTY = -1
WIN_BLOCK_TYPE = 1 #Bloco de vitória

# Arquivo de High Scores (Ranking)
HIGH_SCORE_FILE = "high_scores.txt"