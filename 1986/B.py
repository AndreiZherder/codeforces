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


d4 = ((0, 1), (-1, 0), (0, -1), (1, 0))


def solution():
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    for i in range(n):
        for j in range(m):
            mx = 0
            for di, dj in d4:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    mx = max(mx, a[ni][nj])
            if mx < a[i][j]:
                a[i][j] = mx
    for row in a:
        print(*row)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
