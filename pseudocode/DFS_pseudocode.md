Inputs => Graph, origin node, destination nodes

Set up empty stack  
Push the origin node (as the initial path only contains the origin) onto the stack  
Create an empty set to keep track of visited nodes  

While the stack is not empty:  
    Pop the path at the top from the stack  
    The current node is the last node of the stack  

    If current node is one of the destination nodes:  
        Return the current path  

    if current node is not stored in the visited set:  
        Put current node as visited  

        For each of the neighbors of current node in sorted order:  
            if neighbor is not visited:  
                then create a new path by adding the neighbor to the current path  
                push the new path generated onto the stack  


Output => A path from origin to destination or a failure