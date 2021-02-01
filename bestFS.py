class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighborList = {}

    def addneighbor(self, n, c):
        self.neighbortList[n] = c


class Graph:
    def __init__(self):
        self.vertexList = []
        self.count = 0

    def add_Vertex(self, v):
        obj = Vertex(v)
        self.vertexList[v] = obj

    def addEdge(self, v1, v2, cost):
        self.vertexList[v1].addneighbor(v2, cost)


g = Graph()

S = Vertex('S')
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')
K = Vertex('K')
L = Vertex('L')
M = Vertex('M')
I = Vertex('I')
H = Vertex('H')
J = Vertex('J')

g.add_Vertex(S)
g.add_Vertex(A)
g.add_Vertex(B)
g.add_Vertex(C)
g.add_Vertex(D)
g.add_Vertex(E)
g.add_Vertex(F)
g.add_Vertex(G)
g.add_Vertex(K)
g.add_Vertex(L)
g.add_Vertex(M)
g.add_Vertex(I)
g.add_Vertex(H)
g.add_Vertex(J)

g.addEdge(S, A, 3)
g.addEdge(S, B, 6)
g.addEdge(S, C, 5)
g.addEdge(A, D, 9)
g.addEdge(A, E, 8)
g.addEdge(B, F, 12)
g.addEdge(B, G, 14)
g.addEdge(C, H, 7)
g.addEdge(H, I, 5)
g.addEdge(H, J, 6)
g.addEdge(I, K, 1)
g.addEdge(I, L, 10)
g.addEdge(I, M, 2)



