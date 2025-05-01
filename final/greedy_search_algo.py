#Implement Greedy search algorithm
def greedy_search(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start, [start])]  # (h, node, path)
    visited = set()
    while open_list:
        # Sort the open list based on the heuristic value (smallest first)
        open_list.sort()
        h, current_node, path = open_list.pop(0)
        
        print(f"Visiting: {current_node} (heuristic = {h})")
        
        if current_node == goal:
            return path
        
        visited.add(current_node)
        neighbors = graph.get(current_node, []) # Show neighbors being considered
        if neighbors:
            print(f"  Neighbors of {current_node}:", end=" ")
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    print(f"{neighbor}(h={heuristic[neighbor]})", end=" ")
            print()
        
        for neighbor, cost in neighbors:
            if neighbor not in visited:
                open_list.append((heuristic[neighbor], neighbor, path + [neighbor]))
    
    return None

graph = {}
num_edges = int(input("Enter number of edges: "))
print("Enter edges in the format: from_node to_node cost")

for _ in range(num_edges):
    u, v, cost = input().split()
    cost = int(cost)
    if u not in graph:
        graph[u] = []
    graph[u].append((v, cost))

heuristic = {}
num_nodes = int(input("Enter number of nodes: "))
print("Enter node and its heuristic value (format: node heuristic)")

for _ in range(num_nodes):
    node, h = input().split()
    heuristic[node] = int(h)

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

path = greedy_search(graph, heuristic, start_node, goal_node)

if path:
    print("Greedy path:", " -> ".join(path))
    print("Path length:", len(path)-1)
else:
    print("No path found from", start_node, "to", goal_node)
    
#edges = 7, a b 4, a c 3, b f 5, c d 7, c e 10, e z 5, f z 16
#nodes 7, a 14, b 12, c 11,d 6,e 4, f 11, z 0