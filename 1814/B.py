import sys
from math import gcd


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


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


def solution():
    a, b = (int(num) for num in input().split())
    a, b = min(a, b), max(a, b)
    if a == 1:
        if b == 1:
            print(2)
            return
        elif b == 2:
            print(3)
            return
        else:
            best = 10 ** 20
            facts = list(factors(b))
            if len(facts) > 2:
                for factor in facts:
                    best = min(best, factor + b // factor)
            else:
                for factor in factors(b - 1):
                    best = min(best, 1 + factor + (b - 1) // factor)

            print(best)
            return

    ans = 0
    g = gcd(a, b)
    if g == 1:
        if a % 2 == 1:
            ans += 1
            a -= 1
        if b % 2 == 1:
            ans += 1
            b -= 1
        g = gcd(a, b)


    best = 10 ** 20
    for factor in factors(g):
        best = min(best, factor - 1 + a // factor + b // factor)
    print(ans + best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
