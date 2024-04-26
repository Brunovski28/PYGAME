import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações de tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Cores
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)

def draw_3d_terrain():
    """Desenha um terreno 3D simplificado."""
    # Configurações do terreno
    num_layers = 20
    layer_height = 15
    depth_per_layer = 15
    
    for i in range(num_layers):
        # Calculando as dimensões e posição de cada "camada" do terreno
        rect_width = SCREEN_WIDTH - (i * depth_per_layer)
        rect_height = layer_height
        rect_x = (SCREEN_WIDTH - rect_width) // 2
        rect_y = SCREEN_HEIGHT - (i * layer_height) - layer_height

        # Desenho de cada "camada"
        pygame.draw.rect(screen, BROWN, (rect_x, rect_y, rect_width, rect_height))

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Preenche o fundo com preto
    screen.fill(BLACK)

    # Desenhar o terreno 3D
    draw_3d_terrain()

    # Atualiza a tela
    pygame.display.flip()

pygame.quit()
sys.exit()
