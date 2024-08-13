from os import path
from sys import stdin, stdout
from typing import List

filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


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
    returns sum of rectangle area [row1, col1] - (row2, col2)
    need to calculate prefix_sum_2d first
    """
    return pref[row2][col2] - pref[row1][col2] - pref[row2][col1] + pref[row1][col1]


def solution():
    def cell(i: int, j: int) -> int:
        return i * m + j

    def coords(x: int) -> (int, int):
        return x // m, x % m

    n, m, k = [int(num) for num in input().split()]
    w = int(input())
    a = [int(num) for num in input().split()]
    grid = [[0 for j in range(m)] for i in range(n)]
    cost = [0 for x in range(n * m)]
    for i in range(n):
        for j in range(m):
            cost[cell(i, j)] = (k - max(0, k - (i + 1)) - max(0, i + k - n)) * (k - max(0, k - (j + 1)) - max(0, j + k - m))
    # print('cost')
    # aa = [[0 for j in range(m)] for i in range(n)]
    # for i in range(n):
    #     for j in range(m):
    #         aa[i][j] = cost[cell(i, j)]
    # for row in aa:
    #     print(*row)
    order = sorted(range(n * m), key=cost.__getitem__, reverse=True)
    cost = []
    for x, ai in zip(order, sorted(a, reverse=True)):
        i, j = coords(x)
        grid[i][j] = ai
    order = []
    # print('grid')
    # for row in grid:
    #     print(*row)
    pref = prefix_sum_2d(grid)
    ans = 0
    for i in range(k - 1, n):
        for j in range(k - 1, m):
            ans += sum_2d(pref, i - k + 1, j - k + 1, i + 1, j + 1)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
