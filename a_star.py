graph = {

    "Arad": {"Timisoara": 118, "Sibiu": 140,"Zerind": 75},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia":70},
    "Mehadia": {"Lugoj": 70, "Dobreta": 75},
    "Dobreta": {"Mehadia":75, "Craiova":120},
    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80},
    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99},
    "Fagaras": {"Sibiu": 99, "Bucharest":211},
    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87}

}

heuristic= {"Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Eforie": 161, "Fagaras": 178, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesi": 98, "RimnicuVilcea": 193, "Sibiu": 253, "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
                }

class graphProblem:

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        return list(self.graph[state].keys())

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + self.graph[state1][state2]

class Node:

    def __init__(self, state, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, graphProblem):
        return [self.child_node(graphProblem, action)
                for action in graphProblem.actions(self.state)]

    def child_node(self, graphProblem, action):
        next_state=graphProblem.result(self.state, action)
        return Node(next_state, self, action,
                    graphProblem.path_cost(self.path_cost, self.state, action, next_state))

    def path(self):
        node, path_back = self, []

        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def solution(self):
        return [node.action for node in self.path()[1:]]

class Queue:

    def __init__(self, pop_index):
        self.queue = []
        self.pop_index = pop_index

    def append(self, item):
        self.queue.append(item)

    def sortAppend(self, item,f):
        self.queue.append(item)
        self.queue.sort(key = f)

    def extend(self, items):
        self.queue.extend(items)

    def pop(self):

        if len(self.queue) > 0:
            return self.queue.pop(self.pop_index)
        else:
            raise Exception('FIFO Queue is empty')

    def printQueue(self):

        def __len__(self):
            return len(self.queue)

    def __contains__(self, item):
        return item in self.queue

def graph_search(problem, pop_index):

    node = Node(problem.initial)
    if problem.goal_test(node.state): return node
    frontier = Queue(pop_index)
    explored = set()
    frontier.append(node)

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        explored.add(node.state)

        for child in node.expand(problem):
            if problem.goal_test(child.state): return child
            if child.state not in explored and child not in frontier: frontier.append(child)

    return None

def best_first_search(problem, f, pop_index = 0):

    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return state

    frontier = Queue(pop_index)
    frontier.sortAppend(node, f)
    explored = set()

    while frontier:

        frontier.printQueue()
        node = frontier.pop()

        if problem.goal_test(node.state):
            return node
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.sortAppend(child, f)
    return None

def astar(problem):
    return best_first_search(problem, lambda node:node.path_cost + heuristic[node.state])

gp = graphProblem("Arad", "Bucharest", graph)
ngp = astar(gp)
listSol = list(ngp.solution())
for i in listSol:
    print(i,' ')
print('Cost:', ngp.path_cost)
