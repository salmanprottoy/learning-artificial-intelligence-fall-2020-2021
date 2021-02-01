from collections import defaultdict


class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function to perform a Depth-Limited search

    # from given source 'src'
    def DLS(self, source, tgt, max_depth):

        if source == tgt:
            return True

        # If reached the maximum depth, stop recursing.
        if max_depth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[source]:
            if self.DLS(i, tgt, max_depth - 1):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, source, tgt, max_depth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(max_depth):
            if self.DLS(source, tgt, i):
                return True
        return False


# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

target = 6
maxDepth = 3
src = 0



if g.IDDFS(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")
