import networkx as nx 
import matplotlib.pyplot as plt



Graph = nx.Graph()
Graph.add_node(1, pos=(4,1)) 
Graph.add_node(2, pos=(2,2))
Graph.add_node(3, pos =(4,4))   
Graph.add_node(4, pos=(6,3))
Graph.add_node(5, pos=(5,6))
Graph.add_node(6, pos=(7,5))

Graph.add_edge(2,1, weight=4)
Graph.add_edge(3, 1, weight = 5)
Graph.add_edge(1,3, weight = 5)
Graph.add_edge(2, 3, weight = 4)
Graph.add_edge(3, 2, weight = 5)
Graph.add_edge(4, 1, weight = 6)
Graph.add_edge(1, 4, weight = 6)
Graph.add_edge(4, 3, weight = 5)
Graph.add_edge(3, 5, weight = 6)
Graph.add_edge(5, 3, weight = 6)
Graph.add_edge(4, 5, weight = 7)
Graph.add_edge(5, 4, weight = 8)
Graph.add_edge(6, 3, weight = 7)
Graph.add_edge(3, 6, weight = 7)
SourceNode = 1
CurrentNode = SourceNode
DestinationNode = 6
ParentNodes = {}
Steps = 0
#print(Graph.edges(data=True))


#checks what nodes are connected by comparing the current node to the edge list 
def CheckAdjacency(Currentnode, Destinationnode):
    AdjacentNodes = {}
    for i in Graph.edges(data=True): # Add adjacent node and its weight
        if i[0] == Currentnode:
            
            AdjacentNodes[i[1]] = i[2]['weight']  
        elif i[1] == Currentnode:

            AdjacentNodes[i[0]] = i[2]['weight'] 
    for node in AdjacentNodes: 
        if node in AdjacentNodes == DestinationNode:
            MoveTo(node, CurrentNode)
            break
    AdjacentNodes = {node: weight for node, weight in AdjacentNodes.items() if node not in ParentNodes} #filters out parent nodes (otherwise it gets stuck in an infinate loop)
    return AdjacentNodes

def CheckWeight(MoveableNodes):

    SmallestWeight = 1000
    SmallestNode = None
    for Node  in MoveableNodes:
        if SmallestWeight > MoveableNodes[Node]:
            SmallestWeight = MoveableNodes[Node]
            SmallestNode = Node
    return  SmallestNode
   
def MoveTo(SmallestWeight, CurrentNode, ParentNodes = {}): 
    ParentNodes[SmallestWeight] = CurrentNode

    CurrentNode = SmallestWeight
    print("Current Node:", CurrentNode)
    return CurrentNode




nx.draw_shell(Graph, with_labels=True)
edge_labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw_networkx_edge_labels(Graph, pos=nx.shell_layout(Graph), edge_labels=edge_labels)

plt.show() 
while DestinationNode != CurrentNode:
    
    if CurrentNode == DestinationNode: #checks if the current node is the destination node before running the rest of the code 
        print("Destination Reached")
    else:
        print("Destination not reached")



        Adj = CheckAdjacency(CurrentNode, DestinationNode) 
        
        print("Adjacent Nodes with Weights:", Adj) #bugtesting 

        if not Adj:
            print("No valid moves available. Stuck!")
            break

        
        Adj ={node: weight for node, weight in Adj.items() if node not in ParentNodes} #filters out parent nodes (otherwise it gets stuck in an infinate loop)
        print("Adjacent Nodes with Weights:", Adj) #bugtesting 
  
        SmallestNode = CheckWeight(Adj)
        print("Smallest Node:", SmallestNode) #bugtesting 
        ParentNodes[Steps] = CurrentNode
        CurrentNode = (MoveTo(SmallestNode, CurrentNode))
        Steps += 1
        print("Parent Nodes:", ParentNodes) #Bug testing 
        print("Steps:", Steps) #bugtesting 
