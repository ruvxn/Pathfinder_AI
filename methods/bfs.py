from collections import deque

class BFS:
    def search(self, graph, origin, destination):
        queue = deque([[origin]])
        visited = set()

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current in destination:
                return path, self.calculate_cost(graph, path)

            if current not in visited:
                visited.add(current)

                for neighbor, _ in sorted(graph.neighbors(current)):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        queue.append(new_path)

    def calculate_cost(self, graph, path):
        total = 0
        for i in range(len(path) - 1):
            total += graph.path_cost(path[i], path[i + 1])
        return total
