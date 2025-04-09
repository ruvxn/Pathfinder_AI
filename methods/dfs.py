class DFS:
    def search(self, graph, origin, destination):
        stack = [[origin]] # Origin is the starting point. Hence, it is the first element in the stack
        visited = set()

        while stack:
            path = stack.pop()
            current = path[-1]

            if current in destination:
                return path

            if current not in visited:
                visited.add(current)

                for neighbor, _ in sorted(graph.neighbors(current)):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        stack.append(new_path)

  

    