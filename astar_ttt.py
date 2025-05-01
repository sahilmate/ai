#Implement A* Algorithm for any game search problem. (TicTacToe)
import copy
import heapq

class Node:
    def __init__(self, board, player, depth=0):
        self.board = board
        self.player = player
        self.depth = depth
        self.cost = self.heuristic()

    def heuristic(self):
        # Basic heuristic: +10 for win, -10 for loss, 0 otherwise
        winner = check_winner(self.board)
        if winner == 'X':
            return -10 + self.depth  # 'X' is us, so less cost if we win
        elif winner == 'O':
            return 10 + self.depth   # More cost if opponent wins
        else:
            return self.depth

    def __lt__(self, other):
        return self.cost < other.cost

def check_winner(board):
    win_states = [(0,1,2), (3,4,5), (6,7,8),
                  (0,3,6), (1,4,7), (2,5,8),
                  (0,4,8), (2,4,6)]
    for i,j,k in win_states:
        if board[i] == board[j] == board[k] and board[i] != ' ':
            return board[i]
    return None

def is_full(board):
    return all(cell != ' ' for cell in board)

def generate_children(node):
    children = []
    for i in range(9):
        if node.board[i] == ' ':
            new_board = node.board[:]
            new_board[i] = node.player
            next_player = 'O' if node.player == 'X' else 'X'
            child = Node(new_board, next_player, node.depth + 1)
            children.append(child)
    return children

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')
    print()

def best_move(current_board, current_player):
    root = Node(current_board, current_player)
    best_child = None
    min_cost = float('inf')

    for child in generate_children(root):
        if child.cost < min_cost:
            min_cost = child.cost
            best_child = child

    return best_child.board if best_child else current_board


def main():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print("Winner:", winner)
            break
        if is_full(board):
            print("Draw!")
            break

        if current_player == 'X':
            move = int(input("Enter position (0-8): "))
            if board[move] != ' ':
                print("Invalid move!")
                continue
            board[move] = 'X'
        else:
            print("Computer is thinking...")
            board = best_move(board, 'O')

        current_player = 'O' if current_player == 'X' else 'X'

main()
