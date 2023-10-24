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
    n = int(input())
    nums = [int(num) for num in input().split()]
    ps = {p ** 2 for p in sieve(10 ** 6)}
    for num in nums:
        print('YES' if num in ps else 'NO')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
