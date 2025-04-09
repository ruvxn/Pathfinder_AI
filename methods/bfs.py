from collections import deque

class BFS:
    def search(self, graph, origin, destination):
        queue = deque([[origin]])
        visited = set()

        while queue:
            path = queue.popleft()
            current = path[-1]

            if current in destination:
                return path

            if current not in visited:
                visited.add(current)

                for neighbor, _ in sorted(graph.neighbors(current)):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        queue.append(new_path)

   