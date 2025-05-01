#Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

# Building the graph
graph = {}

print("Enter number of nodes:")
n = int(input())

print("Enter number of edges:")
e = int(input())

print("Enter the edges (node1 node2):")
for _ in range(e):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Since the graph is undirected

# Recursive DFS
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Recursive BFS
def bfs(graph, queue, visited):
    if not queue:
        return
    node = queue.pop(0)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
    bfs(graph, queue, visited)

print("Enter starting node for traversal:")
start_node = input()

# DFS Traversal
print("\nDFS Traversal:")
visited_dfs = []
dfs(graph, start_node, visited_dfs)

# BFS Traversal
print("\nBFS Traversal:")
visited_bfs = [start_node]
queue_bfs = [start_node]
bfs(graph, queue_bfs, visited_bfs)

#output: edges=5, nodes = 4
#edges a b , a c, b d, c e
