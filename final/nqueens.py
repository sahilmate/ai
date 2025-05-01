#Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem.
   
def is_safe(board, row, col):
    # Bounding: Checking if the column is already occupied
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Bounding: Checking left diagonal
    max_left = min(row, col)
    for i in range(1, max_left + 1):
        if board[row - i][col - i] == 'Q':
            return False

    # Bounding: Checking right diagonal
    max_right = min(row, len(board) - 1 - col)
    for i in range(1, max_right + 1):
        if board[row - i][col + i] == 'Q':
            return False

    return True

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n" + "_" * (2 * len(board) - 1) + "\n")

def solve(board, row, solutions):
    if row == len(board):  # Base case: all queens placed
        solutions.append([row[:] for row in board])  # Store a copy of the board
        print_board(board)  # Print the board
        return

    for col in range(len(board)):  # Branching: Trying all columns
        if is_safe(board, row, col):  # Pruning: Only proceed if safe
            board[row][col] = 'Q'
            solve(board, row + 1, solutions)  # Recursive call for next row
            board[row][col] = '_'  # Backtracking: Undo move for next possibility

if __name__ == "__main__":
    try:
        n = int(input("Enter value of N: "))
        
        if n<=0:
            print("N should be a positive integer.")
        elif n ==2 or n == 3:
            print(f"No solution exists for N = {n}")
        else:
            print(f"Solutions for N = {n}:")
            board = [['_'] * n for _ in range(n)]
            solutions = []
            solve(board, 0, solutions)
            print(f"Total Solutions: {len(solutions)}") 
    
            if len(solutions) == 0:
                print("No solution exists")            
        
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
    
    