from bisect import bisect_right
from math import comb
from os import path
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
    n, d = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    ans = 0
    for i in range(n - 2):
        j = bisect_right(nums, nums[i] + d) - 1
        ans += comb(j - i, 2)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
