from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    x, y, z, k = [int(num) for num in input().split()]
    x, y, z = sorted([x, y, z], reverse=True)
    best = 0
    fs = list(factors(k))
    n = len(fs)
    for i in range(n):
        if fs[i] > x:
            break
        a = fs[i]
        for j in range(n):
            if fs[j] > y:
                break
            b = fs[j]
            if k % (a * b) == 0:
                c = k // (a * b)
                if c <= z:
                    best = max(best, (x - a + 1) * (y - b + 1) * (z - c + 1))
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
