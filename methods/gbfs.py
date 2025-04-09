from utils.heuristics import euclidean_distance
from queue import PriorityQueue

class GBFS:

    def get_goal_coordinates(self, graph, destination):
        for dest in destination:
            return graph.nodes[dest]
        

    def search(self, graph, origin, destination):
        frontier = PriorityQueue()
        frontier.put((0, [origin]))
        visited = set()
        goal_coords = self.get_goal_coordinates(graph, destination)

        while not frontier.empty():
            h_score, path = frontier.get()
            current = path[-1]

            if current in destination:
                return path

            if current not in visited:
                visited.add(current)

                for neighbor, _ in sorted(graph.neighbors(current)):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        h = euclidean_distance(graph.nodes[neighbor], goal_coords)
                        frontier.put((h, new_path))

    
    