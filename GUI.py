import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TreeBased Visualisation")

# colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)

GRID_SPACING = 80
FONT = pygame.font.SysFont("Arial", 20)

X_OFFSET = 60
Y_OFFSET = 60
NODE_RADIUS = 25

def draw_grid():
    for x in range(0, WIDTH, GRID_SPACING):
        pygame.draw.line(WINDOW, GREY, (x, 0), (x, HEIGHT))
        label = FONT.render(str(x // GRID_SPACING), True, BLACK)
        WINDOW.blit(label, (x + 2, 2))
    for y in range(0, HEIGHT, GRID_SPACING):
        pygame.draw.line(WINDOW, GREY, (0, y), (WIDTH, y))
        label = FONT.render(str(y // GRID_SPACING), True, BLACK)
        WINDOW.blit(label, (2, y + 2))

def transform_coords(x, y):
    return (x * GRID_SPACING + X_OFFSET, y * GRID_SPACING + Y_OFFSET)

def draw_node(x, y, label):
    screen_pos = transform_coords(x, y)
    print(f"DEBUG: Drawing node '{label}' at ({x}, {y}) => screen {screen_pos}")  # Debugging
    pygame.draw.circle(WINDOW, BLUE, screen_pos, NODE_RADIUS)
    text = FONT.render(str(label), True, WHITE)
    text_rect = text.get_rect(center=screen_pos)
    WINDOW.blit(text, text_rect)

# connecting node paths from arrow
def draw_arrow(start, end, color=BLACK):
    print(f"DEBUG: Drawing arrow from {start} to {end}")  # Debugging
    start_vec = pygame.math.Vector2(start)
    end_vec = pygame.math.Vector2(end)
    direction = (end_vec - start_vec).normalize()
    start_offset = start_vec + direction * NODE_RADIUS
    end_offset = end_vec - direction * NODE_RADIUS
    pygame.draw.line(WINDOW, color, start_offset, end_offset, 2)

    # arrow head
    arrow_size = 10
    left = end_offset - direction * arrow_size + direction.rotate(135) * arrow_size * 0.5
    right = end_offset - direction * arrow_size + direction.rotate(-135) * arrow_size * 0.5
    pygame.draw.polygon(WINDOW, color, [end_offset, left, right])

def main():
    running = True
    while running:
        WINDOW.fill(WHITE)
        draw_grid()

        # draw the nodes
        pos_A = transform_coords(2, 3)
        pos_B = transform_coords(4, 4)
        draw_node(2, 3, "A")
        draw_node(4, 4, "B")

        # draw arrow between the nodes that represents the edge
        draw_arrow(pos_A, pos_B)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
