from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search, test_search_functions)
import random
import unittest

class testPhase2(unittest.TestCase):
    def setUp(self):
        self.list = [random.randint(1, 100) for _ in range(20)]
        self.list.sort()

    def test_print(self):
        if random.random() < 0.5:
            target = random.choice(self.list)
            expected_to_be_present = True
        else:
            target = 101
            expected_to_be_present = False

        test_search_functions(target, self.list)

if __name__ == "__main__":
    unittest.main()