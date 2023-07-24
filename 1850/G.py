from collections import Counter
from math import comb
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    xs = Counter()
    ys = Counter()
    deltas1 = Counter()
    deltas2 = Counter()
    for i in range(n):
        x, y = (int(num) for num in input().split())
        xs[str(x)] += 1
        ys[str(y)] += 1
        deltas1[str(x + y)] += 1
        deltas2[str(y - x)] += 1
    ans = 0
    for v in xs.values():
        ans += comb(v, 2)
    for v in ys.values():
        ans += comb(v, 2)
    for v in deltas1.values():
        ans += comb(v, 2)
    for v in deltas2.values():
        ans += comb(v, 2)
    print(2 * ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
