from heapq import nsmallest
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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, m, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    if k % m == 0:
        d = k // m
        c = sorted((ai, i) for i, ai in enumerate(a))[:d]
        c.sort(key=lambda x: x[1])
        c = [ci[0] for ci in c]
        ans = 0
        cost = 0
        for ci in c:
            ans += m * (ci + cost)
            cost += m
        print(ans)
    else:
        d = ceil(k, m)
        r = k % m
        c = sorted((ai, i) for i, ai in enumerate(a))[:d]
        c.sort(key=lambda x: x[1])
        c = [ci[0] for ci in c]
        total = 0
        cost = 0
        for i in range(len(c)):
            total += m * (c[i] + cost)
            cost += m

        cur = 0
        cost = 0
        best = 10 ** 20
        for i in range(len(c)):
            best = min(best, cur + r * (c[i] + cost) + (total - cur - m * (c[i] + cost) - (m - r) * m * (len(c) - i - 1)))
            cur += m * (c[i] + cost)
            cost += m
        print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
