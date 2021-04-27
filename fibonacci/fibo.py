# an empty dictionary to store cached values
fibonacci_cache = {}


def fibonacci(n):
    """
    Recursively calculates the nth term of the fibonacci sequence, for n > 0.
    Return example: fibonacci(7) ---> 13.
    """

    # checks if certain value have been already calculated to speed up the recursion
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci_cache[n] = value

    return value
