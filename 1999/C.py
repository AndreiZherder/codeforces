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
    n, s, m = [int(num) for num in input().split()]
    cur = 0
    intervals = []
    for i in range(n):
        intervals.append([int(num) for num in input().split()])
    for l, r in intervals:
        if l - cur >= s:
            print('YES')
            return
        cur = r
    if m - cur >= s:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
