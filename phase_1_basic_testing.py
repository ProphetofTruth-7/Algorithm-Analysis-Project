from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search, test_search_functions_printer)
import unittest

class testPhase1(unittest.TestCase):
    def setUp(self):
        self.full_list = [2, 3, 18, 7, 8, 16, 5, 13, 15]
        self.full_list.sort() #2, 3, 5, 7, 8, 13, 15, 16, 18
        self.one_list = [69]
        self.empty_list = []
        self.duplicate_list = [2, 3, 18, 7, 7, 5, 5, 13, 15]
        self.duplicate_list.sort() #2, 3, 5, 5, 7, 7, 13, 15, 18

 
    def test_middle_target(self):
        self.assertEqual(4, recursive_binary_search(self.full_list, 8, 0, len(self.full_list)-1))
        self.assertEqual(4, iterative_binary_search(self.full_list, 8))
        self.assertEqual(4, sequential_search(self.full_list, 8))

    def test_missing_target(self):
        self.assertEqual(-1, recursive_binary_search(self.full_list, 203, 0, len(self.full_list)-1))
        self.assertEqual(-1, iterative_binary_search(self.full_list, 203))
        self.assertEqual(-1, sequential_search(self.full_list, 203))

    def test_first_target(self):
        self.assertEqual(0, recursive_binary_search(self.full_list, 2, 0, len(self.full_list)-1))
        self.assertEqual(0, iterative_binary_search(self.full_list, 2))
        self.assertEqual(0, sequential_search(self.full_list, 2))

    def test_last_target(self):
        self.assertEqual(8, recursive_binary_search(self.full_list, 18, 0, len(self.full_list)-1))
        self.assertEqual(8, iterative_binary_search(self.full_list, 18))
        self.assertEqual(8, sequential_search(self.full_list, 18))

    def test_onelist_target(self):
        self.assertEqual(0, recursive_binary_search(self.one_list, 69, 0, len(self.one_list)-1))
        self.assertEqual(0, iterative_binary_search(self.one_list, 69))
        self.assertEqual(0, sequential_search(self.one_list, 69))

    def test_onelist_missing_target(self):
        self.assertEqual(-1, recursive_binary_search(self.one_list, 2, 0, len(self.one_list)-1))
        self.assertEqual(-1, iterative_binary_search(self.one_list, 2))
        self.assertEqual(-1, sequential_search(self.one_list, 2))

    def test_duplicatelist_target(self):
        self.assertEqual(4, recursive_binary_search(self.duplicate_list, 7, 0, len(self.duplicate_list)-1))
        self.assertEqual(4, iterative_binary_search(self.duplicate_list, 7))
        self.assertEqual(4, sequential_search(self.duplicate_list, 7))

    def test_print(self):
        test_search_functions_printer(8, self.full_list)

if __name__ == "__main__":
    unittest.main()