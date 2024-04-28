from collections import Counter
from heapq import heappush, heappop
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


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [Int(num) for num in input().split()]
    fs = list(Counter(nums).values())
    h = []
    for f in fs:
        heappush(h, (-(f // k), ceil(f, k) * k - f, f))
    reserve = 0
    while h:
        m, add, f = heappop(h)
        m = -m
        if m == 0 and add > reserve:
            print(f + sum(f for m, add, f in h))
            return
        elif m > 0:
            reserve += (k - 1) * m
            if add != 0:
                heappush(h, (0, add, f))
        else:
            reserve -= add
            reserve += k - 1
    if reserve >= k:
        print(k - 1)
    else:
        print(reserve)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
