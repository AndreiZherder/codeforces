from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = '../templates/input.txt'
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
    a = [Int(num) for num in input().split()]
    b = [Int(num) for num in input().split()]
    m = int(input())
    d = [Int(num) for num in input().split()]
    need = Counter()
    for ai, bi in zip(a, b):
        if ai != bi:
            need[bi] += 1
    s = set(b)
    stack = []
    for num in d:
        if num in s:
            stack = []
            if num in need:
                need[num] -= 1
                if need[num] == 0:
                    del need[num]
        else:
            stack.append(num)
    if need or stack:
        print('NO')
    else:
        print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
