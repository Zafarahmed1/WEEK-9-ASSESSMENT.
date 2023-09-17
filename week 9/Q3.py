from functools import reduce
n = 50
fibonacci_series = [0, 1]
fibonacci_series = reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), fibonacci_series)
print(f"Fibonacci series (first {n} elements): {fibonacci_series}")