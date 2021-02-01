
def dfs(graph_needed, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph_needed[start] - visited:
        dfs(graph_needed, next_node, visited)
    return visited


graph = {

    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'F']),
    'C': set(['A', 'E']),
    'D': set(['B', 'I']),
    'E': set(['C', 'F', 'G']),
    'F': set(['B', 'E', 'G']),
    'G': set(['F', 'K']),
    'I': set(['K']),
    'K': set(['I', 'G'])
}

dfs(graph, 'A')
