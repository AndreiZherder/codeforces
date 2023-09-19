from bisect import bisect_left
from itertools import chain, combinations
from math import gcd
from random import getrandbits
from typing import List, Callable
from types import GeneratorType

"""
Recursion decorator for Python
Do not forget to write yield before recursive call and instead of return.
Write yield instead of return even if you return nothing.

@bootstrap
def dfs(v: int) -> int:
    ans = 0
    for u in g[v]:
        ans += yield dfs(u)
    yield ans
"""


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


"""
Protection from set and dict collision hacks
"""

RANDOM = getrandbits(32)


class Int(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM


"""
Binary, combinatorics
"""


# -x = ~x + 1
# ~x = -x - 1
# x & (x - 1)   sets the last one bit to zero
# x & -x        sets all one bits to zero, except the last one bit
# x | (x - 1)   sets all bits to one after the last one bit


def sn(a1: int, an: int, n: int) -> int:
    return (a1 + an) * n // 2


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


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


def most_set_bit(n: int) -> int:
    """
    most_set_bit(6) -> 4
    0110 -> 0100
    """
    return 1 << (n.bit_length() - 1)


def least_set_bit(n: int) -> int:
    """
    least_set_bit(6) -> 2
    0110 -> 0010
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


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def kbits(n: int, k: int) -> List[int]:
    """
    get all n-bit nums with k bits set
    """
    ans = []
    for bits in combinations(range(n), k):
        cur = 0
        for bit in bits:
            cur |= 1 << bit
        ans.append(cur)
    return ans


def backtrack(used: int, cur: List[int]):
    if used == (1 << n) - 1:
        ans.append(cur.copy())
        return
    for j in range(n):
        if used & 1 << j == 0:
            used |= 1 << j
            cur.append(nums[j])
            backtrack(used, cur)
            cur.pop()
            used &= ~(1 << j)


"""
Number theory
"""


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


def prefix_sum_2d(grid: List[List[int]]) -> List[List[int]]:
    """
    returns the 2d prefix sum array of size (n + 1) * (m + 1) with 0 on first row and first col
    """
    n = len(grid)
    m = len(grid[0])
    pref = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] + grid[i - 1][j - 1] - pref[i - 1][j - 1]
    return pref


def sum_2d(pref: List[List[int]], row1: int, col1: int, row2: int, col2: int) -> int:
    """
    returns sum of rectangle area [row1, col1] - (row2, col2)
    need to calculate prefix_sum_2d first
    """
    return pref[row2][col2] - pref[row1][col2] - pref[row2][col1] + pref[row1][col1]


def lis(nums: List[int]) -> int:
    """
    longest increasing subsequence
    """
    dp = []
    for num in nums:
        i = bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)


def bsl(left: int, right: int) -> int:
    """
    FFFFTTTT
        |
    """
    def check(mid: int) -> bool:
        return True

    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


def bsr(left: int, right: int) -> int:
    """
    TTTTFFFF
        |
    """
    def check(mid: int) -> bool:
        return True

    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return left


d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))
d8 = ((0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
