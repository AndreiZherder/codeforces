from os import path
from sys import stdin, stdout
from typing import List

if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def second_min(nums: List[int]) -> int:
        mini = 0
        for i, num in enumerate(nums):
            if num < nums[mini]:
                mini = i
        sec_mini = 0 if mini != 0 else 1
        for i, num in enumerate(nums):
            if i != mini and num < nums[sec_mini]:
                sec_mini = i
        return nums[sec_mini]

    n = int(input())
    grid = []
    mn = 10 ** 20
    for i in range(n):
        m = int(input())
        grid.append([int(num) for num in input().split()])
        mn = min(mn, min(grid[-1]))
    sec_mns = [second_min(nums) for nums in grid]
    delta = min(sec_mns) - mn
    print(sum(sec_mns) - delta)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
