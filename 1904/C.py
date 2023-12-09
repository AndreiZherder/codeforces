from bisect import bisect_left, bisect_right
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


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    if k >= 3:
        print(0)
    else:
        best = min(nums)
        deltas = []
        for i in range(n):
            for j in range(i + 1, n):
                delta = abs(nums[i] - nums[j])
                deltas.append(delta)
                best = min(best, delta)
        if k == 2:
            nums.sort()
            for delta in deltas:
                i = bisect_left(nums, delta)
                if i < n:
                    best = min(best, abs(nums[i] - delta))
                i = bisect_right(nums, delta) - 1
                if i >= 0:
                    best = min(best, abs(nums[i] - delta))
        print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
