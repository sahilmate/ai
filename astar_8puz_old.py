#Implement A* Algorithm for any game search problem.
import heapq

# Goal state for 8-puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the empty tile

# Calculate Manhattan Distance Heuristic
def calculate_heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_x, target_y = divmod(state[i][j] - 1, 3)
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

# Find empty tile position (returns coordinates of 0)
def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all valid neighbors by moving empty tile
def get_neighbors(state):
    neighbors = []
    x, y = find_empty_tile(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Check if current state is the goal
def is_goal_state(state):
    return state == goal_state

# A* Search implementation
def a_star(start_state):
    open_set = []
    heapq.heappush(open_set, (calculate_heuristic(start_state), 0, start_state))
    
    parents = {tuple(map(tuple, start_state)): None}
    g_scores = {tuple(map(tuple, start_state)): 0}

    while open_set:
        _, g, current_state = heapq.heappop(open_set)

        if is_goal_state(current_state):
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = parents[tuple(map(tuple, current_state))]
            return path[::-1]  # Return reversed path

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            g_score = g + 1

            if neighbor_tuple not in g_scores or g_score < g_scores[neighbor_tuple]:
                g_scores[neighbor_tuple] = g_score
                parents[neighbor_tuple] = current_state
                f_score = g_score + calculate_heuristic(neighbor)
                heapq.heappush(open_set, (f_score, g_score, neighbor))

    return None  # No solution found

# Main function
def main():
    print("Enter the start state (row by row, use 0 for the empty tile):")
    start_state = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        start_state.append(row)

    solution = a_star(start_state)

    if solution:
        print(f"\nSolution found in {len(solution) - 1} moves:")
        for step, state in enumerate(solution):
            print(f"\nStep {step} (Heuristic cost: {calculate_heuristic(state)}):")
            for row in state:
                print(row)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
