from bisect import bisect_left
from itertools import chain, combinations
from math import gcd
from typing import List, Tuple

M = 1000000007
mod = 998244353

"""
Binary, math, combinatorics
"""


# -x = ~x + 1
# ~x = -x - 1
# x & (x - 1)   sets the last one bit to zero
# x & -x        sets all one bits to zero, except the last one bit
# x | (x - 1)   sets all bits to one after the last one bit


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


def bin_to_dec(n: str) -> int:
    return int(n, 2)


def popcount(n: int) -> int:
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


# bit_length(n: int) -> int
"""
most_set_bit
bit_length(6) -> 3
"""


def least_set_bit(n: int) -> int:
    """
    least_set_bit(6) -> 2
    """
    return n & -n


def is_power_of_two(n: int) -> bool:
    return n & (n - 1) == 0


def get_subsets(x: int) -> List[int]:
    """
    get all subsets of set x
    """
    ans = []
    b = 0
    while b != x:
        b = (b - x) & x
        ans.append(b)
    return ans


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
            a, b = b, a
        b = b - a
    return a << k


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def sieve(n: int):
    """
    Primes <= n
    """
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
    """
    Distinct factors of n
    """
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


def modular_exponentiation(x: int, y: int, mod: int):
    """
    returns (x ** y) % p
    """
    res = 1
    x = x % mod
    if x == 0:
        return 0
    while y > 0:
        if y & 1 == 1:
            res = (res * x) % mod
        y = y >> 1
        x = (x * x) % mod
    return res


def mod_inverse(x, mod):  # returns (1 / x) % mod
    if gcd(x, mod) == 1:
        return modular_exponentiation(x, mod - 2, mod)


def ncr(n: int, r: int, mod: int) -> int:
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod - 2, mod)) % mod


# https://github.com/lapets/egcd/blob/main/src/egcd/egcd.py
def egcd(b: int, n: int) -> Tuple[int, int, int]:
    """
    Given two integers b and n, returns (gcd(b, n), a, m) such that
    a*b + n*m == gcd(b, n).
    """
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return b, x0, y0


def diophantine(a: int, b: int, c: int) -> Tuple[int, int]:
    """
    solves a*x + b*y = c
    """
    d, x, y = egcd(a, b)
    r = c // d
    return r * x, r * y


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def prefix_sum_2d(grid: List[List[int]]) -> List[List[int]]:
    """
    Returns the 2d prefix sum array of size (n + 1) * (m + 1) with 0 on first row and first col
    """
    n = len(grid)
    m = len(grid[0])
    pref = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] + grid[i - 1][j - 1] - pref[i - 1][j - 1]
    return pref


def lis(nums: List[int]) -> int:
    """
    Longest increasing subsequence
    """
    dp = []
    for num in nums:
        i = bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)
