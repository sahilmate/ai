#Implement Greedy search algorithm for any of the following application: Prim's Minimal Spanning Tree Algorithm (Consider Starting index as 1)

# Prim's Algorithm implementation using adjacency matrix
INF = float('inf')

# Get number of vertices
V = int(input("Enter the number of vertices: "))

# Initialize an empty adjacency matrix
graph = [[0] * V for _ in range(V)]

# Get the edges and weights
E = int(input("Enter the number of edges: "))
print("Enter the edges in the format: vertex1 vertex2 weight")

for _ in range(E):
    u, v, weight = map(int, input().split())
    graph[u-1][v-1] = weight
    graph[v-1][u-1] = weight  # Since it's an undirected graph

def prim_mst(graph):
    selected = [False] * V
    no_edge = 0
    selected[0] = True  # Start from vertex 1 (index 0)

    print("Edge : Weight")

    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f"{x+1} - {y+1} : {graph[x][y]}")
        selected[y] = True
        no_edge += 1

prim_mst(graph)
#output: vertices 6, edges 9
#edges = 1 4 1, 1 5 4, 1 2 2, 4 5 9, 4 3 5, 4 2 3, 2 3 3, 2 6 7, 3 6 8