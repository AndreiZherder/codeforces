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


def solution():
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    besti = -1
    best = -1
    for i in range(n):
        cur = 0
        for j in range(m):
            if a[i][j] == '#':
                cur += 1
        if cur > best:
            best = cur
            besti = i
    for j in range(m):
        if a[besti][j] == '#':
            print(besti + 1, j + best // 2 + 1)
            return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
