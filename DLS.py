from collections import defaultdict

class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_limited_search(self, root, tgt, level):

        if root == tgt:
            return True

        if level <= 0:
            return False

        for i in self.graph[root]:
            if self.depth_limited_search(i, tgt, level - 1):
                return True
        return False

    def IDDFS(self, root, tgt, level):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(level):
            if self.depth_limited_search(root, tgt, i):
                return True
        return False


g = Graph(8)

# Adding Edge
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('D', 'G')
g.add_edge('B', 'C')
g.add_edge('B', 'F')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'H')

# Tgt Vertex
target = 'H'
# Maximum Depth
level = 3
# root vertex
root = 'A'


if g.IDDFS(root, target, level):
    print("Target is reachable from source ")
else:
    print("Target is NOT reachable from source")





























