from itertools import starmap

class DFS:
    def search(self, graph, origin, destination):
        stack = [[origin]]                                                          # Origin is the starting point. Hence, it is the first element in the stack
        visited = set()

        while stack:
            path = stack.pop()                                                      #pop is used for getting the last element LIFO 
            current = path[-1]

            if current in destination:                                              
                return path

            if current not in visited:
                visited.add(current)

               # getting neighbors and filtering visited from unvisited using starmap for tuple unpacking
                neighbors = sorted(graph.neighbors(current))                        #sorted is used for taking the right order when everything is equal
                unvisited = filter(lambda pair: pair[0] not in visited, neighbors)  # filter out where function is false
                new_paths = map(lambda pair: path + [pair[0]], unvisited)           # lambda fucntion maps to all iterables
                stack.extend(new_paths)
