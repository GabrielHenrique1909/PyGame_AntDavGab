from os import path

# Estabelece a pasta que contém as imagens de cada uma das animações dos personagens
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
BEN_DIR = path.join(path.dirname(__file__), 'assets', 'img', 'ben')

# Dados gerais do jogo.
WIDTH = 1920 # Largura da tela
HEIGHT = 1080 # Altura da tela
FPS = 60 # Frames por segundo

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
GAME = 1
QUIT = 2
OVER = 3