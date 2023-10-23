from bisect import bisect_left
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


def solution():
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    b = [[0 for j in range(m)] for i in range(n)]
    ps = list(sieve(10 ** 5 + 100))
    for i in range(n):
        for j in range(m):
            k = bisect_left(ps, a[i][j])
            b[i][j] = ps[k] - a[i][j]
    best = 10 ** 20
    for i in range(n):
        best = min(best, sum(b[i]))
    for j in range(m):
        best = min(best, sum(b[i][j] for i in range(n)))
    print(best)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
