#Implement A* Algorithm for any game search problem. (8Puzzle)
import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.g = parent.g + 1 if parent else 0
        self.h = self.calculate_heuristic()
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def is_goal(self):
        return self.h == 0

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        goal_state = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]
        
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] != 0:
                    # Find where this value should be in the goal state
                    target_x, target_y = divmod(self.puzzle[i][j] - 1, 3)
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def get_children(self):
        children = []
        # Find the empty tile
        empty_pos = None
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    empty_pos = (i, j)
                    break
            if empty_pos:
                break
                
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for move in moves:
            new_pos = (empty_pos[0] + move[0], empty_pos[1] + move[1])
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[empty_pos[0]][empty_pos[1]], new_puzzle[new_pos[0]][new_pos[1]] = \
                    new_puzzle[new_pos[0]][new_pos[1]], new_puzzle[empty_pos[0]][empty_pos[1]]
                children.append(PuzzleState(new_puzzle, self, move))
        return children

def astar(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_state.puzzle)))

        for child in current_state.get_children():
            if tuple(map(tuple, child.puzzle)) not in closed_set:
                heapq.heappush(open_list, child)

    return None

def get_puzzle_from_user(prompt):
    print(prompt)
    return [list(map(int, input(f"Enter row {i + 1} (separated by space): ").split())) for i in range(3)]

if __name__ == "__main__":
    initial_puzzle = get_puzzle_from_user("Enter the initial state of the puzzle:")
    initial_state = PuzzleState(initial_puzzle)
    solution = astar(initial_state)

    if solution:
        print("\nSolution found in", len(solution)-1, "moves:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in state.puzzle:
                print(row)
            print(f"Heuristic (h) = {state.h}, Cost so far (g) = {state.g}, Total (f) = {state.f}")
            print()
    else:
        print("No solution found.")