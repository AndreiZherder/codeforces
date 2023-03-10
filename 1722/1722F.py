import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    grid = []
    for i in range(n):
        grid.append(list(input()))
    steps = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                grid[i][j] = '.'
                painted = [(i, j)]
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in steps:
                        if 0 <= x + dx < n and 0 <= y + dy < m:
                            if grid[x + dx][y + dy] == '*':
                                grid[x + dx][y + dy] = '.'
                                painted.append((x + dx, y + dy))
                                q.append((x + dx, y + dy))
                if len(painted) != 3:
                    print('NO')
                    return
                if len(set(x for x, y in painted)) != 2 or len(set(y for x, y in painted)) != 2:
                    print('NO')
                    return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
