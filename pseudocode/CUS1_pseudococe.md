Inputs => Graph, origin node, destination nodes

Initialize a priority queue as frontier  
Add  (0, origin) to the frontier where 0 is the initial path cost  

Create an empty set to keep track of visited nodes  

While the frontier is not empty:  
    Pop the path with the lowest cost from the frontier  
    Set the current node as the last node in the path  

    If the current node is one of the destination nodes:  
        Add the current node to visited  
        Return the current path, visited nodes, and total cost  

    If the current node is not in visited:  
        Add the current node to visited  

        For each neighbor of the current node in sorted order:  
            If neighbor is not visited:  
                Calculate total cost is current cost + edge cost to neighbor  
                Create a new path by adding the neighbor to the current path  
                Add total cost, new path to the frontier  

Output => A path from origin destination, or failure 