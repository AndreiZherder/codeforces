from itertools import accumulate
from operator import xor
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
    n = int(input())
    a = [int(num) for num in input().split()]
    q = int(input())
    p = [n for i in range(n)]
    for i in range(n - 2, -1, -1):
        if a[i] == a[i + 1]:
            p[i] = p[i + 1]
        else:
            p[i] = i + 1
    while q:
        l, r = [int(num) - 1 for num in input().split()]
        if p[l] > r:
            print(-1, -1)
        else:
            print(l + 1, p[l] + 1)
        q -= 1
    print()


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
