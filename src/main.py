import sys
import pygame
import config

pygame.init()
cfg = config.get()

# setting up the main window
clock = pygame.time.Clock()
window = pygame.display.set_mode((cfg.window.width, cfg.window.height))
pygame.display.set_caption(cfg.window.title)

# grid structure
cols, rows = int(cfg.window.width / cfg.block.size), int(cfg.window.height / cfg.block.size)
grid = [[0 for i in range(cols)] for j in range(rows)]

# one-dimensional ca, starting from top row, middle col
grid[0][int(cols / 2)] = 1

# main loop
while True:
    clock.tick(60)
    window.fill(cfg.colors.background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for col in range(cols):
        for row in range(rows):
            pos_x = col * cfg.block.size
            pos_y = row * cfg.block.size

            # dead/alive drawing
            if grid[row][col] == 1:
                pygame.draw.rect(window, cfg.colors.active, (pos_x, pos_y, cfg.block.size, cfg.block.size))
            else:
                pygame.draw.rect(window, cfg.colors.background, (pos_x, pos_y, cfg.block.size, cfg.block.size))

            # outlines
            pygame.draw.line(window, cfg.colors.grid, (pos_x, pos_y), (pos_x, cfg.window.height))
            pygame.draw.line(window, cfg.colors.grid, (pos_x, pos_y), (cfg.window.height, pos_y))
    
    pygame.display.update()
