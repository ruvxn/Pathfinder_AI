import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TreeBased Visualisation")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    print("DEBUG: Entered main loop")  # debugging 
    running = True
    while running:
        WINDOW.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
