from os import path
from sys import stdin, stdout
from typing import List

filename = "../templates/input.txt"
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
    n, q, c = [int(num) for num in input().split()]
    c += 1
    sky = [[[0 for j in range(100)] for i in range(100)] for k in range(c)]
    while n:
        x, y, s = [int(num) for num in input().split()]
        x -= 1
        y -= 1
        for k in range(c):
            sky[k][x][y] += (s + k) % c
        n -= 1
    pref = [prefix_sum_2d(sky[k]) for k in range(c)]
    while q:
        t, x1, y1, x2, y2 = [int(num) for num in input().split()]
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        k = t % c
        print(sum_2d(pref[k], x1, y1, x2 + 1, y2 + 1))
        q -= 1


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
