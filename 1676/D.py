from collections import Counter
from os import path
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    d1 = Counter()
    d2 = Counter()
    for i in range(n):
        for j in range(m):
            d1[i - j] += a[i][j]
            d2[i + j] += a[i][j]
    best = 0
    for i in range(n):
        for j in range(m):
            best = max(best, d1[i - j] + d2[i + j] - a[i][j])
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
