from itertools import groupby
from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    if all(num == nums[0] for num in nums):
        print(-1)
        return
    if nums[0] != nums[-1]:
        print(0)
        return
    best = 10 ** 20
    prev = nums[0]
    for k, g in groupby(nums):
        if k == nums[0]:
            best = min(best, len(list(g)))
        else:
            if len(list(g)) > 1 or prev != nums[0]:
                print(0)
                return
        prev = k

    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
