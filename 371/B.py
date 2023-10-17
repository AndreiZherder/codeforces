from collections import Counter
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


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


def solution():
    a, b = [int(num) for num in input().split()]
    c1 = Counter(prime_factors(a))
    c2 = Counter(prime_factors(b))
    ans = 0
    for p in (2, 3, 5):
        ans += max(c1[p], c2[p]) - min(c1[p], c2[p])
    for p, v in c1.items():
        if p not in (2, 3, 5) and c1[p] != c2[p]:
            print(-1)
            return
    for p, v in c2.items():
        if p not in (2, 3, 5) and c1[p] != c2[p]:
            print(-1)
            return
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
