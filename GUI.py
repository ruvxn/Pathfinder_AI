import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TreeBased Visualisation")

#colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)

GRID_SPACING = 80
FONT = pygame.font.SysFont("Arial", 20)

def draw_grid():
    print("DEBUG: Drawing grid")  # debugging 
    for x in range(0, WIDTH, GRID_SPACING):
        pygame.draw.line(WINDOW, GREY, (x, 0), (x, HEIGHT))
        label = FONT.render(str(x // GRID_SPACING), True, BLACK)
        WINDOW.blit(label, (x + 2, 2))
    for y in range(0, HEIGHT, GRID_SPACING):
        pygame.draw.line(WINDOW, GREY, (0, y), (WIDTH, y))
        label = FONT.render(str(y // GRID_SPACING), True, BLACK)
        WINDOW.blit(label, (2, y + 2))

def main():
    print("DEBUG: Entered main loop")  # debugging 
    running = True
    while running:
        WINDOW.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
