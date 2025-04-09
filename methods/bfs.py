from collections import deque

class BFS:
    def search(self, graph, origin, destination):
        queue = deque([[origin]])                                                   # deque can remove from end as well which helps in simulating FIFO
        visited = set()

        while queue:
            path = queue.popleft()                                                  #Simulating FIFO. Gets the first element entered
            current = path[-1]

            if current in destination:
                return path

            if current not in visited:
                visited.add(current)

                #getting neighbors and filtering visited from unvisitied streamlined
                neighbors = sorted(graph.neighbors(current))  
                unvisited = filter(lambda pair: pair[0] not in visited, neighbors) #filter out where funtion is false 
                new_paths = map(lambda pair: path + [pair[0]], unvisited) #maps lambda function to all iterables 
                queue.extend(new_paths)