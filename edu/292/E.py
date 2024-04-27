from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout


filename = '../../templates/input.txt'
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
    n, k = [int(num) for num in input().split()]
    nums = [Int(num) for num in input().split()]
    j = 0
    ans = 0
    c = Counter()
    for i in range(n):
        c[nums[i]] += 1
        while len(c) > k:
            c[nums[j]] -= 1
            if c[nums[j]] == 0:
                del c[nums[j]]
            j += 1
        ans += i - j + 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
