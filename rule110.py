import pygame
import numpy as np

# Rule 110
rule = [0, 1, 1, 1, 0, 1, 1, 0]

# Screen size
width, height = 800, 600
size = (width, height)

# Cell size
cell_size = 10

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Initialize the game
pygame.init()

# Set the screen size
screen = pygame.display.set_mode(size)

# Set the clock
clock = pygame.time.Clock()

# Initialize the cell states
cell_states = np.zeros((height // cell_size, width // cell_size))

def draw_cells():
    for i in range(cell_states.shape[0]):
        for j in range(cell_states.shape[1]):
            color = white if cell_states[i][j] else black
            pygame.draw.rect(screen, color, pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size))

def update_cells():
    global cell_states
    new_states = cell_states.copy()
    for i in range(cell_states.shape[0]):
        for j in range(1, cell_states.shape[1] - 1):
            pattern = int(''.join(str(int(x)) for x in cell_states[i, j-1:j+2][::-1]), 2)
            new_states[i, j] = rule[pattern]
    cell_states = new_states

# Game loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            j, i = pygame.mouse.get_pos()
            j //= cell_size
            i //= cell_size
            cell_states[i, j] = not cell_states[i, j]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        update_cells()
    screen.fill(black)
    draw_cells()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
