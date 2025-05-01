# Greedy Selection Sort using Selection Sort Algorithm

# Function to perform selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum element is at the current position
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# User Input
print("Enter number of elements:")
n = int(input())

# Ensure user enters the correct number of elements
while True:
    print(f"Enter exactly {n} elements (space separated):")
    arr = list(map(int, input().split()))
    if len(arr) == n:
        break
    else:
        print(f"Error: Please enter exactly {n} elements.")

# Sorting using greedy approach
sorted_arr = selection_sort(arr)

# Output
print("\nSorted array using Greedy Selection Sort:")
print(*sorted_arr)
