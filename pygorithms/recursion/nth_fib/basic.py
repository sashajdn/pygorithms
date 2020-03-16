"""Problem: Nth Fibonacci.

Write a function that takes in an integer, `n` and returns the Nth-Fibonacci number

### --- BASIC --- ###

## -- COMPLEXITY -- ##
"""


def nthfib_basic(n):
    """Gets the nth fib."""
    if n < 2:
        return n

    return nthfib_basic(n-1) + nthfib_basic(n-2)


if __name__ == " __main__":
    import sys
    print(nthfib_basic(sys.argv[1]))
