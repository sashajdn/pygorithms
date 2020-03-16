"""Problem: Nth Fibonacci.

Write a function that takes in an integer, `n` and returns the Nth-Fibonacci number

### --- LAMBDA CALC --- ###

## -- COMPLEXITY -- ##
"""

add = lambda n: lambda m: n if m==0 else add(n)(m-1) + 1
fib = lambda n, a=0, b=1: a if n <= 0 else fib(n-1, a=b, b=add(a)(b))


if __name__ == " __main__":
    import sys
    print(fib(sys.argv[1]))
