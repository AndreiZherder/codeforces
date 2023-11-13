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
    n, m, x, y, z, p = [int(num) for num in input().split()]
    x %= 4
    y %= 2
    z %= 4
    sn, sm = n, m
    while p:
        i, j = [int(num) - 1 for num in input().split()]
        n, m = sn, sm
        for k in range(x):
            i, j = j, n - i - 1
            n, m = m, n
        for k in range(y):
            j = m - j - 1
        for k in range(4 - z):
            i, j = j, n - i - 1
            n, m = m, n
        print(i + 1, j + 1)
        p -= 1


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
