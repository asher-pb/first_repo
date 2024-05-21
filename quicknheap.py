import sys

# Swap function
def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]

# Quicksort partition function
def partition(arr, start, end):
    pivot = arr[end]
    smaller_idx = start
    for current_idx in range(start, end):
        if (arr[current_idx][1], arr[current_idx][0]) <= (pivot[1], pivot[0]):
            swap(arr, current_idx, smaller_idx)
            smaller_idx += 1
    swap(arr, end, smaller_idx)
    return smaller_idx

# Recursive quicksort function
def _quicksort(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)
        _quicksort(arr, start, pivot_idx - 1)
        _quicksort(arr, pivot_idx + 1, end)

# Quicksort wrapper function
def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

# Heapify function for heapsort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and (arr[left][1], arr[left][0]) > (arr[largest][1], arr[largest][0]):
        largest = left
    if right < n and (arr[right][1], arr[right][0]) > (arr[largest][1], arr[largest][0]):
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)

# Heapsort function
def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)

# Main function
if len(sys.argv) != 3:
    print("Usage: python3 sortNames.py [-quick | -heap] <file_name>")
    sys.exit(1)

sort_method = sys.argv[1]
file_name = sys.argv[2]

# Read the file and split lines into list of names
try:
    with open(file_name, 'r') as f:
        names_list = [line.strip().split() for line in f if line.strip()]
except FileNotFoundError:
    print(f"Error: File {file_name} not found.")
    sys.exit(1)

# Sort using the specified method
if sort_method == '-quick':
    quicksort(names_list)
elif sort_method == '-heap':
    heapsort(names_list)
else:
    print("Invalid sort method. Use -quick or -heap.")
    sys.exit(1)

# Print the sorted names to the console
for name in names_list:
    print(' '.join(name))