from collections import defaultdict
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


def solution():
    def bsr(left: int, right: int) -> int:
        """
        TTTTFFFF
            |
        """

        def check(mid: int) -> bool:
            return trips[d[y][mid]][0] <= r

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


    n, x = [int(num) for num in input().split()]
    INF = 10 ** 20
    trips = []
    for i in range(n):
        trips.append([int(num) for num in input().split()])
    d = defaultdict(list)
    suf = defaultdict(list)
    for i, (l, r, c) in enumerate(trips):
        d[r - l + 1].append(i)
    for y in d:
        d[y].sort(key=lambda i: trips[i][0])
        m = len(d[y])
        suf[y] = [INF for i in range(m)]
        suf[y][m - 1] = trips[d[y][m - 1]][2]
        for i in range(m - 2, -1, -1):
            suf[y][i] = min(suf[y][i + 1], trips[d[y][i]][2])
    best = INF
    for l, r, c in trips:
        y = x - (r - l + 1)
        if y in d:
            j = bsr(0, len(d[y]) - 1)
            if j < len(d[y]):
                best = min(best, c + suf[y][j])
    print(best if best != INF else -1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
