class DFS:
    def search(self, graph, origin, destination):
        stack = [[origin]] # Origin is the starting point. Hence, it is the first element in the stack
        visited = set()

        while stack:
            path = stack.pop()
            current = path[-1]

            if current in destination:
                return path, self.calculate_cost(graph, path)

            if current not in visited:
                visited.add(current)

                for neighbor, _ in graph.neighbors(current):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        stack.append(new_path)

    # Calculate the total cost of the path from origin to destination
    def calculate_cost(self, graph, path):
        total = 0
        for i in range(len(path) - 1):
            total += graph.path_cost(path[i], path[i + 1])
        return total


    