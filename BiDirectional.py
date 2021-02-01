class Graph:
    graph = {}

    # Constractor
    def __init__(self):
        self.reader()

    # Reading the graph.txt file line by line
    def reader(self):
        with open('graph.txt', 'r') as file:
            for line in file:
                line = line.split(', ')             # Spliting inputs
                line1 = line[1].split('\n')         # Spliting inputs

                # Creating list of connections in graph
                if line[0] in self.graph:
                    temp = self.graph[line[0]]
                    temp = temp+","+line1[0]
                    self.graph[line[0]] = temp
                else:
                    self.graph[line[0]] = line1[0]

graph = Graph().ghrap