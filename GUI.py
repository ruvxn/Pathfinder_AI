import pygame
import sys

from utils.graph import Graph

from methods.dfs import DFS
from methods.bfs import BFS
from methods.gbfs import GBFS
from methods.Astar import ASTAR
from methods.cus1 import CUS1
from methods.cus2 import CUS2


pygame.init()

WIDTH, HEIGHT = 1000, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TreeBased Visualisation")

# colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)

METHODS = { "DFS": DFS, "BFS": BFS,  "GBFS": GBFS, "ASTAR": ASTAR, "CUS1": CUS1,"CUS2": CUS2}


GRID_SPACING = 80
FONT = pygame.font.SysFont("Arial", 20)

X_OFFSET = 60
Y_OFFSET = 60
NODE_RADIUS = 25

def draw_grid():

    for x in range(0, WIDTH, GRID_SPACING): #iterate through the width 

        pygame.draw.line(WINDOW, GREY, (x, 0), (x, HEIGHT))
        label = FONT.render(str(x // GRID_SPACING), True, BLACK)
        WINDOW.blit(label, (x + 2, 2))

    for y in range(0, HEIGHT, GRID_SPACING): #iterate through the height 

        pygame.draw.line(WINDOW, GREY, (0, y), (WIDTH, y))
        label = FONT.render(str(y // GRID_SPACING), True, BLACK)
        WINDOW.blit(label, (2, y + 2))

def transform_coords(x, y):
    return (x * GRID_SPACING + X_OFFSET, y * GRID_SPACING + Y_OFFSET)



def draw_node(x, y, label):
    screen_pos = transform_coords(x, y)
    print(f"DEBUG: Drawing node '{label}' at ({x}, {y}) => screen {screen_pos}")  # Debugging
    
    pygame.draw.circle(WINDOW, BLUE, screen_pos, NODE_RADIUS) #node 

    text = FONT.render(str(label), True, WHITE) 
    text_rect = text.get_rect(center=screen_pos)
    WINDOW.blit(text, text_rect)



# connecting node paths from arrow
def draw_arrow(start, end, color=BLACK):
    
    print(f"DEBUG: Drawing arrow from {start} to {end}")  # Debugging
    start_vec = pygame.math.Vector2(start) 
    end_vec = pygame.math.Vector2(end)

    direction = (end_vec - start_vec).normalize() #normalize gets the required direcrtion for arrow representing edge
    start_offset = start_vec + direction * NODE_RADIUS 
    end_offset = end_vec - direction * NODE_RADIUS

    pygame.draw.line(WINDOW, color, start_offset, end_offset, 2)

    # arrow head
    arrow_size = 10

    left = end_offset - direction * arrow_size + direction.rotate(135) * arrow_size * 0.5
    right = end_offset - direction * arrow_size + direction.rotate(-135) * arrow_size * 0.5

    pygame.draw.polygon(WINDOW, color, [end_offset, left, right])

def main():

    if len(sys.argv) != 3: 
        print("Please run the script like this: python3 GUI.py <graph_file> <search_method>")
        sys.exit(1)

    filename = sys.argv[1]  
    method_name = sys.argv[2].upper()

    if method_name not in METHODS:
        print(f"'{method_name}' is not a valid method. Choose from: DFS, BFS, GBFS, ASTAR, CUS1, CUS2")
        sys.exit(1)

    searcher = METHODS[method_name]()  # initialize search class for the method

    running = True
    while running:
        WINDOW.fill(WHITE)
        draw_grid()

        graph = Graph()
        #graph.load_file("tests/PathFinder-test.txt")  hardcoded file path UPDATE THIS TO TAKE INPUTS 
        graph.load_file(filename) # use graph.load_file(filename) to load the graph from the file 
        

        print(f"DEBUG: Loaded {len(graph.nodes)} nodes and {len(graph.edges)} edges")  # debug

        # start with the edges because the layout should show behind the nodes
        for (n1, n2), _ in graph.edges.items():
            start = transform_coords(*graph.nodes[n1])
            end = transform_coords(*graph.nodes[n2])
            draw_arrow(start, end)

        # draw nodes on top of the edges drawn 
        for node_id, (x, y) in graph.nodes.items(): 
            draw_node(x, y, node_id)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
