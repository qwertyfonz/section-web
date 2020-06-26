def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

ls = [i for i in range(20)]

from filter import filter


print(f"Primes: {filter(ls, is_prime)}")