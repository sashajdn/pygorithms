def find_prime_factors(n):

    factors = (2, 3, 5, 7, 11)

    def calculate(n):
        for factor in factors:
            if n % factor == 0:
                yield factor
                yield from calculate(n / factor)
                break

    yield from calculate(n)


if __name__ == "__main__":
    # this is just logic to call from cli
    # eg python find_prime_factors.py 100
    import sys
    try:
        n = sys.argv[1]
    except IndexError:
        n = 1

    print(list(find_prime_factors(int(n))))
