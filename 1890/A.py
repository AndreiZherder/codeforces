from collections import Counter
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
    c = Counter(Int(num) for num in input().split())
    ans = 'No'
    if len(c) == 1:
        ans = 'Yes'
    elif len(c) == 2:
        vs = list(c.values())
        if abs(vs[0] - vs[1]) <= 1:
            ans = 'Yes'
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
