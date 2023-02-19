import sys
from itertools import chain
from math import gcd

M = 1000000007
mod = 998244353


def input_interactive(*args):
    print(' '.join(chain('?', map(str, args))))
    sys.stdout.flush()
    return input()


def print_interactive(*args):
    print(' '.join(chain('!', map(str, args))))
    sys.stdout.flush()


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


def bin_to_dec(n: str) -> int:
    return int(n, 2)


def is_power_of_two(n: int) -> bool:
    return n & (n - 1) == 0


def least_set_bit(n: int) -> int:
    """
    Least significant set bit
    """
    return n & ~(n - 1)


def set_bits_count(n: int) -> int:
    """
    Count set bits in an integer
    """
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


def gcd_small(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_big(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while ((a | b) & 1) == 0:
        a = a >> 1
        b = b >> 1
        k = k + 1
    while (a & 1) == 0:
        a = a >> 1
    while b != 0:
        while (b & 1) == 0:
            b = b >> 1
        if a > b:
            temp = a
            a = b
            b = temp
        b = b - a
    return a << k


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def sieve(n: int):
    primes = bytearray(n + 1)
    p = 3
    while p * p <= n:
        if not primes[p]:
            primes[p * p::p] = [1] * len(primes[p * p::p])
        p += 2
    if n >= 2:
        yield 2
    for p in range(3, n + 1, 2):
        if not primes[p]:
            yield p


def prime_factors(n: int):
    """
    Prime factors of n
    prime_factors(99) --> 3 3 11
    """
    while n % 2 == 0:
        yield 2
        n //= 2
    p = 3
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            n = quotient
        else:
            p += 2
    if n != 1:
        yield n


def is_prime(n: int):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    # all primes > 3 are of the form 6n ± 1
    p = 5
    while p * p <= n:
        if n % p == 0:
            return False
        if n % (p + 2) == 0:
            return False
        p += 6
    return True


def factors(n: int):
    stack = []
    yield 1
    if n != 1:
        stack.append(n)
    p = 2
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            if quotient != p:
                stack.append(quotient)
        p += 1
    while stack:
        yield stack.pop()


def ncr(n: int, r: int, mod: int) -> int:
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod - 2, mod)) % mod


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1
