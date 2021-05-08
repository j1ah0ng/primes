from functools import reduce
from math import sqrt

def is_prime(n):
    if n < 2:
        return True
    else:
        return not reduce(lambda s0, s1: s0 if s0 else n % s1 == 0, range(2, int(sqrt(n)) + 1), False)

def sieve(lo, hi):
    return list(filter(is_prime, range(lo, hi + 1)))

def sieve_generator(lo, hi):
    for n in range(lo, hi + 1):
        if is_prime(n):
            yield n

def count_primes(lo, hi):
    return len(sieve(lo, hi))
