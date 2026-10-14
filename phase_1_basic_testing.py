from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

def test_search_functions(target, array):
    index_RBS = recursive_binary_search(array, target, 0, len(array)-1)
    index_IBS = iterative_binary_search(array, target)
    index_SS = sequential_search(array, target)

    print (f"Recursive Binary Search: Target {target} found at index {index_RBS}")
    print (f"Iterative Binary Search: Target {target} found at index {index_IBS}")
    print (f"Sequential Search: Target {target} found at index {index_SS}") 
    print()



full_list = [2, 3, 18, 7, 8, 16, 5, 13, 15]
full_list.sort() #2, 3, 5, 7, 8, 13, 15, 16, 18
one_list = [69]
empty_list = []
duplicate_list = [2, 3, 18, 7, 7, 5, 5, 13, 15]
duplicate_list.sort() #2, 3, 5, 5, 7, 7, 13, 15, 18

#Middle Target
test_search_functions(8, full_list)
#Missing Target
test_search_functions(203, full_list)
#First Target
test_search_functions(2, full_list)
#Last Target
test_search_functions(18, full_list)
#OneList Target
test_search_functions(69, one_list)
#OneList Missing Target
test_search_functions(2, one_list)
#DuplicateList Target
test_search_functions(7, duplicate_list)


