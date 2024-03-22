from os import path
from sys import stdin, stdout
from typing import List

filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def maxSubArray(nums: List[int]) -> int:
    best = -10 ** 20
    cur = 0
    for num in nums:
        cur += num
        best = max(best, cur)
        cur = max(0, cur)
    return max(0, best)

def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    mod = 10 ** 9 + 7
    x = maxSubArray(nums)
    ans = sum(nums) % mod
    for i in range(k):
        ans = (ans + x) % mod
        x = (x * 2) % mod
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
