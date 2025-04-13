Inputs => Graph, origin node, destination nodes

Set up an empty queue  
Push the origin node which will be the initial path into the queue  
Create an empty set to keep track of visited nodes  

While the queue is not empty:  
    Pop the path from the front  of the queue  (FIFO operation)
    The current node is the last node in the path  

    If the current node is in destination nodes:  
        Add current node to visited for count
        Return the current path and visited nodes  

    If the current node is not in the visited set:  
        Add the current node to visited  

        For each neighbor of the current node in sorted order:  
            If the neighbor is not in visited:  
                Create a new path by adding the neighbor to the current path  
                Add the new path to the back of the queue  

Output => A path from origin to destination node, or failure