from collections import Counter
from os import path
from random import getrandbits
from sys import stdin, stdout


if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


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
    c = Counter(nums)
    nums.append(min(nums) - 1)
    nums = list(sorted(set(nums)))
    n = len(nums)
    cur = 0
    best = 0
    ans = (-1, -1)
    for i in range(n):
        if nums[i] == nums[i - 1] + 1:
            if c[nums[i]] >= k:
                cur += 1
            else:
                cur = 0
        else:
            if c[nums[i]] >= k:
                cur = 1
            else:
                cur = 0
        if cur > best:
            best = cur
            ans = (nums[i - cur + 1], nums[i])
    if ans != (-1, -1):
        print(*ans)
    else:
        print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
