# Linear Search algorithm to return index of search value

# Iterative method of linear search algorithm
def iter_linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        elif key not in arr:
            return -1

# Recursive method of linear search algorithm
def recur_linearSearch(arr, size, key):
    if size == 0:
        return -1
    
    elif arr[size - 1] == key:
        return size - 1
    else:
        return recur_linearSearch(arr, size - 1, key)

if __name__ == "__main__":
    # Iterative method of linear search algorithm
    print(iter_linearSearch([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 110))
    print(iter_linearSearch([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 175))

    # Recursive method of linear search algorithm
    print(recur_linearSearch([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 10, 110))
    print(recur_linearSearch([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 10, 175))