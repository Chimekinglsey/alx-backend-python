def fibonacci_memo(n, cache=None):
    print(cache)
    if cache is None:
        cache = {}  # Initialize the cache only once

    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    cache[n] = result  # Store the result in the cache
    return result
print(fibonacci_memo(5))
print(fibonacci_memo(4))
print(fibonacci_memo(5))