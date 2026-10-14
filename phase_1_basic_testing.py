from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)
import unittest

def test_search_functions(target, array):
    index_RBS = recursive_binary_search(array, target, 0, len(array)-1)
    index_IBS = iterative_binary_search(array, target)
    index_SS = sequential_search(array, target)

    print (f"Recursive Binary Search: Target {target} found at index {index_RBS}")
    print (f"Iterative Binary Search: Target {target} found at index {index_IBS}")
    print (f"Sequential Search: Target {target} found at index {index_SS}") 
    print()

class testPhase1(unittest.TestCase):
    def setUp(self):
        self.full_list = [2, 3, 18, 7, 8, 16, 5, 13, 15]
        self.full_list.sort() #2, 3, 5, 7, 8, 13, 15, 16, 18
        self.one_list = [69]
        self.empty_list = []
        self.duplicate_list = [2, 3, 18, 7, 7, 5, 5, 13, 15]
        self.duplicate_list.sort() #2, 3, 5, 5, 7, 7, 13, 15, 18

    def test_middle_target(self):
        test_search_functions(8, self.full_list)

    def test_missing_target(self):
        test_search_functions(203, self.full_list)

    def test_first_target(self):
        test_search_functions(2, self.full_list)

    def test_last_target(self):
        test_search_functions(18, self.full_list)

    def test_onelist_target(self):
        test_search_functions(69, self.one_list)

    def test_onelist_missing_target(self):
        test_search_functions(2, self.one_list)

    def test_duplicatelist_target(self):
        test_search_functions(7, self.duplicate_list)

if __name__ == "__main__":
    unittest.main()