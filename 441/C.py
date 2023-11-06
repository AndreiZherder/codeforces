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
    n, m, k = [int(num) for num in input().split()]
    points = []
    dj = -1
    j = -1
    for i in range(n):
        dj = -dj
        j += dj
        while 0 <= j <= m - 1:
            points.append((i, j))
            j += dj
    for i in range(k - 1):
        print(2, points[2 * i][0] + 1, points[2 * i][1] + 1, points[2 * i + 1][0] + 1, points[2 * i + 1][1] + 1)
    print(len(points) - 2 * (k - 1), end=' ')
    for i in range(2 * k - 2, len(points)):
        print(points[i][0] + 1, points[i][1] + 1, end=' ')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
