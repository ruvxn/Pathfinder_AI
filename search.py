import sys
from utils.graph import Graph

def main():
    if len(sys.argv) != 3: # The number of arguments includes script, file and search method
        print("Usage: python search.py <graph_file> <search_method>") 
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    #load from input file
    graph = Graph()
    graph.load_file(filename)

    print("graph loaded successfully")
    print(f"Origin: {graph.origin}")
    print(f"Destinations: {list(graph.destination.keys())}")

    if method == "DFS":
        pass  
    elif method == "BFS":
        pass
    elif method == "GBFS":
        pass
    elif method == "ASTAR":
        pass
    elif method == "CUS1":
        pass
    elif method == "CUS2":
        pass
    else:
        print(f"[!] Invalid search method: {method}")
        print("Try: DFS, BFS, UCS, GBFS, ASTAR, CUS1, CUS2")


if __name__ == '__main__':
    main()


