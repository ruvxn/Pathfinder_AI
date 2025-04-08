from queue import PriorityQueue

class CUS1:
    def search(self, graph, origin, destinations):

        frontier = PriorityQueue()
        frontier.put((0, [origin]))

        #to avoid cycling through same nodes
        visited = set()

        #searching until emppty
        while not frontier.empty():
            
            current_cost, path = frontier.get()
            current_node = path[-1]  

            #check if destination is reached
            if current_node in destinations:
                return path, current_cost

            #visit only if not already visited
            if current_node not in visited:
                visited.add(current_node)

                #see the neightbor nodes to visit
                for neighbor, edge_cost in graph.neighbors(current_node):
                    if neighbor not in visited:
                        
                        total_cost = current_cost + edge_cost
                        new_path = path + [neighbor]

                        #add to the frontier
                        frontier.put((total_cost, new_path))

     
        return None, float('inf')
    
    #cost function for later
    def calculate_cost(self, graph, path):
        total = 0
        for i in range(len(path) - 1):
            total += graph.path_cost(path[i], path[i + 1])
        return total
