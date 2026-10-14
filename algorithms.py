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

def test_search_functions(target, array):
    index_RBS = recursive_binary_search(array, target, 0, len(array)-1)
    index_IBS = iterative_binary_search(array, target)
    index_SS = sequential_search(array, target)

    print (f"Recursive Binary Search: Target {target} found at index {index_RBS}")
    print (f"Iterative Binary Search: Target {target} found at index {index_IBS}")
    print (f"Sequential Search: Target {target} found at index {index_SS}") 
    print()
    if target == 101:
        print(f"The Target is not present in the list.")
    else:
        print(f"The Target: {target}")
    print(f"The Sorted List: {array}")
    print()