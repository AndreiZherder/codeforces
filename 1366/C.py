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


def solution():
    d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    ans = 0
    l = (n + m - 1) // 2
    seen = {(0, 0), (n - 1, m - 1)}
    q = deque([(0, 0), (n - 1, m - 1)])
    q1 = deque()
    for k in range(l):
        digits = [0, 0]
        while q:
            i, j = q.popleft()
            digits[a[i][j]] += 1
            for di, dj in d4:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    q1.append((ni, nj))
        q, q1 = q1, q
        ans += min(digits)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
