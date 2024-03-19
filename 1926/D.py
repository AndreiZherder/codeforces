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
    nums = [Int(num) for num in input().split()]
    c = Counter(nums)
    ans1 = 0
    ans2 = 0
    for num in nums:
        if num in c:
            x = Int(~num & 0x7FFFFFFF)
            if x in c:
                ans1 += 1
                c[num] -= 1
                if c[num] == 0:
                    del c[num]
                c[x] -= 1
                if c[x] == 0:
                    del c[x]
            else:
                ans2 += 1
                c[num] -= 1
                if c[num] == 0:
                    del c[num]
    print(ans1 + ans2)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
