from itertools import accumulate
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
    a = [int(num) for num in input().split()]
    ops = []
    for i in range(m):
        ops.append([int(num) for num in input().split()])
    diff = [0 for i in range(m + 1)]
    for i in range(k):
        l, r = [int(num) for num in input().split()]
        l -= 1
        r -= 1
        diff[l] += 1
        diff[r + 1] -= 1
    b = list(accumulate(diff))
    diff = [0 for i in range(n + 1)]
    for x, (l, r, d) in zip(b, ops):
        l -= 1
        r -= 1
        diff[l] += d * x
        diff[r + 1] -= d * x
    b = list(accumulate(diff))
    print(*(ai + bi for ai, bi in zip(a, b)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
