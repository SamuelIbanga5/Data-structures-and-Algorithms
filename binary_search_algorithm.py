# Binary Search algorithm 
def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while high - low > 1:
        mid = (low + high) // 2
        if key > arr[mid]:
            low = mid
        else:
            high = mid

    if arr[low] == key:
        print("Found At Index", low)
    elif arr[high] == key:
        print("Found at Index", high)
    else:
        print("Not Found")

if __name__ == "__main__":
    binarySearch([10, 20, 30, 50, 60, 80, 100, 110, 130, 170], 110)