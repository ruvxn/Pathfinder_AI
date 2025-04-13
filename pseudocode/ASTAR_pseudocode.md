Inputs => Graph, origin node, destination nodes

Set the target as the first destination node  

Initialize a priority queue called OpenSet  
Add (Fscore=0, Gscore=0, origin) into OpenSet  

Create an empty set called Parent to store visited nodes  
Initialize a counter for visited nodes  

While OpenSet is not empty:  
    Pop (Fscore, Gscore, Path) with the lowest Fscore from OpenSet  
    Set CurrentNode as the last node in the Path  

    If CurrentNode equals the target:  
        Print debug info (Destination and Visited Count)  
        Return the Path and total cost (Gscore)  

    If CurrentNode is not in Parent:  
        Add CurrentNode to Parent  
        For each (neighbor, weight) of CurrentNode in the graph:  
            If neighbor is not in Parent:  
                Gscore = cost from origin to neighbor (current Gscore + weight)  
                Hscore = Euclidean distance from neighbor to destination  
                Fscore = Gscore + Hscore  
                UpdatedPath = Path + [neighbor]  
                Add (Fscore, Gscore, UpdatedPath) into OpenSet  

Output => A path from origin to the target destination and the total cost, or failure