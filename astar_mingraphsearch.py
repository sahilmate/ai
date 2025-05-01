#Implement A* Algorithm for Graph search (Minimum cost)
import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}
    """Add an edge between source and destination with given cost"""    
    def add_edge(self, source, destination, cost): 
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append((destination, cost))
    """Set the heuristic value for a node"""
    def set_heuristic(self, node, heuristic_value):
        self.heuristics[node] = heuristic_value
    """Get all neighbors of a node"""    
    def get_neighbors(self, node):
        if node not in self.edges:
            return []
        return self.edges[node]
    """Get the heuristic value for a node"""
    def get_heuristic(self, node):
        return self.heuristics.get(node, 0)

def a_star_search(graph, start, goal):
    # Priority queue to store nodes to explore: (f_score, node, path, cost)
    open_list = [(graph.get_heuristic(start), start, [start], 0)]
    heapq.heapify(open_list)
    closed_set = set() # Set of nodes already evaluated
    while open_list:
        f, current, path, cost = heapq.heappop(open_list) # Get the node with the lowest f_score 
        # If we've reached our goal, return the path and cost
        if current == goal:
            return path, cost    
        if current in closed_set:
            continue    
        closed_set.add(current)
        for neighbor, edge_cost in graph.get_neighbors(current):
            if neighbor in closed_set:
                continue
            new_cost = cost + edge_cost
            new_path = path + [neighbor]
            
            # Calculate f_score = g_score (cost so far) + h_score (heuristic)
            f_score = new_cost + graph.get_heuristic(neighbor)
            heapq.heappush(open_list, (f_score, neighbor, new_path, new_cost))
    return None, None

def main():
    print("A* Algorithm for Graph Search (Minimum Cost)")
    # Create a new graph
    graph = Graph()
    
    # Get nodes from user
    print("\nEnter the nodes (separated by spaces):")
    nodes = input().split()
    
    # Get heuristic values for each node
    print("\nEnter heuristic values for each node (separated by spaces):")
    print(f"Order of nodes: {' '.join(nodes)}")
    heuristics = list(map(int, input().split()))
    
    # Set heuristic values in the graph
    for node, heuristic in zip(nodes, heuristics):
        graph.set_heuristic(node, heuristic)
    
    # Get edges from user
    print("\nEnter the number of edges:")
    num_edges = int(input())
    
    print("\nEnter edges in format 'source destination cost':")
    for i in range(num_edges):
        source, dest, cost = input(f"Edge {i+1}: ").split()
        graph.add_edge(source, dest, int(cost))
    
    # Get start and goal nodes
    print("\nAvailable nodes:", ", ".join(nodes))
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")
    
    # Run A* search
    path, cost = a_star_search(graph, start_node, goal_node)
    if path:
        print("\nPath found:", " -> ".join(path))
        print("Total cost:", cost)
        print("\nStep-by-step evaluation:")
        current_cost = 0
        for i in range(len(path)-1):
            for neighbor, edge_cost in graph.get_neighbors(path[i]):
                if neighbor == path[i+1]:
                    current_cost += edge_cost
                    break
            print(f"{path[i]} -> {path[i+1]}: Cost = {current_cost}, Heuristic = {graph.get_heuristic(path[i+1])}, f = {current_cost + graph.get_heuristic(path[i+1])}")
    else:
        print("\nNo path found between", start_node, "and", goal_node)

if __name__ == "__main__":
    main()
#nodes a b c d e f z
#heuristics 14 12 11 6 4 11 0
#edges 10, a b 4, a c 3, b f 5,b c 12, c d 7, c e 10, d e 2, e b 12, e z 5, f z 16