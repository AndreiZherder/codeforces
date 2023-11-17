from itertools import accumulate
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
    n = int(input())
    a = [int(num) for num in input().split()]
    pref = list(accumulate(a, initial=0))
    best = 0
    for f in factors(n):
        if f != n:
            mx = -10 ** 20
            mn = 10 ** 20
            for i in range(0, n, f):
                mx = max(mx, pref[i + f] - pref[i])
                mn = min(mn, pref[i + f] - pref[i])
            best = max(best, mx - mn)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
