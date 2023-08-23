from collections import Counter
from itertools import count
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
    cnt = Counter(Int(num) for num in input().split())
    m = int(input())
    b = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    print(max(range(m), key=lambda i: (cnt[Int(b[i])], cnt[Int(c[i])])) + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
