from typing import Tuple, List

mod = 1000000007


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Given two integers a and b, returns (gcd(a, b), x, y) such that
    a * x + b * y == gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def diophantine(a: int, b: int, c: int) -> Tuple[int, int]:
    """
    solves a * x + b * y = c
    has solution only if c % gcd(a, b) == 0
    returns (x0, y0)
    other solutions for equation are:
    x = x0 + k * b // gcd(a, b)
    y = y0 - k * a // gcd(a, b)
    """
    g, x, y = egcd(a, b)
    r = c // g
    return r * x, r * y


def madd(x: int, y: int) -> int:
    return (x + y) % mod


def msub(x: int, y: int) -> int:
    return (x - y) % mod


def mmul(x: int, y: int) -> int:
    return (x * y) % mod


def minv(x: int) -> int:
    """
    returns modular inverse of x when mod is prime or not prime
    ans = (1 / x) % mod
    gcd(y, mod) should be 1
    """
    g, inv, _ = egcd(x, mod)
    if g != 1:
        raise ValueError('gcd(x, mod) != 1')
    return inv % mod


def mdiv(x: int, y: int) -> int:
    """
    returns (x / y) % mod
    gcd(y, mod) should be 1
    """
    return (x * minv(y)) % mod


def mpow(x: int, y: int) -> int:
    """
    returns (x ** y) % mod
    """
    return pow(x, y, mod)


def ncr(n: int, r: int) -> int:
    """
    returns number of ways for selecting r elements out of n options
    """
    num, den = 1, 1
    for i in range(r):
        num = mmul(num, n - i)
        den = mmul(den, i + 1)
    return mdiv(num, den)


factorials = [1]
def fac(n, cache=True):
    """
    returns n!
    """
    if not cache:
        ans = 1
        for i in range(1, n + 1):
            ans = (ans * i) % mod
        return ans
    else:
        while len(factorials) < n + 1:
            factorials.append((factorials[-1] * len(factorials)) % mod)
        return factorials[n]


def perm(n, k, cache=True):
    """
    returns number of ways for selecting k elements out of n options with order
    """
    return mdiv(fac(n, cache=cache), fac(n - k, cache=cache))


def comb(n, k, cache=True):
    """
    returns number of ways for selecting k elements out of n options without order
    """
    return mdiv(fac(n, cache=cache), mmul(fac(k, cache=cache), fac(n - k, cache=cache)))


def pascal_triangle(n: int) -> List[List[int]]:
    """
    returns pascal triangle
    which element [n][k] is the binomial coefficient
    or number of ways for selecting k elements out of n options without order
    """
    ans = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        ans[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
    return ans
