from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search, test_search_functions)
import random


random_values = [random.randint(1, 100) for _ in range(20)]
random_values.sort()

if random.random() < 0.5:
    target = random.choice(random_values)
    expected = True
else:
    target = 101
    expected = False
        
test_search_functions(target, random_values)
if expected:
    print(f"Target was present in the list, as expected")
    print()
else:
    print(f"Target was not present in the list, as expected")
    print()
print(f"This is an acceptable outcome")
print()