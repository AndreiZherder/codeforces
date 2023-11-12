from collections import deque
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


d8 = ((0, 0), (0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def solution():
    n = 8
    a = [[] for k in range(n)]
    for i in range(n):
        a[0].append(list(input()))
    for k in range(1, n):
        a[k] = a[k - 1].copy()
        a[k].pop()
        a[k] = [['.'] * 8] + a[k]
    q = deque([(0, 7, 0)])
    seen = {(0, 7, 0)}
    while q:
        k, i, j = q.popleft()
        if k == 7:
            print('WIN')
            return
        for di, dj in d8:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if a[k][ni][nj] != 'S' and a[k + 1][ni][nj] != 'S':
                    if (k + 1, ni, nj) not in seen:
                        if (ni, nj) == (0, 7):
                            print('WIN')
                            return
                        seen.add((k + 1, ni, nj))
                        q.append((k + 1, ni, nj))
    print('LOSE')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
