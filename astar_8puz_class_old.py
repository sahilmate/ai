import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

class Puzzle:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.g = parent.g + 1 if parent else 0
        self.h = self.heuristic()
        self.f = self.g + self.h

    def __lt__(self, other):  # For priority queue
        return self.f < other.f

    def heuristic(self):  # Count misplaced tiles
        return sum(1 for i in range(3) for j in range(3)
                   if self.board[i][j] != 0 and self.board[i][j] != goal_state[i][j])

    def is_goal(self):
        return self.board == goal_state

    def get_moves(self):
        moves = []
        x, y = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0][0]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                moves.append(Puzzle(new_board, self))
        return moves

def a_star(start):
    open_list = []
    heapq.heappush(open_list, start)
    visited = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            path = []
            while current:
                path.append(current)
                current = current.parent
            return path[::-1]

        visited.add(tuple(map(tuple, current.board)))

        for move in current.get_moves():
            if tuple(map(tuple, move.board)) not in visited:
                heapq.heappush(open_list, move)
    return None

# Input from user
def input_board():
    print("Enter puzzle (use 0 for empty):")
    return [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]

if __name__ == "__main__":
    start_board = input_board()
    start_state = Puzzle(start_board)
    result = a_star(start_state)

    if result:
        print(f"\nSolved in {len(result)-1} moves.\n")
        for i, step in enumerate(result):
            print(f"Step {i}:")
            for row in step.board:
                print(row)
            print(f"h = {step.h}, g = {step.g}, f = {step.f}\n")
    else:
        print("No solution found.")