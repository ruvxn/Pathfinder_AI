from utils.heuristics import euclidean_distance
from queue import PriorityQueue

class GBFS:

    def goal_coordinates(self, graph, destination):
        for dest in destination:
            return graph.nodes[dest]
        

    def search(self, graph, origin, destination):
        frontier = PriorityQueue()
        frontier.put((0, [origin]))

        visited = set()                                                                     #intialise list to keep track of visited nodes to avoid cycles
        goal_coords = self.goal_coordinates(graph, destination)

        while not frontier.empty():
            h_score, path = frontier.get() 
            current = path[-1]

            if current in destination:
                return path

            if current not in visited:
                visited.add(current)

                neighbors = sorted(graph.neighbors(current))                                #sorted is used for taking the right order when everything is equal
                unvisited = filter(lambda pair: pair[0] not in visited, neighbors)          # filter out where function is false

                scored_paths = map(                                                         #map lambda function
                    lambda pair: (
                        euclidean_distance(graph.nodes[pair[0]], goal_coords),
                        path + [pair[0]]
                    ),
                    unvisited
                )

                for item in scored_paths:
                    frontier.put(item)


    
    