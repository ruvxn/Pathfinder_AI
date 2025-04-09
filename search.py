import sys
from utils.graph import Graph
from methods.dfs import DFS
from methods.bfs import BFS
from methods.gbfs import GBFS
from methods.cus1 import CUS1
from methods.Astar import ASTAR


def main():
    if len(sys.argv) != 3: # The number of arguments includes script, file and search method
        print("Usage: python search.py <graph_file> <search_method>") 
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    #load from input file 
    graph = Graph()
    graph.load_file(filename)

#clearing redundancy in dfs,bfs,gbfs printing
    search_methods_1 = {
        "DFS": DFS,
        "BFS": BFS,
        "GBFS": GBFS,
    }

    if method in search_methods_1:
        search_method = search_methods_1[method]()
        path = search_method.search(graph, graph.origin, graph.destination)

        print(f"{filename} {method}")
        goal_node = path[-1]
        print(f"{goal_node} {len(path)}")
        print(" ".join(str(n) for n in path))
    


    #if method == "DFS":

        #search_method = DFS()  
        #path = search_method.search(graph, graph.origin, graph.destination)
        
        

       # print(f"{filename} {method}")
       # goal_node = path[-1]
       # print(f"{goal_node} {len(path)}")
       # print(" ".join(str(n) for n in path))


   # elif method == "BFS":
        
        #search_method = BFS()
       # path  = search_method.search(graph, graph.origin, graph.destination)

      #  print(f"{filename} {method}")
       # goal_node = path[-1]
       # print(f"{goal_node} {len(path)}")
       # print(" ".join(str(n) for n in path))



   # elif method == "GBFS":

       # search_method= GBFS()
      #  path = search_method.search(graph, graph.origin, graph.destination)

       # print(f"{filename} {method}")
       # goal_node = path[-1]
       # print(f"{goal_node} {len(path)}")
       # print(" ".join(str(n) for n in path))


    elif method == "ASTAR":
        
        search_method= ASTAR()
        path, cost = search_method.search(graph, graph.origin, graph.destination)

        print(f"{filename} {method}")
        goal_node = path[-1]
        print(f"{goal_node} {len(path)}")
        print(" ".join(str(n) for n in path))

    elif method == "CUS1":

        search_method= CUS1()
        path, cost = search_method.search(graph, graph.origin, graph.destination)

        print(f"{filename} {method}")
        goal_node = path[-1]
        print(f"{goal_node} {len(path)}")
        print(" ".join(str(n) for n in path))

    elif method == "CUS2":
        pass
    else:
        print(f"Invalid search method: {method}")
        print("Try: DFS, BFS, GBFS, ASTAR, CUS1, CUS2")


if __name__ == '__main__':
    main()


