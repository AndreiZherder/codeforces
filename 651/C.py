from collections import Counter
from math import comb
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


RANDOM = getrandbits(32)


class Int(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM


def solution():
    n = int(input())
    a, b, c = Counter(), Counter(), Counter()
    for i in range(n):
        x, y = [Int(num) for num in input().split()]
        a[x] += 1
        b[y] += 1
        c[(x, y)] += 1
    ans = 0
    for v in a.values():
        ans += comb(v, 2)
    for v in b.values():
        ans += comb(v, 2)
    for v in c.values():
        ans -= comb(v, 2)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
