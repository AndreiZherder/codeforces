import sys
from math import gcd
from typing import Tuple


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


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


def solution():
    a, b, c = [int(num) for num in input().split()]
    g = gcd(a, b)
    if c % g == 0:
        a //= g
        b //= g
        c //= g
        x, y = diophantine(a, b, c)
        if x >= 0 and y >= 0:
            print('Yes')
            return
        else:
            if x < 0:
                k = (-x + b - 1) // b
                y = y - k * a
                if y >= 0:
                    print('Yes')
                    return
            if y < 0:
                k = -((-y + a - 1) // a)
                x = x + k * b
                if x >= 0:
                    print('Yes')
                    return
    print('No')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
