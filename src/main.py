import sys
import pygame

pygame.init()

W, H = 600, 350
S = 5

# setting up the main window
clock = pygame.time.Clock()
window = pygame.display.set_mode((W, H))
pygame.display.set_caption('Demo')

# grid structure
cols, rows = int(W/S), int(H/S)
grid = [[0 for i in range(cols)] for j in range(rows)]

# main loop
while True:
    clock.tick(60)
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for col in range(cols):
        for row in range(rows):
            pos_x = col * S
            pos_y = row * S

            # block
            pygame.draw.rect(window, (0, 0, 0), (pos_x, pos_y, S, S))

            # outlines
            pygame.draw.line(window, (20, 20, 20), (pos_x, pos_y), (pos_x, H))
            pygame.draw.line(window, (20, 20, 20), (pos_x, pos_y), (W, pos_y))
    
    pygame.display.update()
