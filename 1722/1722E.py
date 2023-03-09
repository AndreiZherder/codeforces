import sys
from typing import List

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def prefix_sum_2d(grid: List[List[int]]) -> List[List[int]]:
    """
    returns the 2d prefix sum array of size (n + 1) * (m + 1) with 0 on first row and first col
    """
    n = len(grid)
    m = len(grid[0])
    pref = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] + grid[i - 1][j - 1] - pref[i - 1][j - 1]
    return pref


def sum_2d(pref: List[List[int]], row1: int, col1: int, row2: int, col2: int) -> int:
    """
    returns sum of rectangle area [row1, col1) - [row2, col2)
    need to calculate prefix_sum_2d first
    """
    return pref[row2][col2] - pref[row1][col2] - pref[row2][col1] + pref[row1][col1]


def solution():
    n, q = (int(num) for num in input().split())
    a = [[0 for j in range(1000)] for i in range(1000)]
    while n:
        h, w = (int(num) for num in input().split())
        a[h - 1][w - 1] += h * w
        n -= 1
    pref = prefix_sum_2d(a)
    while q:
        hs, ws, hb, wb = (int(num) for num in input().split())
        print(sum_2d(pref, hs, ws, hb - 1, wb - 1))
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
