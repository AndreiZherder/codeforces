from bisect import bisect_right
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
    n = int(input())
    nums = sorted((int(num) for num in input().split()))
    j = bisect_right(nums, 1)
    if j == n:
        if nums[-1] == 1:
            nums[-1] = 2
        print(*nums)
    else:
        print(*(nums[:j] + [1] + nums[j:n - 1]))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
