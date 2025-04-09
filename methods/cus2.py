from utils.heuristics import euclidean_distance
from queue import PriorityQueue
from itertools import count  # Added for tie-breaker

class CUS2:
    def search(self, graph, origin, destinations):
        counter = count()  # Counter to maintain insertion order
        frontier = PriorityQueue()
        frontier.put(((0, next(counter), 0), [origin]))  # (steps, counter, heuristic), path
        visited = set()

        while not frontier.empty():
            (priority, path) = frontier.get()
            (steps, _, _) = priority  # unpack priority tuple properly
            current_node = path[-1]

            if current_node in destinations:
                return path, self.calculate_cost(graph, path)

            if current_node not in visited:
                visited.add(current_node)

                for neighbor, _ in sorted(graph.neighbors(current_node)):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        goal_coords = self.get_goal_coordinates(graph, destinations, neighbor)
                        heuristic = euclidean_distance(graph.nodes[neighbor], goal_coords)
                        steps = len(new_path) - 1  # moves made so far
                        priority = (steps, next(counter), heuristic)
                        frontier.put((priority, new_path))

        return None, float('inf')

    def get_goal_coordinates(self, graph, destinations, current_node):
        current_coords = graph.nodes[current_node]
        closest_dest = min(
            destinations,
            key=lambda dest: euclidean_distance(current_coords, graph.nodes[dest])
        )
        return graph.nodes[closest_dest]

    def calculate_cost(self, graph, path):
        total = 0
        for i in range(len(path) - 1):
            total += graph.path_cost(path[i], path[i + 1])
        return total
