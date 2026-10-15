from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search, test_search_functions_printer)
import random, time

data_sizes = [5000, 50000, 100000, 150000, 1000000]
results_iterative_binary_search = []
results_recursive_binary_search = []
results_sequential_search = []

for size in data_sizes:
    print()
    number_of_trials = 10
    tracker = 1
    random_values = sorted(random.randint(1, 10) for _ in range(size))

    if random.random() < 0.5:
        target = random.choice(random_values)
    else:
        target = 1000001

    while number_of_trials > 0:
        start = time.perf_counter() #Iterative Binary
        IB_index = iterative_binary_search(random_values, target)
        IB_elapsed_microseconds = (time.perf_counter() - start) * 1000000
        results_iterative_binary_search.append(IB_elapsed_microseconds)

        start = time.perf_counter() #Recursive Binary
        RB_index = recursive_binary_search(random_values, target, 0, len(random_values)-1)
        RB_elapsed_microseconds = (time.perf_counter() - start) * 1000000
        results_recursive_binary_search.append(RB_elapsed_microseconds)

        start = time.perf_counter() #Sequential
        S_index = sequential_search(random_values, target)
        S_elapsed_microseconds = (time.perf_counter() - start) * 1000000
        results_sequential_search.append(S_elapsed_microseconds)


        print(f"The target({target}) was found at index {IB_index} in {IB_elapsed_microseconds:.2f} microseconds for Iterative Binary Search with list size {size}. Trial {tracker}")

        if IB_index != -1:
            assert random_values[IB_index] == target
        else:
            assert target not in random_values
        if RB_index != -1:
            assert random_values[RB_index] == target
        else:
            assert target not in random_values
        if S_index != -1:
            assert random_values[S_index] == target
        else:
            assert target not in random_values

        number_of_trials -= 1
        tracker += 1
    

print()
print()
print()
print(f"Results for Iterative Binary Search: {results_iterative_binary_search[10]}")