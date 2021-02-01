class Vertex:
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.neighbourList = {}

    def add_neighbour(self, n):
        self.neighbourList.update({self.name: n})
        print(self.neighbourList)

class Graph(Vertex):
    def __init__(self):
        # self.vertexlist = [self.neighbourList]
        counter = 0

    def add_connection(self, a, b, c):
        self.vertexList[a].add_neighbor(b, c)


S = Vertex('S')
S.add_neighbour('B')
S.add_neighbour('C')
S.add_neighbour('A')

A = Vertex('A')
A.add_neighbour('E')
A.add_neighbour('D')

B = Vertex('B')
B.add_neighbour('G')
B.add_neighbour('F')

C = Vertex('C')
C.add_neighbour('H')

D = Vertex('D')

E = Vertex('E')

F = Vertex('F')

G = Vertex('G')

K = Vertex('K')

L = Vertex('L')

M = Vertex('M')

I = Vertex('I')
I.add_neighbour('K')
I.add_neighbour('L')
I.add_neighbour('M')

H = Vertex('H')
H.add_neighbour('J')
H.add_neighbour('I')

J = Vertex('J')


g = Graph()
g.add_connection('S', 'A', 3)
g.add_connection('S', 'B', 6)
g.add_connection('S', 'C', 5)
g.add_connection('A', 'E', 8)
g.add_connection('A', 'D', 9)
g.add_connection('B', 'F', 12)
g.add_connection('B', 'G', 14)
g.add_connection('C', 'H', 7)
g.add_connection('H', 'J', 6)
g.add_connection('H', 'I', 5)
g.add_connection('I', 'K', 1)
g.add_connection('I', 'L', 10)
g.add_connection('I', 'M', 2)
