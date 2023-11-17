from collections import defaultdict, Counter
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
    def least_set_bit(n: int) -> int:
        """
        least_set_bit(12) -> 4
        1100 -> 0100
        """
        return n & -n


    n = int(input())
    nums = [int(num) for num in input().split()]
    d = defaultdict(lambda: Counter())
    for num in nums:
        k = 0
        cur = num
        while cur % 2 == 0:
            k += 1
            cur //= 2
        d[Int(cur)][Int(num - k)] += 1
    ans = 0
    for counter in d.values():
        for v in counter.values():
            ans += comb(v, 2)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
