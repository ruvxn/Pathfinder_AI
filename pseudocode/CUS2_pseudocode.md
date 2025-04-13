Inputs => Graph, origin node, destination nodes

Initialize a counter for tie-breaking priority queue entries  
Create a priority queue called frontier  
Add ((steps=0, counter=0, heuristic=0), origin) to the frontier  

Create an empty set to track visited nodes  

While the frontier is not empty:  
    Pop the (priority, path) with the lowest priority from frontier  
    Extract steps and current_node (last node in the path)  

    If current_node is one of the destination nodes:  
        Return the current path and its total cost  

    If current_node is not in visited:  
        Add current_node to visited  

        For each (neighbor, _) of current_node in sorted order:  
            If neighbor is not visited:  
                Append neighbor to path to create new_path  
                Find closest destination to neighbor  
                Calculate heuristic = Euclidean distance from neighbor to closest destination  
                Calculate steps = number of nodes in new_path - 1  
                Generate priority = (steps, next counter value, heuristic)  
                Add (priority, new_path) to frontier  

Output => A path from origin to the closest destination with cost, or failure with infinite cost