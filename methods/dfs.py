from itertools import starmap

class DFS:
    def search(self, graph, origin, destination):
        stack = [[origin]]                                                          # Origin is the starting point. Hence, it is the first element in the stack
        visited = set()

        while stack:
            path = stack.pop()                                                      #pop is used for getting the last element LIFO
            current = path[-1]

            if current in destination:
                visited.add(current)                                                # if current is in destination, add it to visited
                return path, visited # the path to the destination and visited nodes

            if current not in visited:
                visited.add(current)

               # getting neighbors and filtering visited from unvisited using starmap for tuple unpacking
                neighbors = sorted(graph.neighbors(current))                        #sorted is used for taking the right order when everything is equal
                unvisited = filter(lambda pair: pair[0] not in visited, neighbors)  # filter out where function is false
                new_paths = map(lambda pair: path + [pair[0]], unvisited)           # lambda fucntion maps to all iterables
                stack.extend(new_paths)

        return None, visited # viqsited nodes and exceptioin when no path was found
