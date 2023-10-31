from collections import defaultdict
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
    me = input()
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input().split()
        x = s[0]
        y = s[-2][:-2]
        action = s[1]
        if action == 'posted':
            if x == me:
                d[y] += 15
            elif y == me:
                d[x] += 15
            else:
                d[x] += 0
                d[y] += 0
        elif action == 'commented':
            if x == me:
                d[y] += 10
            elif y == me:
                d[x] += 10
            else:
                d[x] += 0
                d[y] += 0
        else:
            if x == me:
                d[y] += 5
            elif y == me:
                d[x] += 5
            else:
                d[x] += 0
                d[y] += 0
    print(*sorted(d, key=lambda x: (-d[x], x)), sep='\n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
