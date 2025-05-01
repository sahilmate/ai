#Implement Greedy search algorithm for any of the following application: Dijkstra's Algorithm.

import heapq

def dijkstra(graph, start):
    # Initialize distance dictionary with infinity for all vertices and 0 for start
    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0
    
    # Dictionary to store the previous vertex in the shortest path
    prev = {vertex: None for vertex in graph}
    
    # Priority queue to store vertices to be processed
    priority_queue = [(0, start)]
    
    # Set to keep track of visited vertices
    visited = set()
    
    while priority_queue:
        # Get the vertex with the smallest distance
        current_dist, current_vertex = heapq.heappop(priority_queue)
        
        # If we've already processed this vertex, skip it
        if current_vertex in visited:
            continue
            
        # Mark current vertex as visited
        visited.add(current_vertex)
        
        # If the current distance is greater than the one we have, skip
        if current_dist > dist[current_vertex]:
            continue
            
        # Check all neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate tentative distance
            distance = current_dist + weight
            
            # If we found a shorter path to the neighbor, update it
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist, prev

def get_path(prev, target):
    """
    Reconstruct path from start to target using prev dictionary
    
    Args:
        prev: Dictionary of previous vertices in the shortest path
        target: Target vertex
        
    Returns:
        Path from start to target as a list
    """
    path = []
    current = target
    
    # Traverse from target back to start
    while current is not None:
        path.append(current)
        current = prev[current]
        
    # Reverse to get path from start to target
    return path[::-1]

def get_graph_input():
    """Get graph input from the user"""
    print("Enter the number of vertices in the graph:")
    num_vertices = int(input())
    
    print("Enter the vertices (separated by spaces):")
    vertices = input().split()
    
    # Initialize empty graph
    graph = {vertex: {} for vertex in vertices}
    
    print("Enter the number of edges:")
    num_edges = int(input())
    
    print("Enter the edges in the format 'source destination weight':")
    for i in range(num_edges):
        source, dest, weight = input(f"Edge {i+1}: ").split()
        weight = int(weight)
        graph[source][dest] = weight
        graph[dest][source] = weight  # For undirected graph
    
    return graph, vertices

def main():
    print("Dijkstra's Shortest Path Algorithm")
    # Get graph input from user
    graph, vertices = get_graph_input()
    
    print("\nEnter the starting vertex:")
    start_vertex = input()
    
    if start_vertex not in vertices:
        print("Invalid starting vertex!")
        return
    
    # Apply Dijkstra's algorithm
    distances, previous = dijkstra(graph, start_vertex)
    
    # Display the result
    print("\nShortest distances from vertex", start_vertex)
    print("Vertex\tDistance\tPath")
    for vertex in vertices:
        if vertex == start_vertex:
            continue
        path = get_path(previous, vertex)
        path_str = " -> ".join(path)
        print(f"{vertex}\t{distances[vertex]}\t\t{path_str}")

if __name__ == "__main__":
    main()
#vertices = 6,a b c d e f , edges = 9
#edges = a b 4, a c 5, b c 11, b d 9, b e 7, c e 3, d e 2, d f 2, e f 6