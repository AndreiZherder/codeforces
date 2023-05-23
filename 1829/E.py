import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    grid = []
    for i in range(n):
        grid.append([int(num) for num in input().split()])
    steps = ((0, 1), (0, -1), (-1, 0), (1, 0))
    best = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] > 0:
                q = deque([(x, y)])
                cur = grid[x][y]
                grid[x][y] = 0
                while q:
                    i, j = q.popleft()
                    for di, dj in steps:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] > 0:
                            cur += grid[ni][nj]
                            q.append((ni, nj))
                            grid[ni][nj] = 0
                best = max(best, cur)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
