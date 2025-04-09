import random
import os

def generate_tests():
    
    folder_path = "./tests"  
    os.makedirs(folder_path, exist_ok=True)

    #get user input for required values

    num_nodes = int(input("Enter number of nodes for map: "))
    origin = int(input("Enter the origin: "))
    destinations = input("Enter destination nodes separated by commas(4,8): ")
    filename = input("Enter name for output file: ")
    max_edges_per_node = int(input("Enter maximum edges for nodes: "))

    filepath = os.path.join(folder_path, filename)

    #check if file already exists
    if os.path.exists(filepath):
        print(f"File '{filename}' already exists. Please choose a different name.")
        return
    

    #get destination list from user inputs
    destination_nodes = list(map(int, destinations.strip().split(",")))
    
    #generate nodes with random coordinates

    used_coords = set() # keeping tyrack of used node cordinates so that no two nodes are at the same position
    nodes = {}

    for i in range(1, num_nodes + 1):
        while True:
            x, y = random.randint(0, 10), random.randint(0, 10)
            if (x, y) not in used_coords:
                used_coords.add((x, y))
                nodes[i] = (x, y)
                break

    # Generate edges
    edges = set()

    for current_node in nodes:
        #list of other nodes that the current node we are on can connect to
        other_nodes = [n for n in nodes if n != current_node]

        #how many edges we want from this node
        num_edges = random.randint(1, min(max_edges_per_node, len(other_nodes)))

        # Randomly pick conneting nodes from the nodes list
        connected_nodes = random.sample(other_nodes, num_edges)

        # Create edges with random costs
        for target_node in connected_nodes:
            cost = random.randint(1, 10)
            edges.add((current_node, target_node, cost))


    #write to file
    with open(filepath, 'w') as f:
        f.write("Nodes:\n")
        for node, (x, y) in nodes.items():
            f.write(f"{node}:({x},{y})\n")

        f.write("\nEdges:\n")
        for node1, node2, cost in edges:
            f.write(f"({node1},{node2}):{cost}\n")

        f.write("\nOrigin:\n")
        f.write(f"{origin}\n")

        f.write("\nDestinations:\n")
        f.write("; ".join(map(str, destination_nodes)) + "\n")

    print(f"\n Test file '{filename}' created!")


if __name__ == "__main__":
    generate_tests()
