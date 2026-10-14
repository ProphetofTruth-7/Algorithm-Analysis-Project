from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search, test_search_functions_printer)
import random

random_values = sorted(random.randint(1, 1000000) for _ in range(5000))

if random.random() < 0.5:
    target = random.choice(random_values)
else:
    target = 1000001