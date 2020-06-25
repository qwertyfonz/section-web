from functional import timer

@timer
def is_prime(n):
    """
    Very slow implementation
    """
    for i in range(1, n):
        if n % i == 0:
            return False
    return True

is_prime(5)

