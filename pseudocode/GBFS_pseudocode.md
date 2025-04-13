Inputs => Graph, origin node, destination nodes

Set up a priority queue as frontier  
Add (0, origin) to the frontier where 0 is the heuristic score  

Create an empty set to keep track of visited nodes  

Get the coordinates of the first destination node  

While the frontier is not empty:  
    Pop the path with the lowest heuristic score from the frontier  
    The current node is the last node in the path  

    If the current node is in destination nodes:  
        Add the current node to visited  
        Return the current path and the visited nodes  

    If the current node is not in visited:  
        Add the current node to visited  

        For each neighbor of the current node in sorted order:  
            If neighbor is not visited:  
                Calculate h(n) heuristic value which is Euclidean distance from neighbor to destination  
                Create a new path by adding the neighbor to the current path  
                Add (h(n) value, new path) to the frontier  


Output => A path from origin to destination node, or failure 