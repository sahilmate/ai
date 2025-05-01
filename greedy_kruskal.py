#Implement Greedy search algorithm for any of the following application: Kruskal's Minimal Spanning Tree Algorithm

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, vertex):
        """Find the root/representative of the set containing vertex"""
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        """Union of two sets containing vertex1 and vertex2"""
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 != root2:
            # Union by rank
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_mst(graph):
    """
    Implementation of Kruskal's algorithm to find the Minimum Spanning Tree
    
    Args:
        graph: A list of edges in the format (vertex1, vertex2, weight)
        
    Returns:
        The minimum spanning tree as a list of edges and the total weight
    """
    # Extract all vertices from the graph
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])
    
    # Sort all the edges in non-decreasing order of their weight
    graph.sort(key=lambda edge: edge[2])
    
    # Initialize disjoint set
    disjoint_set = DisjointSet(vertices)
    
    mst = []
    total_weight = 0
    
    # Process edges one by one
    for edge in graph:
        vertex1, vertex2, weight = edge
        
        # Check if including this edge creates a cycle
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            # Include this edge in MST
            mst.append(edge)
            total_weight += weight
            disjoint_set.union(vertex1, vertex2)
    
    return mst, total_weight

def get_graph_input():
    """Get graph input from the user"""
    print("Enter the number of vertices in the graph:")
    num_vertices = int(input())
    
    print("Enter the number of edges in the graph:")
    num_edges = int(input())
    
    print("Enter the edges in the format 'vertex1 vertex2 weight':")
    print("(Vertices can be any value - numbers, letters, etc.)")
    
    graph = []
    for i in range(num_edges):
        input_line = input(f"Edge {i+1}: ")
        vertex1, vertex2, weight = input_line.split()
        # Convert weight to integer, keep vertices as they are
        graph.append((vertex1, vertex2, int(weight)))
    
    return graph

def main():
    print("Kruskal's Minimum Spanning Tree Algorithm")
    print("----------------------------------------")
    
    # Get graph input from user
    graph = get_graph_input()
    
    # Apply Kruskal's algorithm
    mst, total_weight = kruskal_mst(graph)
    
    # Display the result
    print("\nMinimum Spanning Tree:")
    print("Edge \tWeight")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]} \t{edge[2]}")
    
    print(f"\nTotal Weight of MST: {total_weight}")

if __name__ == "__main__":
    main()
    
#vertices = 9, edges = 14
#edges = 0 1 4, 0 7 8, 1 2 8, 1 7 11, 2 3 7, 2 5 4, 2 8 2, 3 4 9, 3 5 14, 4 5 10, 5 6 2, 6 7 1, 6 8 6, 7 8 7