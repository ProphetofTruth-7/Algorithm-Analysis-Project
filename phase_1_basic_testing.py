from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

values = [2, 3, 18, 7, 8, 16, 5, 13, 15]
values.sort()

target = 8
missing_target = 10

index_RBS = recursive_binary_search(values, target, 0, len(values)-1)
index_IBS = iterative_binary_search(values, target)
index_SS = sequential_search(values, target)

print (f"Recursive Binary Search: Target {target} found at index {index_RBS}")
print (f"Iterative Binary Search: Target {target} found at index {index_IBS}")
print (f"Sequential Search: Target {target} found at index {index_SS}")