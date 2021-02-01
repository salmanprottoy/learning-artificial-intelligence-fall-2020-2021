import queue

# Node data structure
class Vertex:

    def __init__(self, label):
        self.out_edges = []
        self.label = label
        self.is_goal = False


    def add_edge(self, node, weight = 0):
        self.out_edges.append(Edge(node, weight))


# Edge data structure
class Edge:

    def __init__(self, node, weight = 0):
        self.node = node
        self.weight = weight

    def to(self):
        return self.node


# Graph data structure, utilises classes Node and Edge
class Graph:

    def __init__(self):
        self.nodes = []


def ucs(G, v):
    visited = set()                  # set of visited nodes
    visited.add(v)                   # mark the starting vertex as visited
    q = queue.PriorityQueue()        # we store vertices in the (priority) queue as tuples with cumulative cost
    q.put((0, v))                    # add the starting node, this has zero *cumulative* cost
    goal_node = None                 # this will be set as the goal node if one is found
    parents = {v: None}               # this dictionary contains the parent of each node, necessary for path construction

    while not q.empty():             # while the queue is nonempty
        dequeued_item = q.get()
        current_node = dequeued_item[1]             # get node at top of queue
        current_node_priority = dequeued_item[0]    # get the cumulative priority for later

        if current_node.is_goal:                    # if the current node is the goal
            path_to_goal = [current_node]           # the path to the goal ends with the current node (obviously)
            prev_node = current_node                # set the previous node to be the current node (this will changed with each iteration)

            while prev_node != v:                   # go back up the path using parents, and add to path
                parent = parents[prev_node]
                path_to_goal.append(parent)
                prev_node = parent

            path_to_goal.reverse()                  # reverse the path
            return path_to_goal                     # return it

        else:
            for edge in current_node.out_edges:     # otherwise, for each adjacent node
                child = edge.to()                   # (avoid calling .to() in future)

                if child not in visited:            # if it is not visited
                    visited.add(child)              # mark it as visited
                    parents[child] = current_node   # set the current node as the parent of child
                    q.put((current_node_priority + edge.weight, child))

