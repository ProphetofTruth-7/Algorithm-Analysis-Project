def recursive_binary_search(array, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recursive_binary_search(array, target, low, mid - 1)
    else:
        return recursive_binary_search(array, target, mid + 1, high)

def iterative_binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def sequential_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1